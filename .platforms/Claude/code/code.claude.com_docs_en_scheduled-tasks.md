[Skip to main content](https://code.claude.com/docs/en/scheduled-tasks#content-area)

[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/light.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=d535f2e20f53cd911acc59ad1b64b2e0)![dark logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/dark.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=28e49a2ffe69101f4aae9bfa70b393d0)](https://code.claude.com/docs)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Build with Claude Code

Run prompts on a schedule

[Getting started](https://code.claude.com/docs/en/overview) [Build with Claude Code](https://code.claude.com/docs/en/sub-agents) [Deployment](https://code.claude.com/docs/en/third-party-integrations) [Administration](https://code.claude.com/docs/en/setup) [Configuration](https://code.claude.com/docs/en/settings) [Reference](https://code.claude.com/docs/en/cli-reference) [Resources](https://code.claude.com/docs/en/legal-and-compliance)

On this page

- [Schedule a recurring prompt with /loop](https://code.claude.com/docs/en/scheduled-tasks#schedule-a-recurring-prompt-with-%2Floop)
- [Interval syntax](https://code.claude.com/docs/en/scheduled-tasks#interval-syntax)
- [Loop over another command](https://code.claude.com/docs/en/scheduled-tasks#loop-over-another-command)
- [Set a one-time reminder](https://code.claude.com/docs/en/scheduled-tasks#set-a-one-time-reminder)
- [Manage scheduled tasks](https://code.claude.com/docs/en/scheduled-tasks#manage-scheduled-tasks)
- [How scheduled tasks run](https://code.claude.com/docs/en/scheduled-tasks#how-scheduled-tasks-run)
- [Jitter](https://code.claude.com/docs/en/scheduled-tasks#jitter)
- [Three-day expiry](https://code.claude.com/docs/en/scheduled-tasks#three-day-expiry)
- [Cron expression reference](https://code.claude.com/docs/en/scheduled-tasks#cron-expression-reference)
- [Disable scheduled tasks](https://code.claude.com/docs/en/scheduled-tasks#disable-scheduled-tasks)
- [Limitations](https://code.claude.com/docs/en/scheduled-tasks#limitations)

Scheduled tasks let Claude re-run a prompt automatically on an interval. Use them to poll a deployment, babysit a PR, check back on a long-running build, or remind yourself to do something later in the session.Tasks are session-scoped: they live in the current Claude Code process and are gone when you exit. For durable scheduling that survives restarts and runs without an active terminal session, see [Desktop scheduled tasks](https://code.claude.com/docs/en/desktop#schedule-recurring-tasks) or [GitHub Actions](https://code.claude.com/docs/en/github-actions).

## [​](https://code.claude.com/docs/en/scheduled-tasks\#schedule-a-recurring-prompt-with-/loop)  Schedule a recurring prompt with /loop

The `/loop` [bundled skill](https://code.claude.com/docs/en/skills#bundled-skills) is the quickest way to schedule a recurring prompt. Pass an optional interval and a prompt, and Claude sets up a cron job that fires in the background while the session stays open.

Report incorrect code

Copy

Ask AI

```
/loop 5m check if the deployment finished and tell me what happened
```

Claude parses the interval, converts it to a cron expression, schedules the job, and confirms the cadence and job ID.

### [​](https://code.claude.com/docs/en/scheduled-tasks\#interval-syntax)  Interval syntax

Intervals are optional. You can lead with them, trail with them, or leave them out entirely.

| Form | Example | Parsed interval |
| --- | --- | --- |
| Leading token | `/loop 30m check the build` | every 30 minutes |
| Trailing `every` clause | `/loop check the build every 2 hours` | every 2 hours |
| No interval | `/loop check the build` | defaults to every 10 minutes |

Supported units are `s` for seconds, `m` for minutes, `h` for hours, and `d` for days. Seconds are rounded up to the nearest minute since cron has one-minute granularity. Intervals that don’t divide evenly into their unit, such as `7m` or `90m`, are rounded to the nearest clean interval and Claude tells you what it picked.

### [​](https://code.claude.com/docs/en/scheduled-tasks\#loop-over-another-command)  Loop over another command

The scheduled prompt can itself be a command or skill invocation. This is useful for re-running a workflow you’ve already packaged.

Report incorrect code

Copy

Ask AI

```
/loop 20m /review-pr 1234
```

Each time the job fires, Claude runs `/review-pr 1234` as if you had typed it.

## [​](https://code.claude.com/docs/en/scheduled-tasks\#set-a-one-time-reminder)  Set a one-time reminder

For one-shot reminders, describe what you want in natural language instead of using `/loop`. Claude schedules a single-fire task that deletes itself after running.

Report incorrect code

Copy

Ask AI

```
remind me at 3pm to push the release branch
```

Report incorrect code

Copy

Ask AI

```
in 45 minutes, check whether the integration tests passed
```

Claude pins the fire time to a specific minute and hour using a cron expression and confirms when it will fire.

## [​](https://code.claude.com/docs/en/scheduled-tasks\#manage-scheduled-tasks)  Manage scheduled tasks

Ask Claude in natural language to list or cancel tasks, or reference the underlying tools directly.

Report incorrect code

Copy

Ask AI

```
what scheduled tasks do I have?
```

Report incorrect code

Copy

Ask AI

```
cancel the deploy check job
```

Under the hood, Claude uses these tools:

| Tool | Purpose |
| --- | --- |
| `CronCreate` | Schedule a new task. Accepts a 5-field cron expression, the prompt to run, and whether it recurs or fires once. |
| `CronList` | List all scheduled tasks with their IDs, schedules, and prompts. |
| `CronDelete` | Cancel a task by ID. |

Each scheduled task has an 8-character ID you can pass to `CronDelete`. A session can hold up to 50 scheduled tasks at once.

## [​](https://code.claude.com/docs/en/scheduled-tasks\#how-scheduled-tasks-run)  How scheduled tasks run

The scheduler checks every second for due tasks and enqueues them at low priority. A scheduled prompt fires between your turns, not while Claude is mid-response. If Claude is busy when a task comes due, the prompt waits until the current turn ends.All times are interpreted in your local timezone. A cron expression like `0 9 * * *` means 9am wherever you’re running Claude Code, not UTC.

### [​](https://code.claude.com/docs/en/scheduled-tasks\#jitter)  Jitter

To avoid every session hitting the API at the same wall-clock moment, the scheduler adds a small deterministic offset to fire times:

- Recurring tasks fire up to 10% of their period late, capped at 15 minutes. An hourly job might fire anywhere from `:00` to `:06`.
- One-shot tasks scheduled for the top or bottom of the hour fire up to 90 seconds early.

The offset is derived from the task ID, so the same task always gets the same offset. If exact timing matters, pick a minute that is not `:00` or `:30`, for example `3 9 * * *` instead of `0 9 * * *`, and the one-shot jitter will not apply.

### [​](https://code.claude.com/docs/en/scheduled-tasks\#three-day-expiry)  Three-day expiry

Recurring tasks automatically expire 3 days after creation. The task fires one final time, then deletes itself. This bounds how long a forgotten loop can run. If you need a recurring task to last longer, cancel and recreate it before it expires, or use [Desktop scheduled tasks](https://code.claude.com/docs/en/desktop#schedule-recurring-tasks) for durable scheduling.

## [​](https://code.claude.com/docs/en/scheduled-tasks\#cron-expression-reference)  Cron expression reference

`CronCreate` accepts standard 5-field cron expressions: `minute hour day-of-month month day-of-week`. All fields support wildcards (`*`), single values (`5`), steps (`*/15`), ranges (`1-5`), and comma-separated lists (`1,15,30`).

| Example | Meaning |
| --- | --- |
| `*/5 * * * *` | Every 5 minutes |
| `0 * * * *` | Every hour on the hour |
| `7 * * * *` | Every hour at 7 minutes past |
| `0 9 * * *` | Every day at 9am local |
| `0 9 * * 1-5` | Weekdays at 9am local |
| `30 14 15 3 *` | March 15 at 2:30pm local |

Day-of-week uses `0` or `7` for Sunday through `6` for Saturday. Extended syntax like `L`, `W`, `?`, and name aliases such as `MON` or `JAN` is not supported.When both day-of-month and day-of-week are constrained, a date matches if either field matches. This follows standard vixie-cron semantics.

## [​](https://code.claude.com/docs/en/scheduled-tasks\#disable-scheduled-tasks)  Disable scheduled tasks

Set `CLAUDE_CODE_DISABLE_CRON=1` in your environment to disable the scheduler entirely. The cron tools and `/loop` become unavailable, and any already-scheduled tasks stop firing. See [Environment variables](https://code.claude.com/docs/en/settings#environment-variables) for the full list of disable flags.

## [​](https://code.claude.com/docs/en/scheduled-tasks\#limitations)  Limitations

Session-scoped scheduling has inherent constraints:

- Tasks only fire while Claude Code is running and idle. Closing the terminal or letting the session exit cancels everything.
- No catch-up for missed fires. If a task’s scheduled time passes while Claude is busy on a long-running request, it fires once when Claude becomes idle, not once per missed interval.
- No persistence across restarts. Restarting Claude Code clears all session-scoped tasks.

For cron-driven automation that needs to run unattended, use a [GitHub Actions workflow](https://code.claude.com/docs/en/github-actions) with a `schedule` trigger, or [Desktop scheduled tasks](https://code.claude.com/docs/en/desktop#schedule-recurring-tasks) if you want a graphical setup flow.

Was this page helpful?

YesNo

[Extend Claude with skills](https://code.claude.com/docs/en/skills) [Output styles](https://code.claude.com/docs/en/output-styles)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.