---
name: hanx-database-tools
description: MySQL database interaction tools with connection management, query execution, and result processing. Provides context managers, parameterized queries, connection pooling, metadata extraction, and comprehensive error handling for database operations.
---

# Hanx Database Tools Skill

Enterprise-grade database interaction tools for MySQL databases with comprehensive connection management, query execution, result processing, and metadata extraction capabilities.

## Overview

This skill provides robust database interaction capabilities based on proven production implementations from MCP servers and enterprise tools. It includes:

- **MySQL Support**: Full connection management with pooling, parameterized queries, transaction control
- **Security**: Parameterized queries for SQL injection prevention, connection validation
- **Context Managers**: Safe resource cleanup with Python context manager protocol
- **Error Handling**: Comprehensive error categorization and user-friendly messages
- **Data Conversion**: Automatic conversion of database types to JSON-compatible formats

## When to Use This Skill

**Activate this skill when:**
- Setting up database connections for MySQL
- Executing database queries (SELECT, INSERT, UPDATE, DELETE)
- Performing database schema operations (CREATE, ALTER, DROP)
- Extracting database metadata (tables, columns, constraints)
- Implementing database migration scripts
- Building data processing pipelines
- Handling database transactions

## Core Capabilities

### MySQL Database Operations

#### Connection Management
- Environment-based configuration (.env file support)
- Connection pooling for performance
- Automatic connection lifecycle management
- Context manager support for safe cleanup
- Parameterized connection parameters

#### Query Execution
- **Read Operations**: SELECT, SHOW, DESCRIBE, EXPLAIN
- **Write Operations**: INSERT, UPDATE, DELETE, REPLACE
- **DDL Operations**: CREATE, ALTER, DROP, TRUNCATE
- **Parameterized Queries**: SQL injection prevention with ? placeholders
- **Batch Operations**: executemany for bulk inserts/updates
- **Transaction Control**: Commit/rollback support

#### Result Processing
- Dictionary-based results (column_name: value)
- Automatic data type conversion (datetime, Decimal, bytes)
- JSON-compatible output format
- Row count information
- Column metadata

## Usage Patterns

### MySQL Usage

#### Basic Query Execution
```python
from scripts.mysql_db import MySQLDB

# Simple query with context manager
with MySQLDB(source_db=True) as db:
    results = db.execute_query("SELECT * FROM users WHERE active = 1")
    for row in results:
        print(f"User: {row['username']}, Email: {row['email']}")
```

#### Parameterized Queries (Security Best Practice)
```python
# Prevent SQL injection with parameterized queries
with MySQLDB(source_db=True) as db:
    # Safe query - parameters are escaped automatically
    query = "SELECT * FROM users WHERE username = %(username)s AND status = %(status)s"
    params = {'username': user_input, 'status': 'active'}
    results = db.execute_query(query, params)
```

#### Batch Operations
```python
# Efficient bulk inserts
with MySQLDB(source_db=False) as db:
    insert_query = "INSERT INTO logs (message, level, timestamp) VALUES (%(msg)s, %(lvl)s, NOW())"
    batch_data = [
        {'msg': 'User login', 'lvl': 'INFO'},
        {'msg': 'Data processed', 'lvl': 'DEBUG'},
        {'msg': 'Error occurred', 'lvl': 'ERROR'}
    ]
    db.execute_many(insert_query, batch_data)
```

#### Transaction Management
```python
# Manual transaction control
db = MySQLDB(source_db=True)
db.connect()
try:
    db.execute_query("START TRANSACTION")
    db.execute_query("UPDATE accounts SET balance = balance - 100 WHERE id = 1")
    db.execute_query("UPDATE accounts SET balance = balance + 100 WHERE id = 2")
    db.execute_query("COMMIT")
except Exception as e:
    db.execute_query("ROLLBACK")
    raise
finally:
    db.disconnect()
```

### Connection Manager Usage

#### Connection Pooling
```python
from scripts.connection_manager import ConnectionPool

# Create connection pool for high-throughput applications
pool = ConnectionPool(
    db_type='mysql',
    host='localhost',
    port=3306,
    database='production',
    user='app_user',
    password='secure_password',
    pool_size=10,
    max_overflow=5
)

# Get connection from pool
with pool.get_connection() as conn:
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM orders WHERE status = 'pending'")
    orders = cursor.fetchall()
```

#### Connection Health Checks
```python
from scripts.connection_manager import test_connection

# Validate connection before use
is_valid, error_msg = test_connection(
    db_type='mysql',
    host='database-server',
    port=3306,
    username='app_user',
    password='password',
    database='production'
)

if is_valid:
    print("Connection successful!")
else:
    print(f"Connection failed: {error_msg}")
```

## Configuration

### Environment Variables

Create a `.env` file in your project root:

```bash
# MySQL Source Database
src_mysql_host=localhost
src_mysql_port=3306
src_mysql_db=source_database
src_mysql_user=source_user
src_mysql_pw=source_password

# MySQL Target Database
tgt_mysql_host=localhost
tgt_mysql_port=3306
tgt_mysql_db=target_database
tgt_mysql_user=target_user
tgt_mysql_pw=target_password
```

### Python Dependencies

Add to your `requirements.txt`:

```
# MySQL Support
mysql-connector-python>=8.0.0

# Utilities
python-dotenv>=1.0.0
sqlparse>=0.4.0  # SQL parsing and validation
```

## Security Best Practices

### 1. Always Use Parameterized Queries

```python
# BAD - SQL Injection Vulnerable
user_input = request.args.get('username')
query = f"SELECT * FROM users WHERE username = '{user_input}'"  # UNSAFE!

# GOOD - Protected Against SQL Injection
query = "SELECT * FROM users WHERE username = %s"
params = (user_input,)
results = db.execute_query(query, params)
```

### 2. Environment-Based Configuration

```python
# GOOD - Credentials from environment
from dotenv import load_dotenv
import os

load_dotenv()
db = MySQLDB(source_db=True)  # Uses .env variables

# BAD - Hardcoded credentials
db = mysql.connector.connect(
    host="production-server",
    user="admin",
    password="hardcoded_password"  # NEVER DO THIS!
)
```

## Error Handling

### MySQL Error Categories

The skill provides categorized error handling:

- **CONNECTION**: Server unreachable, network issues, timeout
- **AUTHENTICATION**: Invalid credentials, access denied
- **SYNTAX**: SQL syntax errors
- **SCHEMA**: Table/column not found, database doesn't exist
- **DATA**: Constraint violations, data too long, foreign key errors
- **SERVER**: Internal server errors
- **TIMEOUT**: Operation timeout
- **UNKNOWN**: Unexpected errors

### Example Error Handling

```python
from scripts.mysql_db import MySQLDB
from mysql.connector import Error

try:
    with MySQLDB(source_db=True) as db:
        results = db.execute_query("SELECT * FROM users")
except Error as e:
    error_code = e.errno
    error_msg = str(e)

    if error_code == 1045:
        print("Authentication failed. Check username/password.")
    elif error_code == 2003:
        print("Cannot connect to database server.")
    elif error_code == 1146:
        print("Table does not exist.")
    else:
        print(f"Database error: {error_msg}")
```

## File Reference

### Core Scripts

- `scripts/mysql_db.py` - MySQL connection and query execution class
- `scripts/mysql_utils.py` - MySQL utility functions (query, execute, describe_table)
- `scripts/connection_manager.py` - Connection pooling and validation
- `scripts/query_builder.py` - Safe query construction utilities
- `scripts/data_converter.py` - Database type to JSON conversion

### Templates

- `templates/.env.database.example` - Environment configuration template

### Examples

- `examples/mysql_examples.md` - Comprehensive MySQL usage examples

## Success Criteria

A successful implementation should demonstrate:

- Secure database connections using environment variables
- Parameterized queries preventing SQL injection
- Proper error handling with user-friendly messages
- Context manager usage for resource cleanup
- Efficient batch operations for bulk data
- Metadata extraction capabilities
- Connection pooling for performance
- Comprehensive logging for debugging
- Type conversion for JSON compatibility

## Support and Resources

### Documentation
- MySQL Connector/Python: https://dev.mysql.com/doc/connector-python/en/
- SQL Injection Prevention: https://owasp.org/www-community/attacks/SQL_Injection

---

**Last Updated**: 2026-01-31
**Version**: 2.0.0
**Skill Type**: Database Integration
**Compatibility**: Cursor IDE, VS Code
