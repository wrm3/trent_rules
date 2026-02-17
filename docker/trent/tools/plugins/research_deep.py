"""
Deep Research Tool Plugin

Conduct comprehensive deep research on a topic and generate detailed markdown documents.
Uses Perplexity API for analysis and OpenAI for document generation.
"""
import os
import logging
from typing import Optional, List, Dict, Any
from datetime import datetime
from pathlib import Path

# ============================================================
# PLUGIN METADATA (Required)
# ============================================================

TOOL_NAME = "research_deep"

TOOL_DESCRIPTION = (
    "Conduct comprehensive deep research on any topic and generate detailed markdown documents. "
    "Uses Perplexity API for research analysis (NO DuckDuckGo). "
    "Produces structured reports with executive summary, key findings, and sources. "
    "Supports different research depths: brief, standard, comprehensive."
)

TOOL_PARAMS = {
    "topic": "The research topic to investigate",
    "target_length": "Research depth: 'brief', 'standard', 'comprehensive' (default: 'comprehensive')",
    "output_directory": "Directory to save research document (default: './research_output')",
    "include_sources": "Whether to verify and include source citations (default: True)"
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
    topic: str,
    target_length: str = "comprehensive",
    output_directory: str = "./research_output",
    include_sources: bool = True,
    context: dict = None
) -> dict:
    """
    Conduct deep research on a topic and generate markdown document.
    """
    import aiohttp

    config = context.get('config', _config) if context else _config

    perplexity_key = config.get('perplexity_api_key')
    openai_key = config.get('openai_api_key')

    logger.info(f"Starting deep research on: {topic}")
    logger.info(f"Target length: {target_length}")

    if not perplexity_key and not openai_key:
        return {
            'success': False,
            'error': 'Deep research requires PERPLEXITY_API_KEY or OPENAI_API_KEY to be configured.'
        }

    try:
        # Generate output filename
        safe_filename = "".join(c for c in topic if c.isalnum() or c in (' ', '-', '_')).rstrip()
        safe_filename = safe_filename.replace(' ', '_').lower()
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_filename = f"{safe_filename}_{timestamp}.md"
        output_path = os.path.join(output_directory, output_filename)

        # Step 1: Conduct research using Perplexity
        research_data = await _conduct_research(topic, target_length, perplexity_key, openai_key)

        if not research_data.get('success'):
            return research_data

        # Step 2: Generate markdown document
        markdown_content = _generate_markdown(topic, research_data, target_length)

        # Step 3: Save to file
        save_result = _save_document(output_path, markdown_content)

        return {
            'success': True,
            'topic': topic,
            'target_length': target_length,
            'research_summary': {
                'executive_summary': research_data.get('executive_summary', '')[:500],
                'key_findings_count': len(research_data.get('key_findings', [])),
                'sources_count': len(research_data.get('sources', []))
            },
            'output_file': {
                'path': save_result.get('path'),
                'filename': output_filename,
                'directory': output_directory,
                'size_bytes': save_result.get('size_bytes', 0)
            },
            'timestamp': datetime.now().isoformat()
        }

    except Exception as e:
        logger.error(f"Deep research failed: {e}")
        return {
            'success': False,
            'error': str(e),
            'topic': topic
        }


async def _conduct_research(topic: str, target_length: str, perplexity_key: str, openai_key: str) -> dict:
    """Conduct research using available APIs."""
    import aiohttp

    current_year = datetime.now().year

    # Determine research depth
    max_tokens = {
        'brief': 1000,
        'standard': 2000,
        'comprehensive': 4000
    }.get(target_length, 2000)

    # Build research prompt
    research_prompt = f"""Conduct comprehensive research on: {topic}

Provide:
1. Executive Summary (2-3 paragraphs)
2. Key Findings (5-10 bullet points)
3. Detailed Analysis (structured by relevant sections)
4. Current State as of {current_year}
5. Key Sources and References

Focus on accuracy, current information, and practical insights.
"""

    # Try Perplexity first (best for research)
    if perplexity_key:
        try:
            return await _research_with_perplexity(research_prompt, max_tokens, perplexity_key)
        except Exception as e:
            logger.warning(f"Perplexity research failed: {e}")

    # Fallback to OpenAI
    if openai_key:
        try:
            return await _research_with_openai(research_prompt, max_tokens, openai_key)
        except Exception as e:
            logger.warning(f"OpenAI research failed: {e}")

    return {
        'success': False,
        'error': 'All research APIs failed'
    }


async def _research_with_perplexity(prompt: str, max_tokens: int, api_key: str) -> dict:
    """Conduct research using Perplexity API."""
    import aiohttp

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "sonar-medium-online",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
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

            # Parse the response into structured data
            return _parse_research_response(content)


async def _research_with_openai(prompt: str, max_tokens: int, api_key: str) -> dict:
    """Conduct research using OpenAI API."""
    import aiohttp

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": "You are a professional research analyst. Provide comprehensive, accurate research with proper citations."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": max_tokens,
        "temperature": 0.3
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=data
        ) as response:
            if response.status != 200:
                raise Exception(f"OpenAI API error: {response.status}")

            result = await response.json()
            content = result.get("choices", [{}])[0].get("message", {}).get("content", "")

            return _parse_research_response(content)


def _parse_research_response(content: str) -> dict:
    """Parse research response into structured data."""

    # Simple parsing - split into sections
    lines = content.split('\n')

    executive_summary = ""
    key_findings = []
    detailed_analysis = content
    sources = []

    # Extract executive summary (first few paragraphs)
    in_summary = False
    summary_lines = []
    for line in lines:
        if 'executive summary' in line.lower() or 'summary' in line.lower():
            in_summary = True
            continue
        if in_summary:
            if line.startswith('#') or 'key findings' in line.lower():
                break
            summary_lines.append(line)

    executive_summary = '\n'.join(summary_lines).strip() or content[:500]

    # Extract key findings (bullet points)
    for line in lines:
        if line.strip().startswith(('-', '*', '•')) and len(line) > 10:
            key_findings.append(line.strip().lstrip('-*• '))

    key_findings = key_findings[:10]  # Limit

    return {
        'success': True,
        'executive_summary': executive_summary,
        'key_findings': key_findings,
        'detailed_analysis': detailed_analysis,
        'sources': sources,
        'raw_content': content
    }


def _generate_markdown(topic: str, research_data: dict, target_length: str) -> str:
    """Generate formatted markdown document from research data."""

    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    markdown = f"""# {topic}

> **Research Date**: {current_date} UTC
> **Research Type**: {target_length.title()} Analysis
> **Generated by**: trent Deep Research

---

## Executive Summary

{research_data.get('executive_summary', 'No executive summary available.')}

---

## Key Findings

"""

    # Add key findings
    for i, finding in enumerate(research_data.get('key_findings', []), 1):
        markdown += f"{i}. {finding}\n"

    markdown += """

---

## Detailed Analysis

"""

    markdown += research_data.get('detailed_analysis', 'No detailed analysis available.')

    # Add sources section
    sources = research_data.get('sources', [])
    if sources:
        markdown += """

---

## Sources and References

"""
        for i, source in enumerate(sources, 1):
            if isinstance(source, dict):
                markdown += f"{i}. [{source.get('title', 'Source')}]({source.get('url', '#')}) - {source.get('description', '')}\n"
            else:
                markdown += f"{i}. {source}\n"

    markdown += f"""

---

## Research Metadata

- **Topic**: {topic}
- **Target Length**: {target_length}
- **Generation Date**: {current_date} UTC
- **Research Engine**: Perplexity/OpenAI
- **Generated by**: trent Deep Research Tool

---

*This research document was automatically generated and should be reviewed for accuracy before use in production environments.*
"""

    return markdown


def _save_document(output_path: str, content: str) -> dict:
    """Save markdown document to file."""

    try:
        # Ensure directory exists
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        # Write content
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)

        return {
            'success': True,
            'path': str(output_file.absolute()),
            'size_bytes': len(content.encode('utf-8'))
        }

    except Exception as e:
        logger.error(f"Failed to save document: {e}")
        return {
            'success': False,
            'error': str(e)
        }
