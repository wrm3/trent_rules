"""Portable Database Explorer API — schema introspection, data browsing, read-only SQL.

A self-contained FastAPI router for PostgreSQL database exploration.
Provides table listing with metadata, paginated data browsing, and a
read-only SQL runner with safety guards.

INTEGRATION NOTES:
  1. Import `router` and include it in your FastAPI app.
  2. Provide your own `get_db` dependency that yields an AsyncSession.
  3. Provide your own `require_admin` dependency for access control.
  4. See README.md for full integration instructions.
"""
import re
import time
import uuid
from datetime import datetime, date
from decimal import Decimal
from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel as PydanticBase, Field
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

# ---------------------------------------------------------------------------
# 🔧 INTEGRATION POINT: Replace these with your project's dependencies
# ---------------------------------------------------------------------------

# Option A: Import your project's database session dependency
# from app.core.database import get_db

# Option B: Define a placeholder — replace with your actual implementation
async def get_db():
    """Yields an AsyncSession. REPLACE with your project's DB dependency."""
    raise NotImplementedError(
        "Replace get_db() with your project's database session dependency. "
        "It should yield a sqlalchemy.ext.asyncio.AsyncSession."
    )

async def require_admin():
    """Access control dependency. REPLACE with your project's auth check."""
    raise NotImplementedError(
        "Replace require_admin() with your project's admin auth dependency. "
        "It should raise HTTPException(403) if the user is not an admin."
    )

# ---------------------------------------------------------------------------
# Router
# ---------------------------------------------------------------------------

router = APIRouter(prefix="/admin/db", tags=["admin-db"])

# Which schemas to expose (customize for your project)
ALLOWED_SCHEMAS = ("public",)

# ---------------------------------------------------------------------------
# Response schemas
# ---------------------------------------------------------------------------

class ColumnInfo(PydanticBase):
    name: str
    data_type: str
    is_nullable: bool
    column_default: Optional[str] = None
    is_primary_key: bool = False
    max_length: Optional[int] = None

class ForeignKeyInfo(PydanticBase):
    column: str
    references_schema: str
    references_table: str
    references_column: str

class IndexInfo(PydanticBase):
    name: str
    columns: list[str]
    is_unique: bool

class TableInfo(PydanticBase):
    schema_name: str = Field(alias="schema")
    table_name: str
    estimated_rows: int
    columns: list[ColumnInfo]
    foreign_keys: list[ForeignKeyInfo]
    indexes: list[IndexInfo]

    model_config = {"populate_by_name": True}

class TablesResponse(PydanticBase):
    tables: list[TableInfo]
    total: int

class DataResponse(PydanticBase):
    columns: list[str]
    rows: list[dict[str, Any]]
    total_count: int
    page: int
    page_size: int
    has_more: bool

class QueryRequest(PydanticBase):
    sql: str

class QueryResponse(PydanticBase):
    columns: list[str]
    rows: list[dict[str, Any]]
    row_count: int
    execution_ms: float
    truncated: bool = False


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_DANGEROUS_PATTERN = re.compile(
    r"\b(INSERT|UPDATE|DELETE|DROP|ALTER|TRUNCATE|CREATE|GRANT|REVOKE|COPY|EXECUTE|CALL)\b",
    re.IGNORECASE,
)


def _validate_readonly_sql(sql: str) -> None:
    """Reject anything that isn't a plain SELECT or WITH...SELECT."""
    stripped = sql.strip().rstrip(";").strip()
    if not stripped:
        raise HTTPException(status_code=400, detail="Empty query")
    if _DANGEROUS_PATTERN.search(stripped):
        raise HTTPException(status_code=400, detail="Only SELECT queries are allowed")
    upper = stripped.upper()
    if not (upper.startswith("SELECT") or upper.startswith("WITH") or upper.startswith("EXPLAIN")):
        raise HTTPException(status_code=400, detail="Query must start with SELECT, WITH, or EXPLAIN")


def _safe_value(val: Any) -> Any:
    """Serialize a DB value to JSON-safe form."""
    if val is None:
        return None
    if isinstance(val, uuid.UUID):
        return str(val)
    if isinstance(val, (datetime, date)):
        return val.isoformat()
    if isinstance(val, Decimal):
        return float(val)
    if isinstance(val, bytes):
        return val.hex()
    if isinstance(val, memoryview):
        return bytes(val).hex()
    return val


def _schema_filter_sql() -> str:
    """Build a SQL IN clause for allowed schemas."""
    quoted = ", ".join(f"'{s}'" for s in ALLOWED_SCHEMAS)
    return f"({quoted})"


# ---------------------------------------------------------------------------
# GET /admin/db/tables — schema introspection
# ---------------------------------------------------------------------------

@router.get("/tables", response_model=TablesResponse)
async def list_tables(
    db: AsyncSession = Depends(get_db),
    _admin=Depends(require_admin),
):
    """List all tables with columns, FKs, indexes, and estimated row counts."""
    schemas_in = _schema_filter_sql()

    tables_q = text(f"""
        SELECT
            schemaname  AS schema_name,
            relname     AS table_name,
            COALESCE(n_live_tup, 0) AS estimated_rows
        FROM pg_stat_user_tables
        WHERE schemaname IN {schemas_in}
        ORDER BY schemaname, relname
    """)
    tables_result = await db.execute(tables_q)
    tables_raw = tables_result.mappings().all()

    cols_q = text(f"""
        SELECT
            c.table_schema,
            c.table_name,
            c.column_name,
            c.data_type,
            c.udt_name,
            c.is_nullable,
            c.column_default,
            c.character_maximum_length,
            CASE WHEN pk.column_name IS NOT NULL THEN true ELSE false END AS is_primary_key
        FROM information_schema.columns c
        LEFT JOIN (
            SELECT kcu.table_schema, kcu.table_name, kcu.column_name
            FROM information_schema.table_constraints tc
            JOIN information_schema.key_column_usage kcu
                ON tc.constraint_name = kcu.constraint_name
                AND tc.table_schema = kcu.table_schema
            WHERE tc.constraint_type = 'PRIMARY KEY'
        ) pk ON c.table_schema = pk.table_schema
            AND c.table_name = pk.table_name
            AND c.column_name = pk.column_name
        WHERE c.table_schema IN {schemas_in}
        ORDER BY c.table_schema, c.table_name, c.ordinal_position
    """)
    cols_result = await db.execute(cols_q)
    cols_raw = cols_result.mappings().all()

    fks_q = text(f"""
        SELECT
            tc.table_schema,
            tc.table_name,
            kcu.column_name,
            ccu.table_schema AS ref_schema,
            ccu.table_name   AS ref_table,
            ccu.column_name  AS ref_column
        FROM information_schema.table_constraints tc
        JOIN information_schema.key_column_usage kcu
            ON tc.constraint_name = kcu.constraint_name
            AND tc.table_schema = kcu.table_schema
        JOIN information_schema.constraint_column_usage ccu
            ON ccu.constraint_name = tc.constraint_name
            AND ccu.table_schema = tc.constraint_schema
        WHERE tc.constraint_type = 'FOREIGN KEY'
            AND tc.table_schema IN {schemas_in}
    """)
    fks_result = await db.execute(fks_q)
    fks_raw = fks_result.mappings().all()

    idx_q = text(f"""
        SELECT
            schemaname,
            tablename,
            indexname,
            indexdef
        FROM pg_indexes
        WHERE schemaname IN {schemas_in}
        ORDER BY schemaname, tablename, indexname
    """)
    idx_result = await db.execute(idx_q)
    idx_raw = idx_result.mappings().all()

    # Build lookup maps
    col_map: dict[tuple[str, str], list[ColumnInfo]] = {}
    for c in cols_raw:
        key = (c["table_schema"], c["table_name"])
        dtype = c["udt_name"] if c["data_type"] == "USER-DEFINED" else c["data_type"]
        col_map.setdefault(key, []).append(ColumnInfo(
            name=c["column_name"],
            data_type=dtype,
            is_nullable=c["is_nullable"] == "YES",
            column_default=c["column_default"],
            is_primary_key=c["is_primary_key"],
            max_length=c["character_maximum_length"],
        ))

    fk_map: dict[tuple[str, str], list[ForeignKeyInfo]] = {}
    for f in fks_raw:
        key = (f["table_schema"], f["table_name"])
        fk_map.setdefault(key, []).append(ForeignKeyInfo(
            column=f["column_name"],
            references_schema=f["ref_schema"],
            references_table=f["ref_table"],
            references_column=f["ref_column"],
        ))

    idx_map: dict[tuple[str, str], list[IndexInfo]] = {}
    for ix in idx_raw:
        key = (ix["schemaname"], ix["tablename"])
        is_unique = "UNIQUE" in (ix["indexdef"] or "").upper()
        col_match = re.search(r"\((.+?)\)", ix["indexdef"] or "")
        cols_list = [c.strip().strip('"') for c in col_match.group(1).split(",")] if col_match else []
        idx_map.setdefault(key, []).append(IndexInfo(
            name=ix["indexname"],
            columns=cols_list,
            is_unique=is_unique,
        ))

    tables = []
    for t in tables_raw:
        key = (t["schema_name"], t["table_name"])
        tables.append(TableInfo(
            schema=t["schema_name"],
            table_name=t["table_name"],
            estimated_rows=t["estimated_rows"],
            columns=col_map.get(key, []),
            foreign_keys=fk_map.get(key, []),
            indexes=idx_map.get(key, []),
        ))

    return TablesResponse(tables=tables, total=len(tables))


# ---------------------------------------------------------------------------
# GET /admin/db/tables/{schema}/{table}/data — paginated row data
# ---------------------------------------------------------------------------

_VALID_SCHEMA = re.compile(r"^[a-z_][a-z0-9_]*$")
_VALID_TABLE = re.compile(r"^[a-z_][a-z0-9_]*$")
_VALID_COLUMN = re.compile(r"^[a-z_][a-z0-9_]*$")


@router.get("/tables/{schema}/{table}/data", response_model=DataResponse)
async def get_table_data(
    schema: str,
    table: str,
    page: int = Query(1, ge=1),
    page_size: int = Query(25, ge=1, le=100),
    order_by: Optional[str] = Query(None),
    order_dir: str = Query("asc", regex="^(asc|desc)$"),
    db: AsyncSession = Depends(get_db),
    _admin=Depends(require_admin),
):
    """Fetch paginated rows from a specific table."""
    if not _VALID_SCHEMA.match(schema) or not _VALID_TABLE.match(table):
        raise HTTPException(status_code=400, detail="Invalid schema or table name")

    check = await db.execute(text(
        "SELECT 1 FROM information_schema.tables "
        "WHERE table_schema = :s AND table_name = :t"
    ), {"s": schema, "t": table})
    if not check.scalar():
        raise HTTPException(status_code=404, detail=f"Table {schema}.{table} not found")

    count_result = await db.execute(text(f'SELECT COUNT(*) FROM "{schema}"."{table}"'))
    total = count_result.scalar() or 0

    order_clause = ""
    if order_by and _VALID_COLUMN.match(order_by):
        direction = "DESC" if order_dir == "desc" else "ASC"
        order_clause = f'ORDER BY "{order_by}" {direction} NULLS LAST'

    offset = (page - 1) * page_size
    data_result = await db.execute(text(
        f'SELECT * FROM "{schema}"."{table}" {order_clause} LIMIT :lim OFFSET :off'
    ), {"lim": page_size, "off": offset})

    columns = list(data_result.keys())
    rows = [
        {col: _safe_value(row[i]) for i, col in enumerate(columns)}
        for row in data_result.fetchall()
    ]

    return DataResponse(
        columns=columns,
        rows=rows,
        total_count=total,
        page=page,
        page_size=page_size,
        has_more=(offset + page_size) < total,
    )


# ---------------------------------------------------------------------------
# POST /admin/db/query — read-only SQL runner
# ---------------------------------------------------------------------------

@router.post("/query", response_model=QueryResponse)
async def run_query(
    body: QueryRequest,
    db: AsyncSession = Depends(get_db),
    _admin=Depends(require_admin),
):
    """Execute a read-only SQL query and return the results."""
    _validate_readonly_sql(body.sql)

    max_rows = 1000
    start = time.monotonic()

    try:
        await db.execute(text("SET LOCAL statement_timeout = '10s'"))
        result = await db.execute(text(body.sql))
        elapsed_ms = round((time.monotonic() - start) * 1000, 2)

        if result.returns_rows:
            columns = list(result.keys())
            all_rows = result.fetchall()
            truncated = len(all_rows) > max_rows
            rows = [
                {col: _safe_value(row[i]) for i, col in enumerate(columns)}
                for row in all_rows[:max_rows]
            ]
            return QueryResponse(
                columns=columns,
                rows=rows,
                row_count=len(all_rows),
                execution_ms=elapsed_ms,
                truncated=truncated,
            )
        else:
            return QueryResponse(
                columns=[],
                rows=[],
                row_count=0,
                execution_ms=elapsed_ms,
            )
    except Exception as e:
        elapsed_ms = round((time.monotonic() - start) * 1000, 2)
        err_msg = str(e).split("\n")[0]
        raise HTTPException(status_code=400, detail=f"Query error ({elapsed_ms}ms): {err_msg}")
