"""
Research Web Scraping Tool Plugin

Scrape content from URLs for research analysis with quality assessment.
"""
import logging
import random
from typing import Optional, Dict, Any, List
from datetime import datetime

# ============================================================
# PLUGIN METADATA (Required)
# ============================================================

TOOL_NAME = "research_scrape"

TOOL_DESCRIPTION = (
    "Scrape content from a URL for research analysis. "
    "Extracts main content, assesses research quality, and returns structured data. "
    "Supports HTML pages with content extraction and quality assessment."
)

TOOL_PARAMS = {
    "url": "The URL to scrape content from",
    "extract_links": "Whether to extract links from the page (default: True)",
    "max_content_length": "Maximum content length to return (default: 50000)"
}


logger = logging.getLogger(__name__)

# ============================================================
# PLUGIN IMPLEMENTATION
# ============================================================

_config = None

DEFAULT_USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/122.0",
]


def setup(context: dict):
    """Called once during plugin loading to set up dependencies."""
    global _config
    _config = context.get('config', {})


async def execute(
    url: str,
    extract_links: bool = True,
    max_content_length: int = 50000,
    context: dict = None
) -> dict:
    """
    Scrape content from a URL for research analysis.
    """
    import aiohttp
    from urllib.parse import urlparse, urljoin

    logger.info(f"Scraping URL for research: {url}")

    try:
        headers = {
            "User-Agent": random.choice(DEFAULT_USER_AGENTS),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, timeout=30) as response:
                if response.status != 200:
                    return {
                        'success': False,
                        'url': url,
                        'error': f"HTTP {response.status}",
                        'status_code': response.status
                    }

                content = await response.text()
                content_type = response.headers.get('content-type', '').lower()

                # Process the response
                result = _process_html_content(url, content, extract_links, max_content_length)
                result['status_code'] = response.status
                result['content_type'] = content_type
                result['success'] = True

                return result

    except Exception as e:
        logger.error(f"Scraping failed for {url}: {e}")
        return {
            'success': False,
            'url': url,
            'error': str(e)
        }


def _process_html_content(url: str, html: str, extract_links: bool, max_length: int) -> dict:
    """Process HTML content and extract research-relevant information."""
    from urllib.parse import urlparse, urljoin

    try:
        from bs4 import BeautifulSoup
    except ImportError:
        return {
            'url': url,
            'title': 'BeautifulSoup not available',
            'text': html[:max_length],
            'research_quality': 'unknown',
            'error': 'BeautifulSoup not installed'
        }

    soup = BeautifulSoup(html, 'html.parser')

    # Extract title
    title = soup.title.string if soup.title else "No title found"

    # Extract main content
    text_content = _extract_main_content(soup)

    # Extract links if requested
    links = []
    if extract_links:
        links = _extract_links(soup, url)

    # Assess research quality
    research_quality = _assess_research_quality(text_content, url)

    return {
        'url': url,
        'title': title,
        'text': text_content[:max_length],
        'text_length': len(text_content),
        'links': links[:30],  # Limit links
        'link_count': len(links),
        'research_quality': research_quality,
        'timestamp': datetime.now().isoformat()
    }


def _extract_main_content(soup) -> str:
    """Extract main text content from HTML."""
    # Remove script and style elements
    for element in soup(['script', 'style', 'nav', 'footer', 'header', 'aside']):
        element.decompose()

    # Try to find main content areas
    main_content = soup.find('main') or soup.find('article') or soup.find('div', class_='content')

    if main_content:
        text_elements = main_content.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li'])
    else:
        text_elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li'])

    text_content = ""
    for element in text_elements:
        if element.text.strip():
            text_content += element.text.strip() + "\n\n"

    return text_content


def _extract_links(soup, base_url: str) -> List[Dict[str, str]]:
    """Extract links from HTML content."""
    from urllib.parse import urljoin

    links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        text = link.get_text(strip=True)

        if href and not href.startswith(('javascript:', '#', 'mailto:')):
            try:
                abs_url = urljoin(base_url, href)
                links.append({
                    "url": abs_url,
                    "text": text or "No text",
                })
            except Exception:
                pass

    return links


def _assess_research_quality(content: str, url: str) -> str:
    """Assess the research quality of the content."""
    if not content:
        return "low"

    # Quality indicators by domain
    quality_domains = {
        "high": [".gov", ".edu", "scholar.google", "pubmed", "arxiv", ".mil",
                 "ffiec.gov", "federalreserve.gov", "sec.gov"],
        "medium": ["wikipedia", "reuters", "bloomberg", "wsj.com", "ft.com",
                   "documentation", "docs.", "api.", "developer."],
        "low": []  # Default
    }

    url_lower = url.lower()

    # Check URL quality
    for domain in quality_domains["high"]:
        if domain in url_lower:
            return "high"

    for domain in quality_domains["medium"]:
        if domain in url_lower:
            return "medium"

    # Check content quality indicators
    content_lower = content.lower()
    quality_indicators = ["overview", "summary", "conclusion", "requirements",
                         "methodology", "analysis", "research", "study"]

    indicator_count = sum(1 for indicator in quality_indicators if indicator in content_lower)

    # Length and structure assessment
    score = 0
    if len(content) > 5000:
        score += 1
    if len(content) > 10000:
        score += 1
    if indicator_count >= 3:
        score += 1
    if indicator_count >= 5:
        score += 1

    if score >= 3:
        return "high"
    elif score >= 1:
        return "medium"
    else:
        return "low"
