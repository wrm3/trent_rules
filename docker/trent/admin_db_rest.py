"""
admin_db_rest.py — Portable Database Explorer for trent

Starlette routes + psycopg2. No SQLAlchemy, no FastAPI required.

Routes (added to ADMIN_ROUTES list, merged into server.py's Starlette app):
  GET  /admin/db                           — Browser UI (self-contained HTML)
  GET  /admin/db/tables                    — Schema introspection JSON
  GET  /admin/db/tables/{schema}/{table}/data  — Paginated rows JSON
  POST /admin/db/query                     — Read-only SQL runner JSON
"""
import re
import time
import logging
import uuid as _uuid
from datetime import datetime as _dt, date as _date
from decimal import Decimal as _Dec
from typing import Optional

from starlette.requests import Request
from starlette.responses import JSONResponse, HTMLResponse
from starlette.routing import Route

logger = logging.getLogger(__name__)

ALLOWED_SCHEMAS = ("public",)
MAX_QUERY_ROWS = 1000
_VALID_IDENT = re.compile(r"^[a-z_][a-z0-9_]*$")
_DANGEROUS = re.compile(
    r"\b(INSERT|UPDATE|DELETE|DROP|ALTER|TRUNCATE|CREATE|GRANT|REVOKE|COPY|EXECUTE|CALL)\b",
    re.IGNORECASE,
)

_db = None


def init_admin_db(db) -> None:
    """Wire in the shared RAGDatabase instance from server.py."""
    global _db
    _db = db


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _validate_readonly(sql: str) -> Optional[str]:
    stripped = sql.strip().rstrip(";").strip()
    if not stripped:
        return "Empty query"
    if _DANGEROUS.search(stripped):
        return "Only SELECT queries are allowed"
    upper = stripped.upper()
    if not (upper.startswith("SELECT") or upper.startswith("WITH") or upper.startswith("EXPLAIN")):
        return "Query must start with SELECT, WITH, or EXPLAIN"
    return None


def _safe_val(v):
    """Serialize a psycopg2 value to a JSON-safe Python type."""
    if v is None:
        return None
    if isinstance(v, _uuid.UUID):
        return str(v)
    if isinstance(v, (_dt, _date)):
        return v.isoformat()
    if isinstance(v, _Dec):
        return float(v)
    if isinstance(v, (bytes, memoryview)):
        return bytes(v).hex()
    # pgvector returns a list-like — truncate for display
    if hasattr(v, "__iter__") and not isinstance(v, (str, dict, list)):
        try:
            lst = list(v)
            return f"[vector({len(lst)})]"
        except Exception:
            return str(v)
    return v


def _rows_to_json(rows_raw) -> list[dict]:
    return [{k: _safe_val(v) for k, v in row.items()} for row in rows_raw]


# ---------------------------------------------------------------------------
# Embedded single-page HTML UI (dark theme, vanilla JS, no build step)
# ---------------------------------------------------------------------------

_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>trent DB Explorer</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:monospace;background:#0f172a;color:#e2e8f0;font-size:13px;height:100vh;display:flex;flex-direction:column;overflow:hidden}
header{background:#1e293b;padding:10px 16px;display:flex;align-items:center;gap:14px;border-bottom:1px solid #334155;flex-shrink:0}
header h1{font-size:14px;color:#38bdf8;font-weight:600}
#st{font-size:11px;color:#64748b}
.main{display:flex;flex:1;overflow:hidden}
.sidebar{width:210px;background:#1e293b;border-right:1px solid #334155;overflow-y:auto;flex-shrink:0;display:flex;flex-direction:column}
.sidebar h2{font-size:10px;color:#475569;padding:9px 12px 5px;text-transform:uppercase;letter-spacing:.06em;flex-shrink:0}
.titem{padding:5px 12px;cursor:pointer;display:flex;justify-content:space-between;border-bottom:1px solid #0f172a;font-size:12px;align-items:center}
.titem:hover,.titem.active{background:#0f172a;color:#38bdf8}
.rc{font-size:10px;color:#475569}
.content{flex:1;display:flex;flex-direction:column;overflow:hidden}
.tabs{display:flex;background:#1e293b;border-bottom:1px solid #334155;flex-shrink:0}
.tab{padding:7px 16px;cursor:pointer;font-size:12px;color:#94a3b8;border-bottom:2px solid transparent;user-select:none}
.tab.active{color:#38bdf8;border-bottom-color:#38bdf8}
.panel{flex:1;overflow:auto;display:none;flex-direction:column}
.panel.active{display:flex}
table{width:100%;border-collapse:collapse;font-size:12px}
th{background:#1e293b;position:sticky;top:0;padding:5px 10px;text-align:left;color:#94a3b8;font-weight:500;white-space:nowrap;border-bottom:1px solid #334155;z-index:1}
td{padding:4px 10px;border-bottom:1px solid #1e293b;white-space:nowrap;max-width:260px;overflow:hidden;text-overflow:ellipsis;vertical-align:top}
tr:hover td{background:#1e293b}
.null{color:#334155;font-style:italic}.bt{color:#4ade80}.bf{color:#f87171}
.pg{display:flex;align-items:center;gap:8px;padding:6px 12px;background:#1e293b;border-top:1px solid #334155;font-size:11px;color:#64748b;flex-shrink:0}
.btn{background:#1e40af;color:#e2e8f0;border:none;padding:3px 10px;border-radius:3px;cursor:pointer;font-size:11px;font-family:monospace}
.btn:hover{background:#1d4ed8}.btn:disabled{opacity:.35;cursor:not-allowed}
.sc-row{display:grid;grid-template-columns:180px 1fr 90px;gap:0;border-bottom:1px solid #1e293b;padding:5px 10px;font-size:12px;align-items:center}
.sc-row:hover{background:#1e293b}
.badge{font-size:9px;border-radius:2px;padding:1px 4px;margin-left:4px;vertical-align:middle}
.pk{background:#78350f;color:#fde68a}.fk{background:#2e1065;color:#ddd6fe}.nullable{background:#0c4a6e;color:#7dd3fc}
.sql-pane{height:100%;display:flex;flex-direction:column}
.sql-bar{display:flex;gap:8px;padding:7px 12px;background:#1e293b;border-bottom:1px solid #334155;align-items:center;font-size:11px;color:#64748b;flex-shrink:0}
textarea{flex:0 0 100px;background:#0f172a;color:#e2e8f0;border:none;border-bottom:1px solid #334155;padding:8px 12px;font-family:monospace;font-size:12px;resize:none;outline:none;width:100%}
.qres{flex:1;overflow:auto}
.msg{padding:24px;color:#334155;text-align:center;font-size:12px}
.err{color:#f87171}
.sh{padding:4px 12px;font-size:10px;color:#475569;background:#1e293b;border-bottom:1px solid #334155;flex-shrink:0}
</style>
</head>
<body>
<header>
  <h1>⬡ trent DB Explorer</h1>
  <span id="st">connecting…</span>
  <span style="margin-left:auto;font-size:10px;color:#334155">read-only · SELECT only</span>
</header>
<div class="main">
  <div class="sidebar">
    <h2>Tables</h2>
    <div id="tlist" style="overflow-y:auto;flex:1"><div class="msg">…</div></div>
  </div>
  <div class="content">
    <div class="tabs">
      <div class="tab active" onclick="showTab('data')">Data</div>
      <div class="tab" onclick="showTab('schema')">Schema</div>
      <div class="tab" onclick="showTab('sql')">SQL Runner</div>
    </div>
    <div id="panel-data" class="panel active"><div class="msg">Select a table from the sidebar</div></div>
    <div id="panel-schema" class="panel"><div class="msg">Select a table from the sidebar</div></div>
    <div id="panel-sql" class="panel sql-pane">
      <div class="sql-bar">
        <button class="btn" onclick="runQ()">▶ Run (Ctrl+Enter)</button>
        <span id="qmeta"></span>
      </div>
      <textarea id="qbox" placeholder="Write a SELECT query…"
        onkeydown="if(event.ctrlKey&&event.key==='Enter'){event.preventDefault();runQ();}"></textarea>
      <div class="qres" id="qres"><div class="msg">Write a SELECT query above and press ▶ Run</div></div>
    </div>
  </div>
</div>
<script>
'use strict';
let tables=[],active=null,page=1;
async function api(path,opts){
  const r=await fetch(path,opts);
  if(!r.ok){const e=await r.json().catch(()=>({error:r.statusText}));throw new Error(e.error||r.statusText);}
  return r.json();
}
function showTab(n){
  document.querySelectorAll('.tab').forEach((t,i)=>t.classList.toggle('active',['data','schema','sql'][i]===n));
  document.querySelectorAll('.panel').forEach(p=>p.classList.toggle('active',p.id==='panel-'+n));
}
function fmt(v){
  if(v===null||v===undefined)return '<span class="null">NULL</span>';
  if(v===true)return '<span class="bt">true</span>';
  if(v===false)return '<span class="bf">false</span>';
  if(typeof v==='object')return JSON.stringify(v).slice(0,100);
  const s=String(v);return s.length>140?s.slice(0,140)+'…':s;
}
function grid(rows,cols){
  if(!rows.length)return '<div class="msg">No rows</div>';
  const ths=cols.map(c=>`<th>${c}</th>`).join('');
  const trs=rows.map(r=>'<tr>'+cols.map(c=>`<td>${fmt(r[c])}</td>`).join('')+'</tr>').join('');
  return `<table><thead><tr>${ths}</tr></thead><tbody>${trs}</tbody></table>`;
}
async function loadTables(){
  try{
    const d=await api('/admin/db/tables');
    tables=d.tables;
    document.getElementById('st').textContent=`${d.total} tables`;
    document.getElementById('tlist').innerHTML=d.tables.map(t=>
      `<div class="titem" id="ti-${t.table_name}" onclick="sel('${t.schema}','${t.table_name}')">
        <span>${t.table_name}</span><span class="rc">${t.estimated_rows.toLocaleString()}</span>
      </div>`).join('');
  }catch(e){document.getElementById('st').innerHTML=`<span class="err">${e.message}</span>`;}
}
async function sel(schema,tname){
  active={schema,tname};page=1;
  document.querySelectorAll('.titem').forEach(el=>el.classList.toggle('active',el.id==='ti-'+tname));
  // Update SQL Runner textarea to reflect selected table
  const qbox=document.getElementById('qbox');
  if(qbox&&!qbox.value.trim()){
    qbox.value=`SELECT * FROM ${tname} ORDER BY 1 DESC LIMIT 20`;
  } else if(qbox){
    qbox.value=`SELECT * FROM ${tname} ORDER BY 1 DESC LIMIT 20`;
  }
  loadData();loadSchema(schema,tname);
}
async function loadData(){
  if(!active)return;
  const pnl=document.getElementById('panel-data');
  pnl.innerHTML='<div class="msg">loading…</div>';
  try{
    const d=await api(`/admin/db/tables/${active.schema}/${active.tname}/data?page=${page}&page_size=50`);
    const nav=`<div class="pg">
      <button class="btn" onclick="pg(-1)" ${page===1?'disabled':''}>← Prev</button>
      <span>Page ${d.page} · ${d.total_count.toLocaleString()} rows total</span>
      <button class="btn" onclick="pg(1)" ${!d.has_more?'disabled':''}>Next →</button>
    </div>`;
    pnl.innerHTML=`<div style="flex:1;overflow:auto">${grid(d.rows,d.columns)}</div>${nav}`;
  }catch(e){pnl.innerHTML=`<div class="msg err">${e.message}</div>`;}
}
function pg(dir){page=Math.max(1,page+dir);loadData();}
function loadSchema(schema,tname){
  const t=tables.find(x=>x.schema===schema&&x.table_name===tname);
  if(!t)return;
  const cols=t.columns.map(c=>{
    const b=[
      c.is_primary_key?'<span class="badge pk">PK</span>':'',
      c.is_nullable?'<span class="badge nullable">NULL</span>':'',
    ].filter(Boolean).join('');
    return `<div class="sc-row"><span>${c.name}${b}</span><span style="color:#64748b">${c.data_type}</span></div>`;
  }).join('');
  const fks=t.foreign_keys.length?`<div class="sh" style="color:#a78bfa">FOREIGN KEYS</div>`+
    t.foreign_keys.map(f=>`<div class="sc-row"><span style="color:#a78bfa">${f.column}</span><span style="color:#475569;font-size:10px">→ ${f.references_table}.${f.references_column}</span></div>`).join(''):'';
  const ixs=t.indexes.length?`<div class="sh" style="color:#94a3b8">INDEXES</div>`+
    t.indexes.map(ix=>`<div class="sc-row"><span style="color:#94a3b8">${ix.name}</span><span style="color:#475569;font-size:10px">${ix.columns.join(', ')}${ix.is_unique?' · UNIQUE':''}</span></div>`).join(''):'';
  document.getElementById('panel-schema').innerHTML=
    `<div class="sh" style="color:#e2e8f0">${tname}</div>
     <div class="sh" style="color:#38bdf8">COLUMNS (${t.columns.length})</div>${cols}${fks}${ixs}`;
}
async function runQ(){
  const sql=document.getElementById('qbox').value.trim();if(!sql)return;
  const res=document.getElementById('qres'),meta=document.getElementById('qmeta');
  res.innerHTML='<div class="msg">running…</div>';meta.textContent='';
  try{
    const d=await api('/admin/db/query',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({sql})});
    meta.textContent=`${d.row_count} rows · ${d.execution_ms}ms${d.truncated?' (truncated at 1000)':''}`;
    res.innerHTML=grid(d.rows,d.columns);
  }catch(e){res.innerHTML=`<div class="msg err">${e.message}</div>`;}
}
loadTables();
</script>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Route handlers
# ---------------------------------------------------------------------------

async def handle_admin_ui(request: Request) -> HTMLResponse:
    return HTMLResponse(_HTML)


async def handle_list_tables(request: Request) -> JSONResponse:
    if not _db:
        return JSONResponse({"error": "Database not configured"}, status_code=503)
    schemas_in = "(" + ", ".join(f"'{s}'" for s in ALLOWED_SCHEMAS) + ")"
    try:
        with _db.get_cursor() as cur:
            cur.execute(f"""
                SELECT schemaname AS schema_name, relname AS table_name,
                       COALESCE(n_live_tup, 0) AS estimated_rows
                FROM pg_stat_user_tables WHERE schemaname IN {schemas_in}
                ORDER BY schemaname, relname
            """)
            tables_raw = cur.fetchall()

            cur.execute(f"""
                SELECT c.table_schema, c.table_name, c.column_name,
                       c.data_type, c.udt_name, c.is_nullable,
                       c.column_default, c.character_maximum_length,
                       CASE WHEN pk.column_name IS NOT NULL THEN true ELSE false END AS is_pk
                FROM information_schema.columns c
                LEFT JOIN (
                    SELECT kcu.table_schema, kcu.table_name, kcu.column_name
                    FROM information_schema.table_constraints tc
                    JOIN information_schema.key_column_usage kcu
                        ON tc.constraint_name=kcu.constraint_name
                        AND tc.table_schema=kcu.table_schema
                    WHERE tc.constraint_type='PRIMARY KEY'
                ) pk ON c.table_schema=pk.table_schema
                     AND c.table_name=pk.table_name
                     AND c.column_name=pk.column_name
                WHERE c.table_schema IN {schemas_in}
                ORDER BY c.table_schema, c.table_name, c.ordinal_position
            """)
            cols_raw = cur.fetchall()

            cur.execute(f"""
                SELECT tc.table_schema, tc.table_name, kcu.column_name,
                       ccu.table_schema AS ref_schema,
                       ccu.table_name   AS ref_table,
                       ccu.column_name  AS ref_column
                FROM information_schema.table_constraints tc
                JOIN information_schema.key_column_usage kcu
                    ON tc.constraint_name=kcu.constraint_name AND tc.table_schema=kcu.table_schema
                JOIN information_schema.constraint_column_usage ccu
                    ON ccu.constraint_name=tc.constraint_name AND ccu.table_schema=tc.constraint_schema
                WHERE tc.constraint_type='FOREIGN KEY' AND tc.table_schema IN {schemas_in}
            """)
            fks_raw = cur.fetchall()

            cur.execute(f"""
                SELECT schemaname, tablename, indexname, indexdef FROM pg_indexes
                WHERE schemaname IN {schemas_in} ORDER BY schemaname, tablename, indexname
            """)
            idx_raw = cur.fetchall()

        # Build lookup maps
        col_map: dict = {}
        for c in cols_raw:
            key = (c["table_schema"], c["table_name"])
            dtype = c["udt_name"] if c["data_type"] == "USER-DEFINED" else c["data_type"]
            col_map.setdefault(key, []).append({
                "name": c["column_name"],
                "data_type": dtype,
                "is_nullable": c["is_nullable"] == "YES",
                "column_default": c["column_default"],
                "is_primary_key": bool(c["is_pk"]),
                "max_length": c["character_maximum_length"],
            })

        fk_map: dict = {}
        for f in fks_raw:
            key = (f["table_schema"], f["table_name"])
            fk_map.setdefault(key, []).append({
                "column": f["column_name"],
                "references_schema": f["ref_schema"],
                "references_table": f["ref_table"],
                "references_column": f["ref_column"],
            })

        idx_map: dict = {}
        for ix in idx_raw:
            key = (ix["schemaname"], ix["tablename"])
            is_unique = "UNIQUE" in (ix["indexdef"] or "").upper()
            col_match = re.search(r"\((.+?)\)", ix["indexdef"] or "")
            cols_list = [c.strip().strip('"') for c in col_match.group(1).split(",")] if col_match else []
            idx_map.setdefault(key, []).append({
                "name": ix["indexname"], "columns": cols_list, "is_unique": is_unique,
            })

        tables = [
            {
                "schema": t["schema_name"],
                "table_name": t["table_name"],
                "estimated_rows": t["estimated_rows"],
                "columns": col_map.get((t["schema_name"], t["table_name"]), []),
                "foreign_keys": fk_map.get((t["schema_name"], t["table_name"]), []),
                "indexes": idx_map.get((t["schema_name"], t["table_name"]), []),
            }
            for t in tables_raw
        ]
        return JSONResponse({"tables": tables, "total": len(tables)})

    except Exception as e:
        logger.error("list_tables error: %s", e)
        return JSONResponse({"error": str(e)}, status_code=500)


async def handle_get_table_data(request: Request) -> JSONResponse:
    if not _db:
        return JSONResponse({"error": "Database not configured"}, status_code=503)

    schema = request.path_params["schema"]
    table = request.path_params["table"]
    if not (_VALID_IDENT.match(schema) and _VALID_IDENT.match(table)):
        return JSONResponse({"error": "Invalid schema or table name"}, status_code=400)

    page = max(1, int(request.query_params.get("page", 1)))
    page_size = min(max(1, int(request.query_params.get("page_size", 25))), 100)
    order_by = request.query_params.get("order_by")
    order_dir = request.query_params.get("order_dir", "asc")

    try:
        with _db.get_cursor() as cur:
            cur.execute(
                "SELECT 1 FROM information_schema.tables WHERE table_schema=%s AND table_name=%s",
                (schema, table),
            )
            if not cur.fetchone():
                return JSONResponse({"error": f"Table {schema}.{table} not found"}, status_code=404)

            cur.execute(f'SELECT COUNT(*) AS cnt FROM "{schema}"."{table}"')
            total = cur.fetchone()["cnt"]

            order_clause = ""
            if order_by and _VALID_IDENT.match(order_by):
                direction = "DESC" if order_dir == "desc" else "ASC"
                order_clause = f'ORDER BY "{order_by}" {direction} NULLS LAST'

            offset = (page - 1) * page_size
            cur.execute(
                f'SELECT * FROM "{schema}"."{table}" {order_clause} LIMIT %s OFFSET %s',
                (page_size, offset),
            )
            rows_raw = cur.fetchall()

        columns = list(rows_raw[0].keys()) if rows_raw else []
        rows = _rows_to_json(rows_raw)
        return JSONResponse({
            "columns": columns, "rows": rows, "total_count": total,
            "page": page, "page_size": page_size,
            "has_more": (offset + page_size) < total,
        })

    except Exception as e:
        logger.error("get_table_data error: %s", e)
        return JSONResponse({"error": str(e)}, status_code=500)


async def handle_query(request: Request) -> JSONResponse:
    if not _db:
        return JSONResponse({"error": "Database not configured"}, status_code=503)

    try:
        body = await request.json()
    except Exception:
        return JSONResponse({"error": "Invalid JSON body"}, status_code=400)

    sql = body.get("sql", "").strip()
    err = _validate_readonly(sql)
    if err:
        return JSONResponse({"error": err}, status_code=400)

    start = time.monotonic()
    try:
        with _db.get_cursor() as cur:
            cur.execute("SET LOCAL statement_timeout = '10s'")
            cur.execute(sql)
            rows_raw = cur.fetchall() or []

        elapsed_ms = round((time.monotonic() - start) * 1000, 2)
        columns = list(rows_raw[0].keys()) if rows_raw else []
        truncated = len(rows_raw) > MAX_QUERY_ROWS
        rows = _rows_to_json(rows_raw[:MAX_QUERY_ROWS])
        return JSONResponse({
            "columns": columns, "rows": rows,
            "row_count": len(rows_raw), "execution_ms": elapsed_ms, "truncated": truncated,
        })

    except Exception as e:
        elapsed_ms = round((time.monotonic() - start) * 1000, 2)
        first_line = str(e).split("\n")[0]
        return JSONResponse(
            {"error": f"Query error ({elapsed_ms}ms): {first_line}"},
            status_code=400,
        )


# ---------------------------------------------------------------------------
# Route list — imported by server.py
# ---------------------------------------------------------------------------
ADMIN_ROUTES = [
    Route("/admin/db",                                    handle_admin_ui,       methods=["GET"]),
    Route("/admin/db/tables",                             handle_list_tables,    methods=["GET"]),
    Route("/admin/db/tables/{schema}/{table}/data",       handle_get_table_data, methods=["GET"]),
    Route("/admin/db/query",                              handle_query,          methods=["POST"]),
]
