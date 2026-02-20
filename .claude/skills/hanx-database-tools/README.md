# Hanx Database Tools Skill

Enterprise-grade MySQL database interaction tools with comprehensive connection management, query execution, and result processing.

## Quick Start

### 1. Install Dependencies

```bash
# MySQL support
pip install mysql-connector-python python-dotenv sqlparse
```

### 2. Configure Environment

Copy the template and fill in your credentials:

```bash
cp templates/.env.database.example .env
# Edit .env with your database credentials
```

### 3. Basic Usage

#### MySQL

```python
from scripts.mysql_db import MySQLDB

# Using context manager (recommended)
with MySQLDB(source_db=True) as db:
    results = db.execute_query(
        "SELECT * FROM users WHERE status = %(status)s",
        params={'status': 'active'}
    )
    for row in results:
        print(f"User: {row['username']}")
```

## Key Features

### Security
- Parameterized queries prevent SQL injection
- Environment-based configuration (no hardcoded credentials)
- Connection parameter validation
- Error message sanitization

### Performance
- Connection pooling support
- Batch operations (executemany)
- Automatic resource cleanup
- Efficient data type conversion

### Reliability
- Context manager protocol
- Comprehensive error handling
- Transaction support
- Connection health checks

### Data Types
- Automatic MySQL type conversion (datetime, Decimal, bytes)
- JSON-compatible output

## File Structure

```
.cursor/skills/hanx-database-tools/
├── SKILL.md                          # Main skill documentation
├── rules.md                          # Implementation rules and standards
├── README.md                         # This file
├── scripts/
│   ├── mysql_db.py                  # MySQL connection class
│   ├── mysql_utils.py               # MySQL utility functions
│   ├── connection_manager.py        # Connection pooling
│   ├── query_builder.py             # Safe query construction
│   └── data_converter.py            # Type conversion utilities
├── templates/
│   └── .env.database.example        # Configuration template
└── examples/
    └── mysql_examples.md            # MySQL usage examples
```

## Common Tasks

### Test Connection

```bash
# Test MySQL connection
python scripts/mysql_db.py
```

### List Tables

```python
from scripts.mysql_db import MySQLDB

with MySQLDB(source_db=True) as db:
    tables = db.get_tables()
    print(f"Found {len(tables)} tables")
```

### Describe Table

```python
from scripts.mysql_db import MySQLDB

with MySQLDB(source_db=True) as db:
    columns = db.describe_table('users')
    for col in columns:
        print(f"{col['Field']}: {col['Type']}")
```

### Batch Insert

```python
from scripts.mysql_db import MySQLDB

with MySQLDB(source_db=False) as db:
    data = [
        {'name': 'Alice', 'email': 'alice@example.com'},
        {'name': 'Bob', 'email': 'bob@example.com'},
    ]
    db.execute_many(
        "INSERT INTO users (name, email) VALUES (%(name)s, %(email)s)",
        data
    )
```

## Security Best Practices

### Always Use Parameterized Queries

```python
# GOOD - Safe from SQL injection
results = db.execute_query(
    "SELECT * FROM users WHERE username = %(username)s",
    params={'username': user_input}
)

# BAD - SQL injection vulnerable
results = db.execute_query(
    f"SELECT * FROM users WHERE username = '{user_input}'"
)
```

### Store Credentials in .env

```bash
# .env file (add to .gitignore!)
src_mysql_host=localhost
src_mysql_port=3306
src_mysql_user=myuser
src_mysql_pw=mypassword
```

## Troubleshooting

### MySQL Connection Issues

**Error**: "Can't connect to MySQL server"
- Check if MySQL server is running
- Verify host and port in .env file
- Check network connectivity/firewall

**Error**: "Access denied for user"
- Verify username and password in .env
- Check user has appropriate permissions
- Ensure user can connect from your host

## Integration

### With MCP Servers

This skill is compatible with MCP servers for AI assistant integration.

### With Other Skills

- **trent-task-management**: Create database-related tasks
- **trent-qa**: Report database bugs and issues
- **trent-planning**: Include database schema in planning

## Version

**Version**: 2.0.0
**Last Updated**: 2026-01-31
**Compatibility**: Cursor IDE, VS Code
