/**
 * Portable Database Viewer — PostgreSQL schema browser, data grid, and SQL runner.
 *
 * Three panes:
 *   1. Table list (left) — grouped by schema, search-filterable
 *   2. Schema + data grid (main) — column metadata and paginated rows
 *   3. SQL runner (toggle) — textarea with results grid
 *
 * INTEGRATION NOTES:
 *   - Requires: react, @tanstack/react-query, lucide-react, clsx, axios
 *   - Uses Tailwind CSS for styling (dark theme)
 *   - Import paths assume the directory structure in this bundle
 *   - See README.md for full integration instructions
 */
import { useState, useMemo, useCallback, useRef, useEffect } from 'react'
import {
  Database,
  Table2,
  Search,
  ChevronRight,
  ChevronDown,
  Key,
  Link2,
  Hash,
  ArrowUpDown,
  ArrowUp,
  ArrowDown,
  Play,
  Copy,
  Check,
  AlertTriangle,
  Loader2,
  Terminal,
  X,
  Columns3,
} from 'lucide-react'
import clsx from 'clsx'
import { useDbTables, useDbTableData, useDbQuery } from '../hooks/useAdminDb'
import type { DbTableInfo, DbColumnInfo, DbForeignKeyInfo, DbQueryResponse } from '../types'

// ---------------------------------------------------------------------------
// Cell renderer
// ---------------------------------------------------------------------------

function CellValue({ value, colName }: { value: unknown; colName: string }) {
  const [expanded, setExpanded] = useState(false)

  if (value === null || value === undefined) {
    return <span className="text-gray-600 italic text-xs">NULL</span>
  }

  if (typeof value === 'boolean') {
    return value
      ? <span className="text-green-400 font-medium">true</span>
      : <span className="text-red-400 font-medium">false</span>
  }

  const str = typeof value === 'object' ? JSON.stringify(value) : String(value)

  if (/^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i.test(str)) {
    return (
      <span className="font-mono text-xs text-blue-300 cursor-pointer group" title={str}
        onClick={() => navigator.clipboard.writeText(str)}>
        {str.slice(0, 8)}...
        <Copy className="inline h-3 w-3 ml-1 opacity-0 group-hover:opacity-60 transition-opacity" />
      </span>
    )
  }

  if (/^\d{4}-\d{2}-\d{2}T/.test(str)) {
    const d = new Date(str)
    const relative = formatRelative(d)
    return <span className="text-gray-300 text-xs" title={str}>{relative}</span>
  }

  if (typeof value === 'object') {
    const preview = str.length > 80 ? str.slice(0, 80) + '...' : str
    return (
      <div>
        <button onClick={() => setExpanded(!expanded)}
          className="text-xs text-amber-300/80 hover:text-amber-200 font-mono text-left max-w-[300px] truncate">
          {expanded ? '' : preview}
        </button>
        {expanded && (
          <pre className="mt-1 p-2 bg-gray-900 rounded text-xs text-gray-300 overflow-auto max-h-48 max-w-[400px] whitespace-pre-wrap">
            {JSON.stringify(value, null, 2)}
          </pre>
        )}
      </div>
    )
  }

  if (str.length > 120) {
    return (
      <div>
        <span className="text-gray-300 text-xs">
          {expanded ? str : str.slice(0, 120) + '...'}
        </span>
        <button onClick={() => setExpanded(!expanded)}
          className="ml-1 text-xs text-blue-400 hover:text-blue-300">
          {expanded ? 'less' : 'more'}
        </button>
      </div>
    )
  }

  return <span className="text-gray-300 text-xs">{str}</span>
}

function formatRelative(d: Date): string {
  const now = Date.now()
  const diff = now - d.getTime()
  const mins = Math.floor(diff / 60_000)
  if (mins < 1) return 'just now'
  if (mins < 60) return `${mins}m ago`
  const hrs = Math.floor(diff / 3_600_000)
  if (hrs < 24) return `${hrs}h ago`
  const days = Math.floor(diff / 86_400_000)
  if (days < 7) return `${days}d ago`
  return d.toLocaleDateString()
}

// ---------------------------------------------------------------------------
// Table list (sidebar)
// ---------------------------------------------------------------------------

interface TableListProps {
  tables: DbTableInfo[]
  selected: { schema: string; table: string } | null
  onSelect: (schema: string, table: string) => void
  isLoading: boolean
}

function TableList({ tables, selected, onSelect, isLoading }: TableListProps) {
  const [filter, setFilter] = useState('')
  const [collapsed, setCollapsed] = useState<Record<string, boolean>>({})

  const grouped = useMemo(() => {
    const map: Record<string, DbTableInfo[]> = {}
    for (const t of tables) {
      if (filter && !t.table_name.toLowerCase().includes(filter.toLowerCase())) continue
      ;(map[t.schema] ??= []).push(t)
    }
    return map
  }, [tables, filter])

  const schemas = Object.keys(grouped).sort()

  return (
    <div className="flex flex-col h-full">
      <div className="p-2 border-b border-gray-700">
        <div className="relative">
          <Search className="absolute left-2 top-1/2 -translate-y-1/2 h-3.5 w-3.5 text-gray-500" />
          <input
            type="text"
            value={filter}
            onChange={(e) => setFilter(e.target.value)}
            placeholder="Filter tables..."
            className="w-full bg-gray-800 border border-gray-700 rounded pl-7 pr-2 py-1.5 text-xs text-gray-300 placeholder-gray-500 focus:outline-none focus:border-blue-500"
          />
        </div>
      </div>

      <div className="flex-1 overflow-y-auto py-1">
        {isLoading ? (
          <div className="flex items-center justify-center p-4 text-gray-500">
            <Loader2 className="h-4 w-4 animate-spin mr-2" />
            <span className="text-xs">Loading tables...</span>
          </div>
        ) : schemas.length === 0 ? (
          <div className="p-4 text-center text-gray-500 text-xs">No tables found</div>
        ) : (
          schemas.map((schema) => (
            <div key={schema}>
              <button
                onClick={() => setCollapsed((p) => ({ ...p, [schema]: !p[schema] }))}
                className="w-full flex items-center px-2 py-1.5 text-xs font-semibold text-gray-400 hover:text-gray-200 uppercase tracking-wider"
              >
                {collapsed[schema] ? <ChevronRight className="h-3 w-3 mr-1" /> : <ChevronDown className="h-3 w-3 mr-1" />}
                <Database className="h-3 w-3 mr-1.5 text-blue-400" />
                {schema}
                <span className="ml-auto text-gray-600 font-normal normal-case">{grouped[schema].length}</span>
              </button>

              {!collapsed[schema] && grouped[schema].map((t) => {
                const isActive = selected?.schema === t.schema && selected?.table === t.table_name
                return (
                  <button
                    key={`${t.schema}.${t.table_name}`}
                    onClick={() => onSelect(t.schema, t.table_name)}
                    className={clsx(
                      'w-full flex items-center px-3 pl-7 py-1.5 text-xs transition-colors',
                      isActive ? 'bg-blue-600/20 text-blue-300' : 'text-gray-400 hover:bg-gray-800 hover:text-gray-200'
                    )}
                  >
                    <Table2 className="h-3 w-3 mr-1.5 shrink-0" />
                    <span className="truncate">{t.table_name}</span>
                    <span className="ml-auto text-gray-600 text-[10px] tabular-nums">{t.estimated_rows.toLocaleString()}</span>
                  </button>
                )
              })}
            </div>
          ))
        )}
      </div>
    </div>
  )
}

// ---------------------------------------------------------------------------
// Schema detail panel
// ---------------------------------------------------------------------------

function SchemaDetail({ table, onNavigate }: { table: DbTableInfo; onNavigate: (schema: string, table: string) => void }) {
  const [showIndexes, setShowIndexes] = useState(false)

  const fkMap = useMemo(() => {
    const m: Record<string, DbForeignKeyInfo> = {}
    for (const fk of table.foreign_keys) m[fk.column] = fk
    return m
  }, [table.foreign_keys])

  return (
    <div className="border border-gray-700 rounded-lg overflow-hidden">
      <div className="bg-gray-800/50 px-3 py-2 flex items-center justify-between">
        <div className="flex items-center space-x-2">
          <Columns3 className="h-4 w-4 text-blue-400" />
          <span className="text-sm font-medium text-white">{table.schema}.{table.table_name}</span>
          <span className="text-xs text-gray-500">({table.columns.length} columns)</span>
        </div>
        <span className="text-xs text-gray-500">~{table.estimated_rows.toLocaleString()} rows</span>
      </div>

      <table className="w-full text-xs">
        <thead className="bg-gray-800/80">
          <tr className="text-gray-400">
            <th className="px-3 py-1.5 text-left font-medium w-6"></th>
            <th className="px-3 py-1.5 text-left font-medium">Column</th>
            <th className="px-3 py-1.5 text-left font-medium">Type</th>
            <th className="px-3 py-1.5 text-left font-medium">Nullable</th>
            <th className="px-3 py-1.5 text-left font-medium">Default</th>
            <th className="px-3 py-1.5 text-left font-medium">FK</th>
          </tr>
        </thead>
        <tbody>
          {table.columns.map((col) => {
            const fk = fkMap[col.name]
            return (
              <tr key={col.name} className="border-t border-gray-800 hover:bg-gray-800/30">
                <td className="px-3 py-1.5">
                  {col.is_primary_key && <span title="Primary Key"><Key className="h-3 w-3 text-yellow-400" /></span>}
                  {fk && !col.is_primary_key && <span title="Foreign Key"><Link2 className="h-3 w-3 text-blue-400" /></span>}
                </td>
                <td className="px-3 py-1.5 font-mono text-gray-200">{col.name}</td>
                <td className="px-3 py-1.5 text-gray-400 font-mono">
                  {col.data_type}{col.max_length ? `(${col.max_length})` : ''}
                </td>
                <td className="px-3 py-1.5">
                  {col.is_nullable
                    ? <span className="text-gray-500">yes</span>
                    : <span className="text-orange-400 font-medium">NOT NULL</span>}
                </td>
                <td className="px-3 py-1.5 text-gray-500 font-mono max-w-[150px] truncate" title={col.column_default || ''}>
                  {col.column_default || '-'}
                </td>
                <td className="px-3 py-1.5">
                  {fk ? (
                    <button
                      onClick={() => onNavigate(fk.references_schema, fk.references_table)}
                      className="text-blue-400 hover:text-blue-300 hover:underline"
                    >
                      {fk.references_schema}.{fk.references_table}.{fk.references_column}
                    </button>
                  ) : '-'}
                </td>
              </tr>
            )
          })}
        </tbody>
      </table>

      {table.indexes.length > 0 && (
        <div className="border-t border-gray-700">
          <button
            onClick={() => setShowIndexes(!showIndexes)}
            className="w-full flex items-center px-3 py-1.5 text-xs text-gray-400 hover:text-gray-200"
          >
            {showIndexes ? <ChevronDown className="h-3 w-3 mr-1" /> : <ChevronRight className="h-3 w-3 mr-1" />}
            <Hash className="h-3 w-3 mr-1.5" />
            Indexes ({table.indexes.length})
          </button>
          {showIndexes && (
            <div className="px-3 pb-2 space-y-1">
              {table.indexes.map((idx) => (
                <div key={idx.name} className="flex items-center text-xs text-gray-500">
                  <span className={clsx('mr-2', idx.is_unique && 'text-yellow-500')}>
                    {idx.is_unique ? 'UNIQUE' : 'INDEX'}
                  </span>
                  <span className="font-mono text-gray-400">{idx.name}</span>
                  <span className="ml-2 text-gray-600">({idx.columns.join(', ')})</span>
                </div>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  )
}

// ---------------------------------------------------------------------------
// Data grid
// ---------------------------------------------------------------------------

interface DataGridProps {
  schema: string
  table: string
  columns: DbColumnInfo[]
}

function DataGrid({ schema, table, columns: schemaCols }: DataGridProps) {
  const [page, setPage] = useState(1)
  const [pageSize, setPageSize] = useState(25)
  const [orderBy, setOrderBy] = useState<string | undefined>()
  const [orderDir, setOrderDir] = useState<string>('asc')

  useEffect(() => { setPage(1); setOrderBy(undefined); setOrderDir('asc') }, [schema, table])

  const { data, isLoading, isFetching } = useDbTableData(schema, table, page, pageSize, orderBy, orderDir)

  const handleSort = useCallback((col: string) => {
    if (orderBy === col) {
      setOrderDir((d) => (d === 'asc' ? 'desc' : 'asc'))
    } else {
      setOrderBy(col)
      setOrderDir('asc')
    }
    setPage(1)
  }, [orderBy])

  if (!data && isLoading) {
    return (
      <div className="flex items-center justify-center p-8 text-gray-500">
        <Loader2 className="h-5 w-5 animate-spin mr-2" />
        Loading data...
      </div>
    )
  }

  if (!data) return null

  const totalPages = Math.ceil(data.total_count / pageSize)

  return (
    <div className="border border-gray-700 rounded-lg overflow-hidden">
      <div className="bg-gray-800/50 px-3 py-2 flex items-center justify-between text-xs">
        <div className="flex items-center space-x-3">
          <span className="text-gray-400">
            {data.total_count.toLocaleString()} rows
          </span>
          {isFetching && <Loader2 className="h-3 w-3 animate-spin text-blue-400" />}
        </div>
        <div className="flex items-center space-x-2">
          <span className="text-gray-500">Rows:</span>
          {[25, 50, 100].map((s) => (
            <button key={s} onClick={() => { setPageSize(s); setPage(1) }}
              className={clsx('px-2 py-0.5 rounded', s === pageSize ? 'bg-blue-600 text-white' : 'text-gray-400 hover:text-white')}>
              {s}
            </button>
          ))}
        </div>
      </div>

      <div className="overflow-x-auto">
        <table className="w-full text-xs">
          <thead className="bg-gray-800">
            <tr>
              {data.columns.map((col) => (
                <th key={col} className="px-3 py-2 text-left font-medium text-gray-400 whitespace-nowrap cursor-pointer hover:text-gray-200"
                  onClick={() => handleSort(col)}>
                  <div className="flex items-center space-x-1">
                    <span>{col}</span>
                    {orderBy === col ? (
                      orderDir === 'asc' ? <ArrowUp className="h-3 w-3 text-blue-400" /> : <ArrowDown className="h-3 w-3 text-blue-400" />
                    ) : (
                      <ArrowUpDown className="h-3 w-3 text-gray-600" />
                    )}
                  </div>
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {data.rows.length === 0 ? (
              <tr><td colSpan={data.columns.length} className="px-3 py-8 text-center text-gray-500">No data</td></tr>
            ) : (
              data.rows.map((row, i) => (
                <tr key={i} className="border-t border-gray-800/50 hover:bg-gray-800/30">
                  {data.columns.map((col) => (
                    <td key={col} className="px-3 py-1.5 max-w-[300px]">
                      <CellValue value={row[col]} colName={col} />
                    </td>
                  ))}
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>

      {totalPages > 1 && (
        <div className="bg-gray-800/50 px-3 py-2 flex items-center justify-between text-xs">
          <span className="text-gray-500">
            Page {page} of {totalPages}
          </span>
          <div className="flex items-center space-x-1">
            <button onClick={() => setPage(1)} disabled={page === 1}
              className="px-2 py-1 rounded bg-gray-700 text-gray-300 hover:bg-gray-600 disabled:opacity-30 disabled:cursor-not-allowed">
              First
            </button>
            <button onClick={() => setPage((p) => Math.max(1, p - 1))} disabled={page === 1}
              className="px-2 py-1 rounded bg-gray-700 text-gray-300 hover:bg-gray-600 disabled:opacity-30 disabled:cursor-not-allowed">
              Prev
            </button>
            <button onClick={() => setPage((p) => Math.min(totalPages, p + 1))} disabled={page === totalPages}
              className="px-2 py-1 rounded bg-gray-700 text-gray-300 hover:bg-gray-600 disabled:opacity-30 disabled:cursor-not-allowed">
              Next
            </button>
            <button onClick={() => setPage(totalPages)} disabled={page === totalPages}
              className="px-2 py-1 rounded bg-gray-700 text-gray-300 hover:bg-gray-600 disabled:opacity-30 disabled:cursor-not-allowed">
              Last
            </button>
          </div>
        </div>
      )}
    </div>
  )
}

// ---------------------------------------------------------------------------
// SQL Runner
// ---------------------------------------------------------------------------

function SqlRunner() {
  const [sql, setSql] = useState('')
  const [result, setResult] = useState<DbQueryResponse | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [copied, setCopied] = useState(false)
  const textareaRef = useRef<HTMLTextAreaElement>(null)
  const query = useDbQuery()

  const handleRun = useCallback(() => {
    if (!sql.trim()) return
    setError(null)
    query.mutate(sql, {
      onSuccess: (data) => { setResult(data); setError(null) },
      onError: (err: any) => {
        setResult(null)
        const detail = err?.response?.data?.detail || err?.message || 'Query failed'
        setError(detail)
      },
    })
  }, [sql, query])

  const handleKeyDown = useCallback((e: React.KeyboardEvent) => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
      e.preventDefault()
      handleRun()
    }
  }, [handleRun])

  const handleCopy = useCallback(() => {
    if (!result) return
    const header = result.columns.join('\t')
    const rows = result.rows.map((r) => result.columns.map((c) => {
      const v = r[c]
      return v === null ? '' : typeof v === 'object' ? JSON.stringify(v) : String(v)
    }).join('\t'))
    navigator.clipboard.writeText([header, ...rows].join('\n'))
    setCopied(true)
    setTimeout(() => setCopied(false), 2000)
  }, [result])

  return (
    <div className="space-y-3">
      <div className="border border-gray-700 rounded-lg overflow-hidden">
        <div className="bg-gray-800/50 px-3 py-2 flex items-center justify-between">
          <div className="flex items-center space-x-2">
            <Terminal className="h-4 w-4 text-green-400" />
            <span className="text-sm font-medium text-white">SQL Runner</span>
            <span className="text-xs text-gray-500">SELECT only | 10s timeout | 1000 row limit</span>
          </div>
          <div className="flex items-center space-x-2">
            {result && (
              <button onClick={handleCopy}
                className="flex items-center space-x-1 px-2 py-1 text-xs bg-gray-700 hover:bg-gray-600 rounded text-gray-300">
                {copied ? <Check className="h-3 w-3 text-green-400" /> : <Copy className="h-3 w-3" />}
                <span>{copied ? 'Copied' : 'Copy TSV'}</span>
              </button>
            )}
            <button onClick={handleRun} disabled={query.isPending || !sql.trim()}
              className="flex items-center space-x-1 px-3 py-1 text-xs bg-green-600 hover:bg-green-700 disabled:opacity-40 rounded text-white font-medium">
              {query.isPending ? <Loader2 className="h-3 w-3 animate-spin" /> : <Play className="h-3 w-3" />}
              <span>Run</span>
              <span className="text-green-300 text-[10px]">Ctrl+Enter</span>
            </button>
          </div>
        </div>

        <textarea
          ref={textareaRef}
          value={sql}
          onChange={(e) => setSql(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="SELECT * FROM public.users LIMIT 10;"
          className="w-full bg-gray-900 text-gray-200 font-mono text-xs p-3 min-h-[100px] resize-y focus:outline-none placeholder-gray-600"
          spellCheck={false}
        />
      </div>

      {error && (
        <div className="flex items-start space-x-2 p-3 bg-red-900/20 border border-red-800/50 rounded-lg">
          <AlertTriangle className="h-4 w-4 text-red-400 shrink-0 mt-0.5" />
          <pre className="text-xs text-red-300 whitespace-pre-wrap">{error}</pre>
        </div>
      )}

      {result && (
        <div className="border border-gray-700 rounded-lg overflow-hidden">
          <div className="bg-gray-800/50 px-3 py-2 flex items-center justify-between text-xs">
            <span className="text-gray-400">
              {result.row_count} row{result.row_count !== 1 ? 's' : ''} returned
              {result.truncated && <span className="text-amber-400 ml-1">(truncated to 1000)</span>}
            </span>
            <span className="text-gray-500">{result.execution_ms}ms</span>
          </div>

          {result.columns.length > 0 && (
            <div className="overflow-x-auto max-h-[400px] overflow-y-auto">
              <table className="w-full text-xs">
                <thead className="bg-gray-800 sticky top-0">
                  <tr>
                    {result.columns.map((col) => (
                      <th key={col} className="px-3 py-2 text-left font-medium text-gray-400 whitespace-nowrap">{col}</th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {result.rows.map((row, i) => (
                    <tr key={i} className="border-t border-gray-800/50 hover:bg-gray-800/30">
                      {result.columns.map((col) => (
                        <td key={col} className="px-3 py-1.5 max-w-[300px]">
                          <CellValue value={row[col]} colName={col} />
                        </td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      )}
    </div>
  )
}

// ---------------------------------------------------------------------------
// Main DatabaseViewer
// ---------------------------------------------------------------------------

type ViewMode = 'browse' | 'query'

export default function DatabaseViewer() {
  const { data: tablesData, isLoading } = useDbTables()
  const [selected, setSelected] = useState<{ schema: string; table: string } | null>(null)
  const [viewMode, setViewMode] = useState<ViewMode>('browse')

  const tables = tablesData?.tables ?? []

  const selectedTable = useMemo(() => {
    if (!selected) return null
    return tables.find((t) => t.schema === selected.schema && t.table_name === selected.table) ?? null
  }, [tables, selected])

  const handleNavigate = useCallback((schema: string, table: string) => {
    setSelected({ schema, table })
    setViewMode('browse')
  }, [])

  return (
    <div className="flex h-[calc(100vh-280px)] min-h-[500px] gap-4">
      {/* Left: Table list */}
      <div className="w-64 shrink-0 bg-gray-800/30 border border-gray-700 rounded-lg overflow-hidden">
        <div className="p-2 border-b border-gray-700 flex items-center justify-between">
          <div className="flex items-center space-x-1.5">
            <Database className="h-4 w-4 text-blue-400" />
            <span className="text-xs font-semibold text-gray-300">Tables</span>
            <span className="text-[10px] text-gray-500">({tables.length})</span>
          </div>
        </div>
        <TableList
          tables={tables}
          selected={selected}
          onSelect={(s, t) => setSelected({ schema: s, table: t })}
          isLoading={isLoading}
        />
      </div>

      {/* Right: Main content */}
      <div className="flex-1 flex flex-col min-w-0 space-y-3">
        {/* Mode toggle */}
        <div className="flex items-center space-x-2">
          <button onClick={() => setViewMode('browse')}
            className={clsx('flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-medium transition-colors',
              viewMode === 'browse' ? 'bg-blue-600/20 text-blue-300 border border-blue-500/30' : 'text-gray-400 hover:text-white border border-transparent')}>
            <Table2 className="h-3.5 w-3.5" />
            <span>Browse</span>
          </button>
          <button onClick={() => setViewMode('query')}
            className={clsx('flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-medium transition-colors',
              viewMode === 'query' ? 'bg-green-600/20 text-green-300 border border-green-500/30' : 'text-gray-400 hover:text-white border border-transparent')}>
            <Terminal className="h-3.5 w-3.5" />
            <span>SQL Runner</span>
          </button>
          {selected && viewMode === 'browse' && (
            <div className="ml-auto flex items-center space-x-1.5 text-xs text-gray-500">
              <span className="text-gray-600">{selected.schema}.</span>
              <span className="text-gray-300 font-medium">{selected.table}</span>
              <button onClick={() => setSelected(null)} className="text-gray-600 hover:text-gray-400">
                <X className="h-3 w-3" />
              </button>
            </div>
          )}
        </div>

        {/* Content */}
        <div className="flex-1 overflow-y-auto space-y-3">
          {viewMode === 'query' ? (
            <SqlRunner />
          ) : selected && selectedTable ? (
            <>
              <SchemaDetail table={selectedTable} onNavigate={handleNavigate} />
              <DataGrid schema={selected.schema} table={selected.table} columns={selectedTable.columns} />
            </>
          ) : (
            <div className="flex flex-col items-center justify-center h-full text-gray-500">
              <Database className="h-12 w-12 mb-3 text-gray-700" />
              <p className="text-sm">Select a table to browse its schema and data</p>
              <p className="text-xs text-gray-600 mt-1">or switch to SQL Runner for custom queries</p>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
