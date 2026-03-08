/**
 * API client for the Database Viewer endpoints.
 *
 * INTEGRATION: You need to configure the axios instance to point to your
 * backend's base URL and include any auth headers your project requires.
 * See README.md for examples.
 */
import axios from 'axios'
import type { DbTablesResponse, DbDataResponse, DbQueryResponse } from '../types'

// 🔧 INTEGRATION POINT: Configure your axios instance
// Replace this with your project's configured axios instance that includes:
//   - baseURL pointing to your API
//   - Auth headers (Bearer token, cookies, etc.)
//   - Any interceptors you need
const api = axios.create({
  baseURL: '/api',  // Adjust to your API base URL
  headers: { 'Content-Type': 'application/json' },
})

// If you already have a configured axios instance, just import it:
// import { api } from './yourExistingApiModule'

const getData = <T>(res: { data: T }) => res.data

export const dbApi = {
  getTables: () =>
    api.get<DbTablesResponse>('/admin/db/tables').then(getData),

  getTableData: (schema: string, table: string, params?: {
    page?: number
    page_size?: number
    order_by?: string
    order_dir?: string
  }) =>
    api.get<DbDataResponse>(`/admin/db/tables/${schema}/${table}/data`, { params }).then(getData),

  runQuery: (sql: string) =>
    api.post<DbQueryResponse>('/admin/db/query', { sql }).then(getData),
}
