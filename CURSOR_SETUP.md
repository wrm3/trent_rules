# Cursor + trent Setup Guide

This guide walks you through setting up the trent AI development system in Cursor IDE.

## Prerequisites

| Requirement | Version | Notes |
|-------------|---------|-------|
| **Docker Desktop** | Latest | **Required** - MCP server runs in Docker |
| **Cursor IDE** | Latest | Download from [cursor.com](https://cursor.com) |
| **Git** | 2.x+ | For cloning the repository |

### Installing Docker Desktop

1. Download from [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/)
2. Run the installer (requires admin rights)
3. Restart your machine when prompted
4. Launch Docker Desktop and wait for it to fully start (whale icon in system tray should be steady, not animating)
5. Verify installation in PowerShell: `docker --version`

**Important**: Docker Desktop must be running before you start the MCP server. If you see "docker daemon is not running" errors, open Docker Desktop and wait for it to initialize.

## Setup Overview

```
Step 1: Clone the repo
Step 2: Start Docker MCP server
Step 3: Configure mcp.json in Cursor
Step 4: Install trent into your project
Step 5: Verify everything works
```

## Step 1: Clone the Repository

```bash
git clone https://github.com/fstrent/trent_rules.git
cd trent_rules
```

## Step 2: Start the MCP Server

```bash
cd docker
docker-compose up -d
```

This starts the full stack including:
- `trent` MCP server on port **8082** (RAG, research, Oracle, video analysis, templates)
- `postgres` database on port **5433** (for RAG knowledge base)

Verify it's running:

```bash
docker ps | grep trent
```

You should see `trent` and `trent_postgres` running and healthy.

## Step 3: Configure Cursor MCP Connection

Cursor needs to know where the MCP server is. You do this by editing your **mcp.json** file.

### Locate your mcp.json

The MCP configuration file is located at:

```
Windows:  C:\Users\<your-username>\.cursor\mcp.json
macOS:    ~/.cursor/mcp.json
Linux:    ~/.cursor/mcp.json
```

### Edit mcp.json

Open the file and add the `trent` server entry. If the file doesn't exist, create it.

**If you're running Docker locally (same machine as Cursor):**

```json
{
  "mcpServers": {
    "trent": {
      "url": "http://localhost:8082/sse"
    }
  }
}
```

**If Docker is running on a different machine (e.g., a shared server):**

Replace `localhost` with the IP address or hostname of the Docker host:

```json
{
  "mcpServers": {
    "trent": {
      "url": "http://192.168.1.100:8082/sse"
    }
  }
}
```

**If you already have other MCP servers configured**, just add the `trent` entry inside the existing `mcpServers` block:

```json
{
  "mcpServers": {
    "some_other_server": {
      "url": "http://localhost:9000/mcp"
    },
    "trent": {
      "url": "http://localhost:8082/sse"
    }
  }
}
```

A reference copy is available at `docker/mcp.json.example`.

### Restart Cursor

After editing `mcp.json`, **restart Cursor** for the changes to take effect. The MCP server connection is loaded at startup.

## Step 4: Install trent Into Your Project

The repo you cloned is the **distribution source**. The template folders contain everything you need to set up trent in any project.

### Choose your template

| Template | What's Included | Best For |
|----------|----------------|----------|
| `docker/templates/` | Core rules, commands, trent skills, basic agents, task management | Minimal setup, small projects |
| `docker/templates_full/` | ALL agents, ALL skills, ALL rules, full agent SDK | Full development environment (recommended) |

### Copy to your project

Open a terminal and copy the template contents into your project folder:

**Full installation (recommended):**

```powershell
# From the trent_rules repo root:
xcopy /E /I /Y docker\templates_full\.cursor G:\my-project\.cursor
xcopy /E /I /Y docker\templates_full\.claude G:\my-project\.claude
xcopy /E /I /Y docker\templates_full\.trent G:\my-project\.trent
copy /Y docker\templates_full\agents.md G:\my-project\agents.md
copy /Y docker\templates_full\CLAUDE.md G:\my-project\CLAUDE.md
copy /Y LICENSE G:\my-project\LICENSE
copy /Y NOTICE G:\my-project\NOTICE
```

**Or use the MCP install_trent tool:**

In Cursor chat, ask the AI to install trent to your project:
```
Use the install_trent tool to install trent templates to G:\my-project
```

**Minimal installation:**

```powershell
xcopy /E /I /Y docker\templates\* G:\my-project\
```

### What gets installed

```
your-project/
├── .cursor/              # Cursor IDE AI configuration
│   ├── agents/           # Specialized AI agents
│   ├── skills/           # AI skill definitions
│   ├── rules/            # .mdc rule files (auto-loaded by Cursor)
│   └── commands/         # @trent-* commands
├── .claude/              # Claude Code configuration
│   ├── agents/           # Agent definitions + SDK
│   ├── skills/           # Skill definitions
│   └── commands/         # Claude Code commands
├── .trent/               # Task management
│   ├── TASKS.md          # Master task list
│   ├── PLAN.md           # Product requirements
│   ├── tasks/            # Individual task files
│   └── phases/           # Phase documentation
├── agents.md             # AI agent instructions
├── CLAUDE.md             # Claude-specific context
├── LICENSE               # MIT License
└── NOTICE                # Attribution
```

**Reopen the project folder in Cursor** after copying so the new rules load.

## Step 5: Verify Everything Works

In a Cursor Agent chat within your project, type:

```
@trent-status
```

You should see a project status overview. The AI agent will also have access to:
- All specialized agents
- All skills
- All `@trent-*` commands
- RAG knowledge base tools
- Research tools
- Oracle database query/execute tools
- Markdown to HTML conversion

## MCP Tools Available

These tools are available in any Cursor chat once `mcp.json` is configured:

| Category | Tools | Description |
|----------|-------|-------------|
| **RAG** | `rag_search`, `rag_ingest_text`, `rag_list_sources`, `rag_stats` | Semantic search over knowledge bases |
| **Research** | `research_search`, `research_scrape`, `research_comprehensive`, `research_deep` | Web research via Perplexity/Google |
| **Video** | `video_analyze`, `video_extract_frames`, `video_extract_transcript`, `video_batch_process` | YouTube/video analysis with AI vision |
| **Oracle** | `oracle_query`, `oracle_execute` | Oracle database operations |
| **MediaWiki** | `mediawiki_page`, `mediawiki_search` | Wiki page CRUD and search |
| **Template** | `install_trent` | Install trent to new projects (from GitHub) |
| **Utility** | `md_to_html` | Convert markdown to styled HTML |

## Oracle Database Usage

Oracle credentials are **not stored in configuration files**. They are passed with each query:

```
Use the oracle_query tool to run:
SELECT * FROM my_table WHERE rownum <= 10

Host: your-oracle-host
Port: 1521
Username: your_username
Password: your_password
Service: your_service_name
```

The MCP server uses Oracle Instant Client (thick mode) pre-installed in the Docker container, supporting Oracle Network Encryption.

## Task Management (After Installation)

trent uses a file-based task management system in `.trent/`:

1. **TASKS.md** - Master task list (check here first)
2. **tasks/** - Detailed task files
3. **phases/** - Phase documentation
4. **PLAN.md** - Product requirements

### Quick Task Workflow

```
@trent-task-new       # Create a task
@trent-task-update    # Update task status
@trent-status         # See overall progress
@trent-task-sync-check # Verify consistency
```

## Environment Variables

Create a `.env` file in the `docker/` folder (copy from `.env.example`):

### Required for RAG

| Variable | Description | Example |
|----------|-------------|---------|
| `OPENAI_API_KEY` | OpenAI API key for embeddings | `sk-...` |
| `POSTGRES_PASSWORD` | Database password | `your_secure_password` |

### Optional: Research APIs

| Variable | Description |
|----------|-------------|
| `PERPLEXITY_API_KEY` | Perplexity API (best for research) |
| `GOOGLE_SEARCH_API_KEY` | Google Custom Search API |
| `GOOGLE_SEARCH_ENGINE_ID` | Google Search Engine ID |
| `ANTHROPIC_API_KEY` | Anthropic API (for summaries) |

### Optional: MediaWiki

| Variable | Description |
|----------|-------------|
| `MEDIAWIKI_URL` | Wiki base URL |
| `MEDIAWIKI_USERNAME` | Bot username |
| `MEDIAWIKI_PASSWORD` | Bot password |

## Troubleshooting

### Docker container won't start

```bash
# Check logs
docker logs trent

# Rebuild from scratch
cd docker
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

### MCP tools not appearing in Cursor

1. Verify Docker is running: `docker ps | grep trent`
2. Check mcp.json is saved at `C:\Users\<you>\.cursor\mcp.json`
3. Verify the URL is correct: `http://localhost:8082/sse`
4. **Restart Cursor** after editing mcp.json
5. Try opening `http://localhost:8082/` in your browser to confirm the server responds

### Oracle connection fails

- Verify the Oracle host is reachable from the Docker container
- Check VPN connection if accessing internal databases
- Credentials are passed per-query; double-check spelling
- The Docker container needs network access to the Oracle host

### Rules/Skills not loading after copying templates

- **Reopen the project folder** in Cursor after copying template files
- Rules in `.cursor/rules/` auto-load when the project folder is open
- Skills in `.cursor/skills/` are available via the AI agent
- Check that `.mdc` files have valid YAML frontmatter

### Can't find mcp.json

The file should be at `C:\Users\<your-username>\.cursor\mcp.json`. If it doesn't exist, create it with the content shown in Step 3 above.

## Repository Structure

```
trent_rules/                     # Distribution repo (clone this)
├── docker/                      # MCP server
│   ├── docker-compose.yml       # Docker config
│   ├── Dockerfile               # Python 3.11 + Oracle Instant Client
│   ├── mcp.json.example         # Reference MCP config
│   ├── templates/               # Basic install templates
│   ├── templates_full/          # Full install templates
│   └── trent/                   # MCP server code
│       ├── server.py            # FastMCP server
│       ├── config.py            # Configuration
│       ├── plugin_loader.py     # Dynamic plugin loader
│       └── tools/plugins/       # Tool implementations
├── .cursor/                     # Full Cursor configuration
│   ├── agents/                  # All specialized agents
│   ├── skills/                  # All AI skills
│   ├── rules/                   # All .mdc rules
│   └── commands/                # All @trent-* commands
├── .claude/                     # Claude Code configuration
├── .trent/                      # Task management
├── docs/                        # Project documentation
├── CURSOR_SETUP.md              # This setup guide
├── README.md                    # Project overview
├── LICENSE                      # MIT License
└── NOTICE                       # Attribution
```

## Getting Help

- **Ask the AI agent** - Once installed, it has full context via rules and skills
- **Check `AGENTS.md`** - Detailed documentation (available after installation)
- **Check `docker/`** - MCP server configuration and logs
- **GitHub Issues** - Report bugs or request features

---

**Version**: 3.2.0
**Last Updated**: 2026-02-19
