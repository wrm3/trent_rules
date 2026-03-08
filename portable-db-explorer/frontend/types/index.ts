/**
 * TypeScript types for the Database Viewer.
 * These match the Pydantic response schemas from the backend.
 */

export interface DbColumnInfo {
  name: string
  data_type: string
  is_nullable: boolean
  column_default?: string | null
  is_primary_key: boolean
  max_length?: number | null
}

export interface DbForeignKeyInfo {
  column: string
  references_schema: string
  references_table: string
  references_column: string
}

export interface DbIndexInfo {
  name: string
  columns: string[]
  is_unique: boolean
}

export interface DbTableInfo {
  schema: string
  table_name: string
  estimated_rows: number
  columns: DbColumnInfo[]
  foreign_keys: DbForeignKeyInfo[]
  indexes: DbIndexInfo[]
}

export interface DbTablesResponse {
  tables: DbTableInfo[]
  total: number
}

export interface DbDataResponse {
  columns: string[]
  rows: Record<string, unknown>[]
  total_count: number
  page: number
  page_size: number
  has_more: boolean
}

export interface DbQueryResponse {
  columns: string[]
  rows: Record<string, unknown>[]
  row_count: number
  execution_ms: number
  truncated: boolean
}
