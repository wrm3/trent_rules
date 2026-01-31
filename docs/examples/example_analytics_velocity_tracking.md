# Example: Task Velocity and Phase Health Analytics

**This example demonstrates analytics and reporting capabilities for tracking project health.**

---

## Task Velocity Tracking

### Weekly Velocity Report

**Week of 2026-01-20 to 2026-01-27**

| Metric | Value | Trend |
|--------|-------|-------|
| **Tasks Completed** | 12 | ↑ +2 from last week |
| **Average Completion Time** | 1.8 days | ↓ -0.3 days |
| **Tasks Created** | 8 | → Same as last week |
| **Tasks In Progress** | 5 | ↓ -1 from last week |
| **Blocked Tasks** | 1 | → Same as last week |
| **Velocity (tasks/week)** | 12 | ↑ +2 |
| **Burndown Rate** | 85% | ↑ +5% |

### Velocity Chart

```
Tasks Completed per Week
│
15│                    ●
  │                 ●
10│              ●     ●
  │           ●
 5│        ●
  │     ●
 0└─────────────────────────
   W1  W2  W3  W4  W5  W6
```

### Story Points Completed

**This Week**: 28 story points
- 1 SP tasks: 4 tasks
- 2 SP tasks: 3 tasks
- 3 SP tasks: 2 tasks
- 5 SP tasks: 1 task
- 8 SP tasks: 0 tasks

**Average Velocity**: 25 SP/week
**Velocity Trend**: ↑ Increasing (was 22 SP/week last month)

---

## Phase Health Dashboard

### Phase 0: Setup & Infrastructure

**Status**: ✅ **COMPLETE**

| Metric | Value | Status |
|--------|-------|--------|
| **Completion** | 100% (15/15 tasks) | ✅ |
| **Duration** | 8 days | ✅ On time |
| **Quality Score** | 4.2/5.0 | ✅ Good |
| **Technical Debt** | Low | ✅ |
| **Blockers** | 0 | ✅ |

**Health**: 🟢 **HEALTHY**

---

### Phase 1: Foundation

**Status**: 🔄 **IN PROGRESS** (85% complete)

| Metric | Value | Status |
|--------|-------|--------|
| **Completion** | 85% (17/20 tasks) | 🟡 On track |
| **Duration** | 12 days (of 14 planned) | 🟡 Slightly behind |
| **Quality Score** | 4.0/5.0 | ✅ Good |
| **Technical Debt** | Medium | 🟡 Monitor |
| **Blockers** | 1 (Task 118) | 🟡 |

**Health**: 🟡 **MONITOR**

**Issues:**
- Task 118 blocked on external dependency (API key approval)
- Some technical debt accumulating (needs refactoring)

**Actions:**
- Escalate Task 118 blocker
- Schedule refactoring sprint after Phase 1

---

### Phase 2: Core Development

**Status**: ⏸️ **PENDING** (waiting for Phase 1)

| Metric | Value | Status |
|--------|-------|--------|
| **Completion** | 0% (0/25 tasks) | ⏸️ Not started |
| **Planned Duration** | 18 days | ⏸️ |
| **Dependencies** | Phase 1 (3 tasks remaining) | ⏸️ |
| **Risk Level** | Low | ✅ |

**Health**: ⏸️ **PENDING**

---

## Task Distribution Analysis

### By Status

```
Status Distribution
│
20│                    ████
  │                    ████
15│              ████  ████
  │              ████  ████
10│        ████  ████  ████
  │        ████  ████  ████
 5│  ████  ████  ████  ████
  │  ████  ████  ████  ████
 0└─────────────────────────
   Pending Ready In-Progress Completed
```

### By Priority

| Priority | Count | Percentage |
|----------|-------|------------|
| Critical | 2 | 5% |
| High | 8 | 20% |
| Medium | 20 | 50% |
| Low | 10 | 25% |

### By Phase

| Phase | Tasks | Completed | In Progress | Pending |
|-------|-------|-----------|-------------|---------|
| Phase 0 | 15 | 15 (100%) | 0 | 0 |
| Phase 1 | 20 | 17 (85%) | 2 | 1 |
| Phase 2 | 25 | 0 (0%) | 0 | 25 |

---

## Bottleneck Analysis

### Current Bottlenecks

1. **Task 118 - API Integration** (BLOCKED)
   - **Blocker**: Waiting for external API key approval
   - **Impact**: Blocks 3 dependent tasks
   - **Action**: Escalate to project manager, find workaround

2. **Code Review Queue** (WIP LIMIT EXCEEDED)
   - **Current**: 4 tasks in review (limit: 2)
   - **Impact**: Slows task completion
   - **Action**: Increase review capacity or reduce WIP limit

3. **Testing Queue** (WIP LIMIT EXCEEDED)
   - **Current**: 3 tasks in testing (limit: 2)
   - **Impact**: Delays task completion
   - **Action**: Parallelize testing or increase capacity

---

## Predictive Analytics

### Completion Forecast

**Phase 1 Forecast:**
- **Current Progress**: 85% (17/20 tasks)
- **Remaining Tasks**: 3 tasks
- **Estimated Completion**: 2026-01-29 (2 days)
- **Confidence**: 85% (based on current velocity)

**Phase 2 Forecast:**
- **Planned Start**: 2026-01-30
- **Estimated Completion**: 2026-02-17 (18 days)
- **Confidence**: 70% (depends on Phase 1 completion)

### Risk Indicators

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Phase 1 delay | Medium | High | Escalate blockers, add resources |
| Technical debt | High | Medium | Schedule refactoring sprint |
| Scope creep | Low | Medium | Enforce phase gates |
| Resource availability | Low | High | Cross-train team members |

---

## Quality Metrics

### Bug Rate

- **Bugs Found**: 3 this week
- **Bugs Fixed**: 3 this week
- **Bug Rate**: 0.25 bugs per task (target: <0.3)
- **Fix Time**: Average 1.2 days (target: <2 days)

### Code Quality

- **Test Coverage**: 85% (target: 90%)
- **Code Review Time**: Average 4 hours (target: <8 hours)
- **Technical Debt**: Medium (target: Low)
- **Documentation**: 80% complete (target: 90%)

---

## Recommendations

### Immediate Actions
1. **Escalate Task 118 blocker** - External dependency blocking progress
2. **Reduce review queue** - Current WIP limit exceeded
3. **Schedule refactoring** - Technical debt accumulating

### Short-Term Improvements
1. **Increase test coverage** - Target 90% by Phase 2
2. **Improve documentation** - Target 90% completion
3. **Optimize review process** - Reduce review time

### Long-Term Enhancements
1. **Automate reporting** - Generate analytics automatically
2. **Predictive modeling** - Better completion forecasts
3. **Quality gates** - Automated quality checks

---

**This analytics example demonstrates:**
1. **Velocity Tracking**: Weekly completion rates and trends
2. **Phase Health**: Comprehensive phase status monitoring
3. **Bottleneck Detection**: Identification of workflow issues
4. **Predictive Analytics**: Completion forecasts and risk assessment
5. **Quality Metrics**: Bug rates, test coverage, code quality
