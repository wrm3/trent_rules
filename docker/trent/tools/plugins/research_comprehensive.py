"""
Comprehensive Research Tool Plugin

Combines web search and content scraping for full research workflow.
"""
import logging
from typing import Optional, List, Dict, Any
from datetime import datetime

# ============================================================
# PLUGIN METADATA (Required)
# ============================================================

TOOL_NAME = "research_comprehensive"

TOOL_DESCRIPTION = (
    "Perform comprehensive web research by combining search and content extraction. "
    "Searches for sources using reliable APIs (NO DuckDuckGo), then scrapes top results "
    "for detailed content. Returns full research data with quality assessment."
)

TOOL_PARAMS = {
    "query": "The research query to investigate",
    "max_sources": "Maximum number of sources to research in detail (default: 10)",
    "include_content": "Whether to scrape full content from sources (default: True)"
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
    max_sources: int = 10,
    include_content: bool = True,
    context: dict = None
) -> dict:
    """
    Perform comprehensive web research combining search and content extraction.
    """
    import aiohttp

    config = context.get('config', _config) if context else _config

    logger.info(f"Starting comprehensive research for: {query}")

    try:
        # Step 1: Search for sources
        search_results = await _perform_search(query, max_sources * 2, config)

        if not search_results.get('success'):
            return search_results

        # Step 2: Extract top URLs
        top_results = search_results.get('results', [])[:max_sources]
        urls_to_scrape = [r['url'] for r in top_results if r.get('url') and r['url'] != '#']

        logger.info(f"Found {len(urls_to_scrape)} URLs to scrape")

        # Step 3: Scrape content if requested
        scraped_content = {}
        if include_content and urls_to_scrape:
            scraped_content = await _scrape_urls(urls_to_scrape)

        # Step 4: Combine results
        enhanced_results = []
        for result in top_results:
            url = result.get('url', '')
            scraped = scraped_content.get(url, {})

            enhanced_result = {
                'title': result.get('title', ''),
                'url': url,
                'search_snippet': result.get('snippet', ''),
                'source': result.get('source', 'unknown'),
                'content_available': bool(scraped),
                'research_quality': scraped.get('research_quality', 'unknown')
            }

            if scraped:
                enhanced_result.update({
                    'full_content': scraped.get('text', '')[:20000],  # Limit content size
                    'content_length': scraped.get('text_length', 0),
                    'scraped_successfully': True,
                    'links': scraped.get('links', [])[:10]
                })
            else:
                enhanced_result['scraped_successfully'] = False

            enhanced_results.append(enhanced_result)

        # Calculate statistics
        successful_scrapes = sum(1 for r in enhanced_results if r.get('scraped_successfully'))
        high_quality = sum(1 for r in enhanced_results if r.get('research_quality') == 'high')

        return {
            'success': True,
            'query': query,
            'search_engine': search_results.get('engine', 'unknown'),
            'research_summary': {
                'total_sources': len(enhanced_results),
                'successful_scrapes': successful_scrapes,
                'high_quality_sources': high_quality,
                'search_engine': search_results.get('engine', 'unknown')
            },
            'sources': enhanced_results,
            'analysis': search_results.get('analysis'),  # Perplexity provides this
            'timestamp': datetime.now().isoformat()
        }

    except Exception as e:
        logger.error(f"Comprehensive research failed: {e}")
        return {
            'success': False,
            'error': str(e),
            'query': query
        }


async def _perform_search(query: str, max_results: int, config: dict) -> dict:
    """Perform web search using available engines."""
    import aiohttp

    # Get API keys
    perplexity_key = config.get('perplexity_api_key')
    google_key = config.get('google_search_api_key')
    google_cx = config.get('google_search_engine_id')

    # Try Perplexity first
    if perplexity_key:
        try:
            return await _search_perplexity(query, max_results, perplexity_key)
        except Exception as e:
            logger.warning(f"Perplexity search failed: {e}")

    # Try Google
    if google_key and google_cx:
        try:
            return await _search_google(query, max_results, google_key, google_cx)
        except Exception as e:
            logger.warning(f"Google search failed: {e}")

    # Fallback to direct sources
    return await _search_direct_sources(query)


async def _search_perplexity(query: str, max_results: int, api_key: str) -> dict:
    """Search using Perplexity API."""
    import aiohttp

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

            return {
                'success': True,
                'query': query,
                'engine': 'perplexity',
                'results': [],  # Perplexity returns analysis, not list
                'analysis': content,
                'timestamp': datetime.now().isoformat()
            }


async def _search_google(query: str, max_results: int, api_key: str, cx: str) -> dict:
    """Search using Google Custom Search API."""
    import aiohttp

    params = {
        "key": api_key,
        "cx": cx,
        "q": query,
        "num": min(max_results, 10)
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
                'timestamp': datetime.now().isoformat()
            }


async def _search_direct_sources(query: str) -> dict:
    """Provide curated direct sources based on query domain."""

    query_lower = query.lower()
    results = []

    # Banking/compliance sources
    if any(term in query_lower for term in ["bank", "compliance", "regulatory", "financial"]):
        results = [
            {"title": "FFIEC", "url": "https://www.ffiec.gov/", "snippet": "Federal examination procedures"},
            {"title": "FinCEN", "url": "https://www.fincen.gov/", "snippet": "BSA/AML compliance"},
            {"title": "OFAC", "url": "https://sanctionssearch.ofac.treas.gov/", "snippet": "Sanctions screening"},
        ]

    for r in results:
        r['source'] = 'direct_sources'

    return {
        'success': True,
        'query': query,
        'engine': 'direct_sources',
        'results': results,
        'timestamp': datetime.now().isoformat()
    }


async def _scrape_urls(urls: List[str]) -> Dict[str, dict]:
    """Scrape multiple URLs concurrently."""
    import aiohttp
    import asyncio
    import random

    results = {}

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    ]

    async def scrape_one(session, url):
        try:
            headers = {"User-Agent": random.choice(user_agents)}
            async with session.get(url, headers=headers, timeout=15) as response:
                if response.status == 200:
                    html = await response.text()
                    return url, _process_html(url, html)
        except Exception as e:
            logger.warning(f"Failed to scrape {url}: {e}")
        return url, None

    async with aiohttp.ClientSession() as session:
        tasks = [scrape_one(session, url) for url in urls[:10]]  # Limit concurrent
        scraped = await asyncio.gather(*tasks)

        for url, data in scraped:
            if data:
                results[url] = data

    return results


def _process_html(url: str, html: str) -> dict:
    """Process HTML and extract content."""
    try:
        from bs4 import BeautifulSoup
    except ImportError:
        return {'text': html[:10000], 'research_quality': 'unknown'}

    soup = BeautifulSoup(html, 'html.parser')

    # Remove unwanted elements
    for element in soup(['script', 'style', 'nav', 'footer', 'header']):
        element.decompose()

    # Extract text
    text = ""
    for element in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'li']):
        if element.text.strip():
            text += element.text.strip() + "\n\n"

    # Assess quality
    quality = "medium"
    if ".gov" in url or ".edu" in url:
        quality = "high"
    elif len(text) > 5000:
        quality = "medium"
    else:
        quality = "low"

    return {
        'text': text,
        'text_length': len(text),
        'research_quality': quality,
        'links': []
    }
