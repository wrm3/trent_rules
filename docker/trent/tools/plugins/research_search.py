"""
Research Web Search Tool Plugin

Perform web searches for research using reliable APIs (NO DuckDuckGo).
Supports Perplexity, Google Custom Search, and direct source access.
"""
import logging
from typing import Optional, List, Dict, Any
from datetime import datetime

# ============================================================
# PLUGIN METADATA (Required)
# ============================================================

TOOL_NAME = "research_search"

TOOL_DESCRIPTION = (
    "Perform web searches for research using reliable search APIs. "
    "Supports Perplexity (best for research), Google Custom Search, and direct source access. "
    "NO DuckDuckGo due to rate limiting issues. "
    "Returns comprehensive results with sources and analysis."
)

TOOL_PARAMS = {
    "query": "The search query to research",
    "max_results": "Maximum number of results to return (default: 20)",
    "engine": "Preferred engine: 'auto', 'perplexity', 'google', 'direct' (default: 'auto')"
}


logger = logging.getLogger(__name__)

# ============================================================
# PLUGIN IMPLEMENTATION
# ============================================================

_config = None


def setup(context: dict):
    """Called once during plugin loading to set up dependencies."""
    global _config
    _config = context.get('config', {})


async def execute(
    query: str,
    max_results: int = 20,
    engine: str = "auto",
    context: dict = None
) -> dict:
    """
    Perform web search for research using reliable APIs.

    Priority: Perplexity > Google > Direct Sources
    NO DuckDuckGo due to rate limiting issues.
    """
    import aiohttp

    config = context.get('config', _config) if context else _config

    # Get API keys from config
    perplexity_key = config.get('perplexity_api_key')
    google_key = config.get('google_search_api_key')
    google_cx = config.get('google_search_engine_id')

    logger.info(f"Research search for: {query}")

    # Determine which engine to use
    available_engines = []
    if perplexity_key:
        available_engines.append('perplexity')
    if google_key and google_cx:
        available_engines.append('google')
    available_engines.append('direct')  # Always available

    if not available_engines:
        return {
            'success': False,
            'error': 'No search engines available. Configure PERPLEXITY_API_KEY or GOOGLE_SEARCH_API_KEY.'
        }

    # Select engine
    if engine == 'auto':
        selected_engine = available_engines[0]
    elif engine in available_engines:
        selected_engine = engine
    else:
        selected_engine = available_engines[0]

    try:
        if selected_engine == 'perplexity':
            return await _search_perplexity(query, max_results, perplexity_key)
        elif selected_engine == 'google':
            return await _search_google(query, max_results, google_key, google_cx)
        else:
            return await _search_direct_sources(query)

    except Exception as e:
        logger.error(f"Research search failed: {e}")
        return {
            'success': False,
            'error': str(e),
            'query': query,
            'engine_attempted': selected_engine
        }


async def _search_perplexity(query: str, max_results: int, api_key: str) -> dict:
    """Search using Perplexity API - best for research."""
    import aiohttp

    logger.info(f"Searching with Perplexity: {query}")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "sonar-medium-online",
        "messages": [{"role": "user", "content": f"Research: {query}. Provide comprehensive information with sources."}],
        "max_tokens": 2000,
        "temperature": 0.1
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://api.perplexity.ai/chat/completions",
            headers=headers,
            json=data
        ) as response:
            if response.status != 200:
                raise Exception(f"Perplexity API error: {response.status}")

            result = await response.json()
            content = result.get("choices", [{}])[0].get("message", {}).get("content", "")

            # Extract sources from Perplexity response
            sources = _extract_perplexity_sources(content)

            return {
                'success': True,
                'query': query,
                'engine': 'perplexity',
                'results': sources,
                'total_results': len(sources),
                'analysis': content,
                'timestamp': datetime.now().isoformat()
            }


async def _search_google(query: str, max_results: int, api_key: str, cx: str) -> dict:
    """Search using Google Custom Search API."""
    import aiohttp

    logger.info(f"Searching with Google: {query}")

    params = {
        "key": api_key,
        "cx": cx,
        "q": query,
        "num": min(max_results, 10)  # Google API limit
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://www.googleapis.com/customsearch/v1",
            params=params
        ) as response:
            if response.status != 200:
                raise Exception(f"Google Search API error: {response.status}")

            data = await response.json()
            results = []

            for item in data.get("items", []):
                results.append({
                    "title": item.get("title", ""),
                    "url": item.get("link", ""),
                    "snippet": item.get("snippet", ""),
                    "source": "google"
                })

            return {
                'success': True,
                'query': query,
                'engine': 'google',
                'results': results,
                'total_results': len(results),
                'timestamp': datetime.now().isoformat()
            }


async def _search_direct_sources(query: str) -> dict:
    """Direct access to known authoritative sources for specific domains."""

    logger.info(f"Searching direct sources for: {query}")

    query_lower = query.lower()
    results = []

    # Banking/financial sources
    if any(term in query_lower for term in ["bank", "compliance", "regulatory", "financial", "bsa", "aml"]):
        results.extend([
            {"title": "FFIEC - Federal Financial Institutions Examination Council",
             "url": "https://www.ffiec.gov/",
             "snippet": "Examination procedures, compliance guides, regulatory requirements"},
            {"title": "FinCEN - Financial Crimes Enforcement Network",
             "url": "https://www.fincen.gov/",
             "snippet": "BSA, AML, suspicious activity reporting, compliance"},
            {"title": "OFAC - Sanctions Search",
             "url": "https://sanctionssearch.ofac.treas.gov/",
             "snippet": "Sanctions screening, SDN list, OFAC compliance"},
            {"title": "Federal Reserve Board",
             "url": "https://www.federalreserve.gov/",
             "snippet": "Monetary policy, bank regulation, supervisory guidance"},
            {"title": "OCC - Office of the Comptroller",
             "url": "https://www.occ.gov/",
             "snippet": "National bank supervision, regulatory bulletins"}
        ])

    # Technology sources
    if any(term in query_lower for term in ["python", "javascript", "programming", "api", "software"]):
        results.extend([
            {"title": "Python Documentation",
             "url": "https://docs.python.org/",
             "snippet": "Official Python language documentation"},
            {"title": "MDN Web Docs",
             "url": "https://developer.mozilla.org/",
             "snippet": "Web technologies, JavaScript, HTML, CSS documentation"},
            {"title": "GitHub",
             "url": "https://github.com/",
             "snippet": "Code repositories, open source projects"}
        ])

    # Academic sources
    if any(term in query_lower for term in ["research", "study", "academic", "paper", "journal"]):
        results.extend([
            {"title": "Google Scholar",
             "url": "https://scholar.google.com/",
             "snippet": "Academic papers, citations, scholarly literature"},
            {"title": "arXiv",
             "url": "https://arxiv.org/",
             "snippet": "Open access research papers, preprints"},
            {"title": "PubMed",
             "url": "https://pubmed.ncbi.nlm.nih.gov/",
             "snippet": "Biomedical literature, medical research"}
        ])

    # Generic fallback
    if not results:
        results.append({
            "title": f"Research Required: {query}",
            "url": "#",
            "snippet": "Configure Perplexity or Google API keys for comprehensive search results.",
            "source": "fallback"
        })

    for r in results:
        r['source'] = 'direct_sources'

    return {
        'success': True,
        'query': query,
        'engine': 'direct_sources',
        'results': results,
        'total_results': len(results),
        'timestamp': datetime.now().isoformat(),
        'note': 'Results from curated authoritative sources'
    }


def _extract_perplexity_sources(content: str) -> List[Dict[str, Any]]:
    """Extract source citations from Perplexity response."""
    sources = []

    # Perplexity includes citations in various formats
    lines = content.split('\n')
    for line in lines:
        if '[' in line and ']' in line and ('http' in line.lower() or 'www.' in line.lower()):
            sources.append({
                "title": line.strip()[:100],
                "url": "#",  # Perplexity doesn't always provide direct URLs
                "snippet": line.strip(),
                "source": "perplexity_citation"
            })

    return sources[:20]
