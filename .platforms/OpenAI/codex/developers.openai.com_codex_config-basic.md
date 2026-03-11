## Search the Codex docs

Close

Clear

Primary navigation

Clear

### Getting Started

- [Overview](https://developers.openai.com/codex)
- [Quickstart](https://developers.openai.com/codex/quickstart)
- [Explore](https://developers.openai.com/codex/explore)
- [Pricing](https://developers.openai.com/codex/pricing)
- Concepts

  - [Prompting](https://developers.openai.com/codex/prompting)
  - [Customization](https://developers.openai.com/codex/concepts/customization)
  - [Sandboxing](https://developers.openai.com/codex/concepts/sandboxing)
  - [Multi-agents](https://developers.openai.com/codex/concepts/multi-agents)
  - [Workflows](https://developers.openai.com/codex/workflows)
  - [Models](https://developers.openai.com/codex/models)
  - [Cyber Safety](https://developers.openai.com/codex/concepts/cyber-safety)

### Using Codex

- App

  - [Overview](https://developers.openai.com/codex/app)
  - [Features](https://developers.openai.com/codex/app/features)
  - [Settings](https://developers.openai.com/codex/app/settings)
  - [Review](https://developers.openai.com/codex/app/review)
  - [Automations](https://developers.openai.com/codex/app/automations)
  - [Worktrees](https://developers.openai.com/codex/app/worktrees)
  - [Local Environments](https://developers.openai.com/codex/app/local-environments)
  - [Commands](https://developers.openai.com/codex/app/commands)
  - [Windows](https://developers.openai.com/codex/app/windows)
  - [Troubleshooting](https://developers.openai.com/codex/app/troubleshooting)

- IDE Extension

  - [Overview](https://developers.openai.com/codex/ide)
  - [Features](https://developers.openai.com/codex/ide/features)
  - [Settings](https://developers.openai.com/codex/ide/settings)
  - [IDE Commands](https://developers.openai.com/codex/ide/commands)
  - [Slash commands](https://developers.openai.com/codex/ide/slash-commands)

- CLI

  - [Overview](https://developers.openai.com/codex/cli)
  - [Features](https://developers.openai.com/codex/cli/features)
  - [Command Line Options](https://developers.openai.com/codex/cli/reference)
  - [Slash commands](https://developers.openai.com/codex/cli/slash-commands)

- Web

  - [Overview](https://developers.openai.com/codex/cloud)
  - [Environments](https://developers.openai.com/codex/cloud/environments)
  - [Internet Access](https://developers.openai.com/codex/cloud/internet-access)

- Integrations

  - [GitHub](https://developers.openai.com/codex/integrations/github)
  - [Slack](https://developers.openai.com/codex/integrations/slack)
  - [Linear](https://developers.openai.com/codex/integrations/linear)

- Codex Security

  - [Overview](https://developers.openai.com/codex/security)
  - [Setup](https://developers.openai.com/codex/security/setup)
  - [Improving the threat model](https://developers.openai.com/codex/security/threat-model)
  - [FAQ](https://developers.openai.com/codex/security/faq)

### Configuration

- Config File

  - [Config Basics](https://developers.openai.com/codex/config-basic)
  - [Advanced Config](https://developers.openai.com/codex/config-advanced)
  - [Config Reference](https://developers.openai.com/codex/config-reference)
  - [Sample Config](https://developers.openai.com/codex/config-sample)

- [Speed](https://developers.openai.com/codex/speed)
- [Rules](https://developers.openai.com/codex/rules)
- [AGENTS.md](https://developers.openai.com/codex/guides/agents-md)
- [MCP](https://developers.openai.com/codex/mcp)
- [Skills](https://developers.openai.com/codex/skills)
- [Multi-agents](https://developers.openai.com/codex/multi-agent)

### Administration

- [Authentication](https://developers.openai.com/codex/auth)
- [Agent approvals & security](https://developers.openai.com/codex/agent-approvals-security)
- Enterprise

  - [Admin Setup](https://developers.openai.com/codex/enterprise/admin-setup)
  - [Governance](https://developers.openai.com/codex/enterprise/governance)
  - [Managed configuration](https://developers.openai.com/codex/enterprise/managed-configuration)

- [Windows](https://developers.openai.com/codex/windows)

### Automation

- [Non-interactive Mode](https://developers.openai.com/codex/noninteractive)
- [Codex SDK](https://developers.openai.com/codex/sdk)
- [App Server](https://developers.openai.com/codex/app-server)
- [MCP Server](https://developers.openai.com/codex/guides/agents-sdk)
- [GitHub Action](https://developers.openai.com/codex/github-action)

### Learn

- [Videos](https://developers.openai.com/codex/videos)
- Blog

  - [Building frontend UIs with Codex and Figma](https://developers.openai.com/blog/building-frontend-uis-with-codex-and-figma)
  - [Run long horizon tasks with Codex](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex)
  - [View all](https://developers.openai.com/blog/topic/codex)

- Cookbooks

  - [Codex Prompting Guide](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide)
  - [Modernizing your Codebase with Codex](https://developers.openai.com/cookbook/examples/codex/code_modernization)
  - [View all](https://developers.openai.com/cookbook/topic/codex)

- [Building AI Teams](https://developers.openai.com/codex/guides/build-ai-native-engineering-team)

### Community

- [Ambassadors](https://developers.openai.com/codex/ambassadors)
- [Open Source Program](https://developers.openai.com/codex/community/codex-for-oss)
- [Meetups](https://developers.openai.com/codex/community/meetups)

### Releases

- [Changelog](https://developers.openai.com/codex/changelog)
- [Feature Maturity](https://developers.openai.com/codex/feature-maturity)
- [Open Source](https://developers.openai.com/codex/open-source)

[API Dashboard](https://platform.openai.com/login)

Search
⌘

K

Copy PageMore page actions

Copy PageMore page actions

Codex reads configuration details from more than one location. Your personal defaults live in `~/.codex/config.toml`, and you can add project overrides with `.codex/config.toml` files. For security, Codex loads project config files only when you trust the project.

## Codex configuration file

Codex stores user-level configuration at `~/.codex/config.toml`. To scope settings to a specific project or subfolder, add a `.codex/config.toml` file in your repo.

To open the configuration file from the Codex IDE extension, select the gear icon in the top-right corner, then select **Codex Settings > Open config.toml**.

The CLI and IDE extension share the same configuration layers. You can use them to:

- Set the default model and provider.
- Configure [approval policies and sandbox settings](https://developers.openai.com/codex/agent-approvals-security#sandbox-and-approvals).
- Configure [MCP servers](https://developers.openai.com/codex/mcp).

## Configuration precedence

Codex resolves values in this order (highest precedence first):

1. CLI flags and `--config` overrides
2. [Profile](https://developers.openai.com/codex/config-advanced#profiles) values (from `--profile <name>`)
3. Project config files: `.codex/config.toml`, ordered from the project root down to your current working directory (closest wins; trusted projects only)
4. User config: `~/.codex/config.toml`
5. System config (if present): `/etc/codex/config.toml` on Unix
6. Built-in defaults

Use that precedence to set shared defaults at the top level and keep profiles focused on the values that differ.

If you mark a project as untrusted, Codex skips project-scoped `.codex/` layers (including `.codex/config.toml`) and falls back to user, system, and built-in defaults.

For one-off overrides via `-c`/`--config` (including TOML quoting rules), see [Advanced Config](https://developers.openai.com/codex/config-advanced#one-off-overrides-from-the-cli).

On managed machines, your organization may also enforce constraints via
`requirements.toml` (for example, disallowing `approval_policy = "never"` or
`sandbox_mode = "danger-full-access"`). See [Managed\\
configuration](https://developers.openai.com/codex/enterprise/managed-configuration) and [Admin-enforced\\
requirements](https://developers.openai.com/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml).

## Common configuration options

Here are a few options people change most often:

#### Default model

Choose the model Codex uses by default in the CLI and IDE.

```
model = "gpt-5.4"


```

#### Approval prompts

Control when Codex pauses to ask before running generated commands.

```
approval_policy = "on-request"


```

For behavior differences between `untrusted`, `on-request`, and `never`, see [Run without approval prompts](https://developers.openai.com/codex/agent-approvals-security#run-without-approval-prompts) and [Common sandbox and approval combinations](https://developers.openai.com/codex/agent-approvals-security#common-sandbox-and-approval-combinations).

#### Sandbox level

Adjust how much filesystem and network access Codex has while executing commands.

```
sandbox_mode = "workspace-write"


```

For mode-by-mode behavior (including protected `.git`/`.codex` paths and network defaults), see [Sandbox and approvals](https://developers.openai.com/codex/agent-approvals-security#sandbox-and-approvals), [Protected paths in writable roots](https://developers.openai.com/codex/agent-approvals-security#protected-paths-in-writable-roots), and [Network access](https://developers.openai.com/codex/agent-approvals-security#network-access).

#### Windows sandbox mode

When running Codex natively on Windows, set the native sandbox mode to `elevated` in the `windows` table. Use `unelevated` only if you don’t have administrator permissions or if elevated setup fails.

```
[windows]
sandbox = "elevated"   # Recommended
# sandbox = "unelevated" # Fallback if admin permissions/setup are unavailable


```

#### Web search mode

Codex enables web search by default for local tasks and serves results from a web search cache. The cache is an OpenAI-maintained index of web results, so cached mode returns pre-indexed results instead of fetching live pages. This reduces exposure to prompt injection from arbitrary live content, but you should still treat web results as untrusted. If you are using `--yolo` or another [full access sandbox setting](https://developers.openai.com/codex/agent-approvals-security#common-sandbox-and-approval-combinations), web search defaults to live results. Choose a mode with `web_search`:

- `"cached"` (default) serves results from the web search cache.
- `"live"` fetches the most recent data from the web (same as `--search`).
- `"disabled"` turns off the web search tool.

```
web_search = "cached"  # default; serves results from the web search cache
# web_search = "live"  # fetch the most recent data from the web (same as --search)
# web_search = "disabled"


```

#### Reasoning effort

Tune how much reasoning effort the model applies when supported.

```
model_reasoning_effort = "high"


```

#### Communication style

Set a default communication style for supported models.

```
personality = "friendly" # or "pragmatic" or "none"


```

You can override this later in an active session with `/personality` or per thread/turn when using the app-server APIs.

#### Command environment

Control which environment variables Codex forwards to spawned commands.

```
[shell_environment_policy]
include_only = ["PATH", "HOME"]


```

#### Log directory

Override where Codex writes local log files such as `codex-tui.log`.

```
log_dir = "/absolute/path/to/codex-logs"


```

For one-off runs, you can also set it from the CLI:

```
codex -c log_dir=./.codex-log


```

## Feature flags

Use the `[features]` table in `config.toml` to toggle optional and experimental capabilities.

```
[features]
shell_snapshot = true           # Speed up repeated commands


```

### Supported features

| Key | Default | Maturity | Description |
| --- | --- | --- | --- |
| `apps` | false | Experimental | Enable ChatGPT Apps/connectors support |
| `apps_mcp_gateway` | false | Experimental | Route Apps MCP calls through `https://api.openai.com/v1/connectors/mcp/` instead of legacy routing |
| `collaboration_modes` | true | Stable | Enable collaboration modes such as plan mode |
| `multi_agent` | false | Experimental | Enable multi-agent collaboration tools |
| `personality` | true | Stable | Enable personality selection controls |
| `remote_models` | false | Experimental | Refresh remote model list before showing readiness |
| `runtime_metrics` | false | Experimental | Show runtime metrics summaries in TUI turn separators |
| `request_rule` | true | Stable | Enable Smart approvals (`prefix_rule` suggestions) |
| `search_tool` | false | Experimental | Enable `search_tool_bm25` so Codex discovers Apps MCP tools via search before tool calls |
| `shell_snapshot` | false | Beta | Snapshot your shell environment to speed up repeated commands |
| `shell_tool` | true | Stable | Enable the default `shell` tool |
| `use_linux_sandbox_bwrap` | false | Experimental | Use the bubblewrap-based Linux sandbox pipeline |
| `unified_exec` | false | Beta | Use the unified PTY-backed exec tool |
| `undo` | true | Stable | Enable undo via per-turn git ghost snapshots |
| `web_search` | true | Deprecated | Legacy toggle; prefer the top-level `web_search` setting |
| `web_search_cached` | true | Deprecated | Legacy toggle that maps to `web_search = "cached"` when unset |
| `web_search_request` | true | Deprecated | Legacy toggle that maps to `web_search = "live"` when unset |

The Maturity column uses feature maturity labels such as Experimental, Beta,
and Stable. See [Feature Maturity](https://developers.openai.com/codex/feature-maturity) for how to
interpret these labels.

Omit feature keys to keep their defaults.

### Enabling features

- In `config.toml`, add `feature_name = true` under `[features]`.
- From the CLI, run `codex --enable feature_name`.
- To enable more than one feature, run `codex --enable feature_a --enable feature_b`.
- To disable a feature, set the key to `false` in `config.toml`.