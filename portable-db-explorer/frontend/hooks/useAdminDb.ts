/**
 * React Query hooks for the Database Viewer.
 *
 * INTEGRATION: Update the import path for `dbApi` to match your project's
 * API service location. See README.md for details.
 */
import { useQuery, useMutation } from '@tanstack/react-query'
import { dbApi } from '../services/dbApi'

export const adminDbKeys = {
  all: ['admin-db'] as const,
  tables: () => [...adminDbKeys.all, 'tables'] as const,
  tableData: (schema: string, table: string, page: number, pageSize: number, orderBy?: string, orderDir?: string) =>
    [...adminDbKeys.all, 'data', schema, table, page, pageSize, orderBy, orderDir] as const,
}

export function useDbTables() {
  return useQuery({
    queryKey: adminDbKeys.tables(),
    queryFn: () => dbApi.getTables(),
    staleTime: 30_000,
  })
}

export function useDbTableData(
  schema: string,
  table: string,
  page: number,
  pageSize: number,
  orderBy?: string,
  orderDir?: string,
) {
  return useQuery({
    queryKey: adminDbKeys.tableData(schema, table, page, pageSize, orderBy, orderDir),
    queryFn: () => dbApi.getTableData(schema, table, { page, page_size: pageSize, order_by: orderBy, order_dir: orderDir }),
    enabled: !!schema && !!table,
    staleTime: 10_000,
  })
}

export function useDbQuery() {
  return useMutation({
    mutationFn: (sql: string) => dbApi.runQuery(sql),
  })
}
