# IDEA_BOARD.md

> **Parking lot for ideas not yet ready for development.**
> Capture freely — evaluate deliberately — promote intentionally.

---

## Active Ideas

<!-- Add new ideas here. Use next available IDEA-NNN ID. -->
<!-- AI: capture immediately when user says "make note of this", "idea:", "remember this", etc. -->

### IDEA-001: Rename rag_* to knowledge_* across the codebase
**Status**: raw
**Category**: technical
**Captured**: 2026-03-06
**Source**: user

**Description**:
The `rag_*` naming (RAG_SUBJECT env var, rag_ingest_page() function, POSTGRES_DB=rag_knowledge, rag_search tool) predates the current memory system and creates confusion — "RAG" was associated with the removed Perplexity research tools in users' minds, but it actually refers to the active PostgreSQL/pgvector knowledge store. Rename to `knowledge_*` throughout for clarity.

**Potential Value**:
Removes a persistent source of confusion for new teammates and project owners. Makes it immediately clear that the knowledge store is the active memory/search infrastructure, not the old research tools that were removed.

**When Ready**:
Low priority cosmetic cleanup. Good candidate for a quiet maintenance sprint when no active feature work is in flight. Requires touching: env vars (POSTGRES_DB, RAG_SUBJECT), function names in scheduler.py and plugins, DB name migration or alias, and .env.example documentation.

**Notes**:
Scope: docker/firecrawl/scheduler.py, docker/trent/tools/plugins/rag_search.py (if exists), .env / .env.example, docker-compose.yml, any rules that reference "RAG" as a feature name. DB rename requires a migration script or just documenting it as a breaking change in the migration guide.

---

## Promoted Ideas

<!-- Ideas that were accepted and converted to tasks or phases. -->
<!-- Format: ### IDEA-NNN: [Title] → Task #{ID} / Phase {N} -->

---

## Shelved Ideas

<!-- Ideas consciously decided not to pursue right now. Keep for context. -->
<!-- Format: same as Active, plus **Shelved Reason**: [why] -->

---

## Idea Template

```markdown
### IDEA-{NNN}: [Short descriptive title]
**Status**: raw
**Category**: feature | monetization | ux | technical | architecture | business
**Captured**: YYYY-MM-DD
**Source**: user | AI | session

**Description**:
[The idea in 1-3 sentences. Be specific enough to reconstruct intent later.]

**Potential Value**:
[Why this is worth keeping — problem it solves, revenue potential, UX improvement, etc.]

**When Ready**:
[What prerequisites, milestones, or triggers would make this worth developing?]

**Notes**:
[Additional context, related ideas, implementation hints]
```

---

## Idea Lifecycle Reference

| Status | Meaning | Action |
|--------|---------|--------|
| `raw` | Just captured | No action needed yet |
| `evaluating` | Under active consideration | Discuss with team/AI |
| `accepted` | Approved for development | Create task/phase, update status |
| `shelved` | Not pursuing now | Add shelved reason, move to Shelved section |

---

## Category Reference

| Category | Examples |
|----------|---------|
| `feature` | New user-facing capability |
| `monetization` | Pricing, upsells, revenue model |
| `ux` | UX/UI improvements, flows |
| `technical` | Architecture, refactoring, performance |
| `architecture` | System design, integration patterns |
| `business` | Business model, partnerships, strategy |
