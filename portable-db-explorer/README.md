# Portable PostgreSQL Database Explorer

A complete, self-contained database explorer with schema browser, paginated data viewer, and read-only SQL runner. Built with **FastAPI** (backend) and **React + TypeScript** (frontend), styled with **Tailwind CSS** (dark theme).

![Architecture: FastAPI + React + PostgreSQL]

## Features

- **Schema browser**: Table list grouped by schema, searchable, with column metadata, foreign keys, indexes
- **Data viewer**: Paginated, sortable data grid with smart cell rendering (UUIDs, JSON, dates, booleans)
- **SQL runner**: Execute read-only SELECT queries with Ctrl+Enter, 10s timeout, 1000-row limit
- **FK navigation**: Click foreign key references to jump to referenced tables
- **Copy support**: Click UUIDs to copy, export SQL results as TSV
- **Security**: Regex-based SQL injection prevention, admin-only access, statement timeouts

## Directory Structure

```
portable-db-explorer/
├── README.md                          # This file
├── backend/
│   └── admin_db.py                    # FastAPI router (self-contained)
└── frontend/
    ├── components/
    │   └── DatabaseViewer.tsx          # Main UI component (all sub-components included)
    ├── hooks/
    │   └── useAdminDb.ts              # React Query hooks
    ├── services/
    │   └── dbApi.ts                   # Axios API client
    └── types/
        └── index.ts                   # TypeScript interfaces
```

## Prerequisites

### Backend (Python)
- Python 3.10+
- FastAPI
- SQLAlchemy (async) with asyncpg
- Pydantic v2
- PostgreSQL database

### Frontend (Node.js)
- React 18+
- TypeScript
- `@tanstack/react-query` v5+
- `axios`
- `lucide-react`
- `clsx`
- Tailwind CSS v3+ (dark theme configured)

---

## Integration Guide

### Step 1: Install Frontend Dependencies

If your project doesn't already have these:

```bash
npm install @tanstack/react-query axios lucide-react clsx
```

Ensure Tailwind CSS is configured with dark mode support.

### Step 2: Copy Files Into Your Project

Copy the files into your project structure. Adjust paths to match your conventions:

```
your-project/
├── backend/
│   └── app/
│       └── api/
│           └── admin_db.py          # Copy from backend/admin_db.py
└── frontend/
    └── src/
        ├── components/
        │   └── admin/
        │       └── DatabaseViewer.tsx  # Copy from frontend/components/
        ├── hooks/
        │   └── useAdminDb.ts          # Copy from frontend/hooks/
        ├── services/
        │   └── dbApi.ts               # Copy from frontend/services/
        └── types/
            └── db-explorer.ts         # Copy from frontend/types/
```

### Step 3: Configure the Backend

Open `backend/admin_db.py` and make these changes:

#### 3a. Replace `get_db` dependency

Replace the placeholder with your project's database session dependency:

```python
# BEFORE (placeholder):
async def get_db():
    raise NotImplementedError(...)

# AFTER (your project's dependency):
from app.core.database import get_db  # Your actual import
```

Your `get_db` must yield a `sqlalchemy.ext.asyncio.AsyncSession`.

#### 3b. Replace `require_admin` dependency

Replace with your project's authentication/authorization check:

```python
# BEFORE (placeholder):
async def require_admin():
    raise NotImplementedError(...)

# AFTER — Example with JWT auth:
from app.core.auth import get_current_user
from app.models.user import User

async def require_admin(user: User = Depends(get_current_user)):
    if user.role not in ("admin", "owner"):
        raise HTTPException(status_code=403, detail="Admin privileges required")
    return user
```

Or if you don't need auth (dev-only tool):

```python
async def require_admin():
    pass  # No auth check — ONLY use in development!
```

#### 3c. Configure allowed schemas

Edit `ALLOWED_SCHEMAS` to expose the schemas you want:

```python
# Default — only public schema:
ALLOWED_SCHEMAS = ("public",)

# Multiple schemas:
ALLOWED_SCHEMAS = ("public", "auth", "app")
```

#### 3d. Register the router

In your FastAPI app setup (e.g., `main.py` or `api/__init__.py`):

```python
from app.api.admin_db import router as admin_db_router

app.include_router(admin_db_router, prefix="/api")
# Endpoints will be at: /api/admin/db/tables, /api/admin/db/query, etc.
```

### Step 4: Configure the Frontend

#### 4a. Update API base URL

Open `frontend/services/dbApi.ts` and configure the axios instance:

**Option A — Use your existing axios instance:**

```typescript
// Replace the standalone axios.create() with your project's configured instance:
import { api } from '@/services/api'  // Your existing configured axios
```

**Option B — Configure the standalone instance:**

```typescript
const api = axios.create({
  baseURL: 'http://localhost:8000/api',  // Your backend URL
  headers: { 'Content-Type': 'application/json' },
})

// Add auth interceptor if needed:
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})
```

#### 4b. Fix import paths

Update import paths in each file to match your project structure:

In `DatabaseViewer.tsx`:
```typescript
// Adjust these imports to your project's path conventions:
import { useDbTables, useDbTableData, useDbQuery } from '../../hooks/useAdminDb'
import type { DbTableInfo, DbColumnInfo, DbForeignKeyInfo, DbQueryResponse } from '../../types'
```

In `useAdminDb.ts`:
```typescript
import { dbApi } from '../services/dbApi'  // Adjust path
```

#### 4c. Ensure React Query Provider exists

Your app must have a `QueryClientProvider` wrapping the component tree:

```tsx
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'

const queryClient = new QueryClient()

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      {/* Your app content */}
    </QueryClientProvider>
  )
}
```

### Step 5: Mount the Component

Import and render the `DatabaseViewer` wherever you want it:

```tsx
import DatabaseViewer from '@/components/admin/DatabaseViewer'

// As a full page:
function DatabasePage() {
  return (
    <div className="p-4 bg-gray-900 min-h-screen">
      <h1 className="text-xl font-bold text-white mb-4">Database Explorer</h1>
      <DatabaseViewer />
    </div>
  )
}

// Or lazy-loaded in a tab:
const DatabaseViewer = React.lazy(() => import('@/components/admin/DatabaseViewer'))

function AdminPage() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <DatabaseViewer />
    </Suspense>
  )
}
```

### Step 6: Adjust Height (Optional)

The component uses `h-[calc(100vh-280px)]` by default. Adjust this in `DatabaseViewer.tsx` to fit your layout:

```tsx
// In the main component's return, find this div:
<div className="flex h-[calc(100vh-280px)] min-h-[500px] gap-4">

// Change to fit your page layout, e.g.:
<div className="flex h-[calc(100vh-64px)] min-h-[500px] gap-4">  // 64px header
<div className="flex h-full min-h-[500px] gap-4">                // Fill parent
```

---

## API Endpoints Reference

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/admin/db/tables` | List all tables with columns, FKs, indexes, row counts |
| `GET` | `/admin/db/tables/{schema}/{table}/data` | Paginated rows (query params: `page`, `page_size`, `order_by`, `order_dir`) |
| `POST` | `/admin/db/query` | Execute read-only SQL (body: `{ "sql": "SELECT ..." }`) |

### Response Types

**TablesResponse**: `{ tables: TableInfo[], total: number }`
**DataResponse**: `{ columns: string[], rows: object[], total_count, page, page_size, has_more }`
**QueryResponse**: `{ columns: string[], rows: object[], row_count, execution_ms, truncated }`

---

## Security Notes

1. **Admin-only**: All endpoints require admin authentication (you implement the check)
2. **Read-only SQL**: Regex rejects INSERT, UPDATE, DELETE, DROP, ALTER, TRUNCATE, CREATE, GRANT, REVOKE
3. **Query timeout**: 10-second PostgreSQL `statement_timeout` prevents runaway queries
4. **Row limit**: SQL runner caps results at 1000 rows
5. **Input validation**: Schema/table/column names validated against `^[a-z_][a-z0-9_]*$`
6. **No raw string interpolation**: Table/schema names are validated before use in queries

### Production Considerations

- Consider adding rate limiting to the SQL runner endpoint
- Consider adding query logging/auditing
- The SQL regex validation is a defense-in-depth layer, not a SQL parser — use a DB user with SELECT-only permissions for maximum safety
- Consider disabling in production or restricting to specific IP ranges

---

## Customization

### Theming

The UI uses Tailwind CSS utility classes with a dark theme (gray-800/900 backgrounds). To adapt to your theme:

- Search for `bg-gray-` classes and replace with your color scheme
- Search for `text-gray-` classes for text colors
- The component uses `blue-400/500/600` for primary accents, `green-400/600` for success, `red-400` for errors

### Adding Features

Common extensions:

- **Table row count refresh**: Add a refresh button that calls `ANALYZE` on a table
- **Export to CSV**: Extend the Copy TSV button to generate proper CSV
- **Saved queries**: Add localStorage-based query history
- **Table DDL view**: Add an endpoint that returns `pg_dump --schema-only` output
- **Column search within data**: Add a filter row above the data grid

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "Admin privileges required" | Your `require_admin` dependency is rejecting the user. Check auth setup. |
| Empty table list | Check `ALLOWED_SCHEMAS` matches your database schemas. Run `SELECT schema_name FROM information_schema.schemata;` to verify. |
| "Query must start with SELECT" | Only SELECT, WITH, and EXPLAIN queries are allowed. No mutations. |
| Timeout errors | Queries exceeding 10s are killed. Add WHERE clauses or LIMIT to narrow results. |
| CORS errors | Configure CORS on your FastAPI app: `app.add_middleware(CORSMiddleware, ...)` |
| Types don't match | Ensure `DbTablesResponse` in your types file matches the backend's `TablesResponse` Pydantic model |

---

## License

This component was extracted from a larger project. Use it however you like.
