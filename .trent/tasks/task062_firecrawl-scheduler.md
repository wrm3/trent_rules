---
id: 62
title: 'Create Firecrawl scheduler.py (weekly cron, diff, commit, RAG ingest)'
type: feature
status: pending
priority: high
phase: 0
subsystems: [platform-docs]
ai_safe: false
blast_radius: medium
requires_verification: true
requires_solo_agent: false
dependencies: [61]
project_context: 'scheduler.py is the automation layer — runs weekly, triggers crawls, ingests diffs into RAG, commits changelog updates to git; the living documentation system depends on this running reliably'
---

# Task 062: Create Firecrawl scheduler.py

## Objective
Create `template_v2/docker/firecrawl/scheduler.py` — the scheduled runner that orchestrates weekly crawls, processes diffs, ingests changes into the RAG system, and commits platform changelog updates to git.

## Scheduler Workflow

```python
"""
Firecrawl Scheduler
Runs weekly (or on-demand), orchestrates the full platform docs update pipeline:
crawler → diff → RAG ingest → git commit → notification
"""

def run_weekly_update():
    """Main scheduled function — runs every Sunday 03:00 UTC"""
    
    # 1. Run crawler for all targets
    results = crawler.crawl_all_targets()
    
    # 2. Compute diffs
    diffs = [crawler.compute_diff(r.target_id, r) for r in results]
    
    # 3. Skip targets with no changes
    changed = [d for d in diffs if d.changed_count > 0]
    
    # 4. Ingest changed pages into RAG
    for diff in changed:
        rag_chunks = crawler.prepare_rag_input(diff.target_id, diff)
        rag_client.ingest_batch(rag_chunks, subject=f"platform_docs_{diff.target_id}")
    
    # 5. Update .platforms/ changelog
    update_platform_changelog(changed)
    
    # 6. Git commit the changes
    git_commit_platform_update(changed)
    
    # 7. Write update report
    write_update_report(changed)
```

## Key Functions

```python
def update_platform_changelog(diffs: list[DiffResult]):
    """Update .platforms/CHANGELOG.md with summary of changes found"""
    ...

def git_commit_platform_update(diffs: list[DiffResult]):
    """Commit crawled content and changelog to git"""
    commit_msg = f"""docs(platforms): weekly platform docs update {date}
    
Changed platforms: {[d.target_id for d in diffs]}
Pages changed: {sum(len(d.changed_pages) for d in diffs)}
Pages added: {sum(len(d.new_pages) for d in diffs)}

Agent: firecrawl-scheduler
Rules-Version: {RULES_VERSION}"""
    ...

def write_update_report(diffs: list[DiffResult]) -> str:
    """Write human-readable update report to docker/firecrawl/LAST_UPDATE.md"""
    ...
```

## Schedule Configuration (in docker-compose or config.yaml)

```yaml
schedule:
  enabled: true
  cron: "0 3 * * 0"    # Sunday 3am UTC
  timezone: "UTC"
  on_startup_crawl: false  # Don't crawl on container start
  force_crawl_on_demand: true  # Allow manual trigger via HTTP POST /crawl
```

## HTTP Trigger Endpoint

```
POST /crawl
  body: { "target": "cursor" | "claude" | "gemini" | "all" }
  response: { "job_id": "...", "status": "queued" }

GET /status
  response: { "last_crawl": "...", "next_scheduled": "...", "jobs_running": [] }
```

## Acceptance Criteria
- [ ] `template_v2/docker/firecrawl/scheduler.py` exists
- [ ] `run_weekly_update()` function with 7-step workflow
- [ ] `update_platform_changelog()` function
- [ ] `git_commit_platform_update()` function with correct commit format
- [ ] HTTP endpoint for manual trigger (`POST /crawl`)
- [ ] Schedule config in `config.yaml`
- [ ] Graceful error handling: single target failure doesn't stop other targets
- [ ] `LAST_UPDATE.md` written after each run

## Verification Steps
- [ ] File exists at correct path
- [ ] `run_weekly_update()` has all 7 steps
- [ ] git commit format includes `docs(platforms):` prefix and agent footer
- [ ] HTTP trigger endpoint defined
- [ ] Error isolation (one target failure doesn't break others)

## When Stuck
- task061 (crawler.py) is prerequisite — needs the `PlatformDocCrawler` class
- For RAG ingestion client: look at existing `_trent_shared.py` for pattern
- APScheduler library: `pip install apscheduler`
