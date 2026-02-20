---
description: "Always be aware of the current date and time for accurate responses"
activation: "always_on"
---

# Current Date/Time Awareness Rule

## Purpose

Ensure the AI assistant is aware of the actual current date/time (not training cutoff) and proactively researches current information for time-sensitive queries.

## Current Date Awareness

**CRITICAL**: The current date is provided in the system context as "Today's date" in the user_info section. ALWAYS use this date, NOT your training data cutoff date.

### How to Determine Current Date

1. **Check user_info**: Look for `Today's date:` in the system context
2. **If not available**: Ask the user or use shell command:
   ```powershell
   Get-Date -Format "yyyy-MM-dd HH:mm:ss"
   ```

### Training Data Limitations

| Model | Approximate Training Cutoff | Knowledge Gap |
|-------|----------------------------|---------------|
| Claude 3.5 | Early 2024 | ~2 years |
| Claude 3 Opus | Early 2024 | ~2 years |
| GPT-4 | April 2023 | ~3 years |
| GPT-4 Turbo | December 2023 | ~2 years |

**Your training data is likely 1-3 years old. Always verify current information.**

## When to Research

### ALWAYS Research For:

```
□ Current versions of software/libraries/frameworks
□ Latest API documentation or endpoints
□ Current pricing (cloud services, APIs, subscriptions)
□ Recent security vulnerabilities or patches
□ Current best practices (may have evolved)
□ Active GitHub repositories (stars, last commit, issues)
□ Current company information (funding, employees, status)
□ Recent news or announcements
□ Current legal/regulatory requirements
□ Live service status or availability
```

### Time-Sensitive Query Indicators

Watch for these keywords/phrases that indicate current information is needed:

```
- "latest", "current", "newest", "recent"
- "now", "today", "this year", "2025", "2026"
- "best [tool/library/framework] for..."
- "is [X] still [active/maintained/recommended]?"
- "what's the current version of..."
- "has [X] changed..."
- "up to date", "modern", "state of the art"
- Version numbers (check if newer exists)
- Pricing questions
- API documentation requests
```

### Research Decision Tree

```
Is the query time-sensitive?
├── Yes: Is the information likely >6 months old?
│   ├── Yes: MUST research before answering
│   │   └── Use WebSearch or check official docs
│   └── No: Provide answer, note it may be outdated
└── No: Use training knowledge (still note date if relevant)
```

## How to Research

### Available Tools

1. **WebSearch**: For general current information
   ```
   WebSearch: "Python 3.12 new features 2024"
   WebSearch: "React 19 release date"
   WebSearch: "AWS Lambda pricing 2026"
   ```

2. **WebFetch**: For specific documentation URLs
   ```
   WebFetch: "https://docs.python.org/3/whatsnew/3.12.html"
   ```

3. **MCP Research Tools** (if available):
   ```
   research_query: Deep research via Perplexity/Google
   web_fetch: Fetch and extract web content
   ```

### Research Best Practices

```
1. State your knowledge cutoff:
   "My training data is from early 2024, so let me verify..."

2. Research before answering:
   - Don't guess at current versions
   - Don't assume APIs haven't changed
   - Don't assume pricing is still accurate

3. Cite sources:
   "According to the official docs as of [date]..."
   "Based on the current GitHub repository..."

4. Note uncertainty:
   "This was accurate as of my research, but verify for critical decisions"
```

## Response Patterns

### When You Have Current Information

```markdown
Based on the current documentation (verified [today's date]):
- [Current information]
- [Source/link if available]
```

### When Research Is Needed

```markdown
My training data is from [cutoff date], which is [X months/years] old.
Let me research the current information...

[Perform WebSearch/WebFetch]

Current information as of [today's date]:
- [Researched facts]
- Source: [URL]
```

### When Research Fails

```markdown
I attempted to verify current information but couldn't access [source].
Based on my training data from [cutoff]:
- [Information with caveat]

⚠️ Please verify this is still accurate, as it may be outdated.
```

## Examples

### Example 1: Version Question

**User**: "What's the latest version of Node.js?"

**Bad Response**: "Node.js 20 is the latest LTS version."

**Good Response**: 
```
Let me check the current Node.js versions...
[WebSearch: "Node.js current version 2026"]

As of today (2026-02-01):
- Current LTS: Node.js 22.x
- Current: Node.js 23.x
- Source: nodejs.org
```

### Example 2: Library Recommendation

**User**: "What's the best React state management library?"

**Bad Response**: "Redux is the most popular choice."

**Good Response**:
```
My training data is from early 2024. Let me research current recommendations...
[WebSearch: "best React state management 2026"]

Current landscape (2026):
- Zustand: Lightweight, popular for new projects
- Jotai: Atomic state management
- Redux Toolkit: Still widely used in enterprise
- TanStack Query: For server state

The ecosystem evolves quickly - check npm trends for latest adoption rates.
```

### Example 3: API Documentation

**User**: "How do I use the OpenAI API?"

**Good Response**:
```
Let me fetch the current OpenAI API documentation...
[WebFetch: "https://platform.openai.com/docs/api-reference"]

Current API (as of 2026-02-01):
- Latest model: [current model]
- Endpoint: https://api.openai.com/v1/chat/completions
- [Current code example]

Note: OpenAI updates their API frequently. Always check the official docs.
```

## Self-Check Questions

Before answering time-sensitive queries, ask yourself:

```
□ What is today's actual date? (Check user_info)
□ When was my training data cutoff?
□ Is this information likely to have changed?
□ Should I research before answering?
□ Have I clearly stated any uncertainty?
□ Did I provide sources for current information?
```

## Integration with Other Rules

- **00_always.mdc**: Include current timestamp in responses
- **Research skills**: Use research-methodology skill for deep research
- **MCP tools**: Use available research MCP tools when appropriate

---

*This rule ensures accurate, current information is provided rather than potentially outdated training data.*
