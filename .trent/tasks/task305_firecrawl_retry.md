---
id: 305
title: 'Firecrawl retry/backoff + zero-page alert'
type: feature
status: in-progress
priority: high
phase: 3
subsystem: firecrawl
blast_radius: low
ai_safe: true
requires_solo_agent: false
dependencies: []
created_date: "2026-03-06"
completed_date: null
rules_version: "5.1.0"
project_context: "scheduler.py fires crawls with no retry. A single network timeout silently leaves platform knowledge stale with no notification. Add exponential backoff per-page, a zero-page guard, and a crawl result written to a status file the trent_health_report can surface."
---

# Task 305: Firecrawl retry/backoff + zero-page alert

## Objective
1. Add `crawl_with_retry(page, max_attempts=3, base_delay=5)` to `scheduler.py`
2. Add zero-page guard — if total crawled pages == 0, write CRAWL_FAILED status
3. Write `.platforms/CRAWL_STATUS.json` after every run (success or fail)
4. `trent_health_report` reads CRAWL_STATUS.json and surfaces stale crawls

## Acceptance Criteria
- [ ] Page-level retry with exponential backoff (5s, 10s, 20s)
- [ ] After 3 failures on a page: log as dead-letter, continue with rest
- [ ] If 0 pages crawled total: write status `failed`, log ERROR
- [ ] CRAWL_STATUS.json written every run with: date, pages_crawled, pages_failed, status
- [ ] trent_health_report reads CRAWL_STATUS.json and adds warning if > 14 days stale
