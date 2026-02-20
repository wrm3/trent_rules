"""
trent - Unified MCP Server with Dynamic Tool Loading

Provides:
- RAG (semantic search over knowledge bases)
- Deep research (Perplexity, Google - NO DuckDuckGo)
- MediaWiki integration
- Template installation for new projects

TRANSPORT MODES:
    - stdio (default): Standard input/output for IDE integration
    - sse: Server-Sent Events over HTTP
    - streamable-http: Full HTTP transport for Docker deployment

    Set MCP_TRANSPORT environment variable to choose transport mode.

DYNAMIC TOOL LOADING:
    Tools are loaded from trent/tools/plugins/ at startup.
    Each .py file (except those starting with _) is loaded as a plugin.
"""
import os
import sys
import logging
import atexit
from pathlib import Path
from datetime import datetime
from typing import Optional

from mcp.server.fastmcp import FastMCP

# Setup logging before imports
LOG_DIR = Path(__file__).parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

log_file = LOG_DIR / f"trent_{datetime.now():%Y%m%d}.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
logger.info("=" * 60)
logger.info("trent server starting (unified MCP)...")

# Import configuration
from .config import load_config

# Load configuration
try:
    config = load_config()
    logger.info("Configuration loaded successfully")
except EnvironmentError as e:
    logger.error(f"Configuration error: {e}")
    print(f"ERROR: {e}", file=sys.stderr)
    sys.exit(1)

# Import database modules (RAG)
from .database.client import RAGDatabase
from .database.embeddings import EmbeddingGenerator
from .database.multi_subject import MultiSubjectDatabase, SubjectAwareDBWrapper
from .subjects import SubjectManager
from .plugin_loader import PluginLoader

# Initialize components
db: Optional[RAGDatabase] = None
multi_db: Optional[MultiSubjectDatabase] = None
embedding_generator: Optional[EmbeddingGenerator] = None
subject_manager: Optional[SubjectManager] = None
plugin_loader: Optional[PluginLoader] = None

# RAG components (optional - only if PostgreSQL configured)
if config.get('postgres_host'):
    try:
        subject_manager = SubjectManager()
        multi_db = MultiSubjectDatabase(subject_manager)
        db = RAGDatabase(config)
        embedding_generator = EmbeddingGenerator(config.get('openai_api_key'))

        logger.info("RAG components initialized")
        logger.info(f"Available subjects: {[s.id for s in subject_manager.list_subjects()]}")

        if multi_db.test_connection():
            logger.info("Database connection test successful")
        else:
            logger.warning("Database connection test failed - RAG queries may fail")

    except Exception as e:
        logger.warning(f"RAG initialization failed (optional): {e}")
        subject_manager = None
        multi_db = None
        db = None
        embedding_generator = None
else:
    logger.info("PostgreSQL not configured - RAG features disabled")

# Initialize FastMCP server
mcp = FastMCP(
    "trent_rules_docker",
    instructions="""
Unified MCP Server - trent

This server provides multiple tool categories:

**RAG (Knowledge Base):**
- rag_search - Semantic search over knowledge bases
- rag_ingest_text - Store text content
- rag_ingest_url - Store web content
- rag_list_sources - Browse content catalog
- rag_stats - Knowledge base statistics
- Subject management (create, delete, list, set default)

**Oracle Database:**
- oracle_query - Execute read queries (source database)
- oracle_execute - Execute write operations (target database)
- oracle_describe - Describe Oracle objects

**Research Tools (NO DuckDuckGo):**
- research_query - Deep research via Perplexity/Google
- research_summarize - Summarize research content
- web_fetch - Fetch and extract web content

**MediaWiki:**
- mediawiki_get_page - Get wiki page content
- mediawiki_create_page - Create new pages
- mediawiki_update_page - Update existing pages
- mediawiki_search - Search wiki

**Template Installer:**
- template_install - Install trent to new projects
- template_check - Check installation status
- template_update - Update existing installation

Use the appropriate tools based on your task.
"""
)

# Initialize plugin loader and discover plugins
try:
    plugins_dir = Path(__file__).parent / "tools" / "plugins"
    plugin_loader = PluginLoader(plugins_dir)

    # Set context that plugins can access
    plugin_loader.set_context(
        db=db,
        multi_db=multi_db,
        embedding_generator=embedding_generator,
        subject_manager=subject_manager,
        config=config,
        config_path=Path(__file__).parent / "subjects.json"
    )

    # Discover and load plugins
    discovered = plugin_loader.discover_plugins()
    logger.info(f"Discovered {len(discovered)} plugins: {discovered}")

    # Register plugins with FastMCP
    registered_count = plugin_loader.register_all(mcp)
    logger.info(f"Registered {registered_count} dynamic tools with MCP server")

except Exception as e:
    logger.error(f"Plugin loading failed: {e}")
    print(f"WARNING: Plugin loading failed: {e}", file=sys.stderr)


# ========================================
# Server Status Tool (Always Available)
# ========================================

@mcp.tool(
    description="Get server status, loaded plugins, and available features. Use as health check."
)
async def trent_server_status() -> dict:
    """
    Get server status and list of loaded tools.
    Also serves as a health check endpoint.

    Returns:
        Server status including loaded plugins and available features
    """
    features = []
    if db is not None:
        features.append("rag")
    if config.get('oracle_src_host'):
        features.append("oracle")
    if config.get('perplexity_api_key') or config.get('google_search_api_key'):
        features.append("research")
    if config.get('mediawiki_url'):
        features.append("mediawiki")
    features.append("template_installer")  # Always available

    return {
        'success': True,
        'status': 'healthy',
        'server': 'trent_rules_docker',
        'version': '1.0.0',
        'transport': os.getenv('MCP_TRANSPORT', 'stdio'),
        'features': features,
        'plugins': plugin_loader.list_plugins() if plugin_loader else [],
        'subjects': [s.id for s in subject_manager.list_subjects()] if subject_manager else [],
        'default_subject': subject_manager.default_subject_id if subject_manager else None
    }


# Cleanup handler
@atexit.register
def cleanup():
    """Clean up resources on shutdown."""
    logger.info("Shutting down trent server...")
    if db:
        db.close()
    if subject_manager:
        subject_manager.close_all_connections()
    logger.info("Shutdown complete")


def main():
    """
    Main entry point for the MCP server.

    Transport mode is controlled by MCP_TRANSPORT environment variable:
    - stdio (default): Standard I/O for IDE integration
    - sse: Server-Sent Events over HTTP
    - streamable-http: Full HTTP transport for Docker
    """
    transport = os.getenv('MCP_TRANSPORT', 'stdio').lower()

    if transport == 'stdio':
        logger.info("Starting trent MCP server (stdio transport)")
        logger.info(f"Loaded {len(plugin_loader.plugins) if plugin_loader else 0} dynamic tools")
        mcp.run(transport='stdio')

    elif transport in ('sse', 'streamable-http', 'http'):
        host = os.getenv('MCP_HOST', '0.0.0.0')
        port = int(os.getenv('MCP_PORT', '8082'))

        logger.info(f"Starting trent MCP server ({transport} transport)")
        logger.info(f"Listening on http://{host}:{port}")
        logger.info(f"Loaded {len(plugin_loader.plugins) if plugin_loader else 0} dynamic tools")

        try:
            import uvicorn
        except ImportError:
            logger.error("uvicorn required for HTTP transport. Install with: pip install uvicorn")
            print("ERROR: uvicorn required for HTTP transport", file=sys.stderr)
            sys.exit(1)

        if transport == 'sse':
            app = mcp.sse_app()
        else:
            app = mcp.streamable_http_app()

        logger.info("MCP server ready - use trent_server_status tool to check health")
        uvicorn.run(app, host=host, port=port, log_level="info")

    else:
        logger.error(f"Unknown transport mode: {transport}")
        print(f"ERROR: Unknown transport mode '{transport}'", file=sys.stderr)
        sys.exit(1)


def main_http():
    """Convenience entry point for HTTP transport mode."""
    os.environ['MCP_TRANSPORT'] = 'streamable-http'
    main()


def main_sse():
    """Convenience entry point for SSE transport mode."""
    os.environ['MCP_TRANSPORT'] = 'sse'
    main()


if __name__ == "__main__":
    main()
