[Skip to main content](https://cursor.com/docs/reference/sandbox#main-content)

## Command Palette

Search for a command to run...

## Get Started

[Welcome](https://cursor.com/docs) [Quickstart](https://cursor.com/docs/get-started/quickstart)
Models & Pricing

## Agent

[Overview](https://cursor.com/docs/agent/overview) [Planning](https://cursor.com/docs/agent/plan-mode) [Prompting](https://cursor.com/docs/agent/prompting) [Debugging](https://cursor.com/docs/agent/debug-mode)
Tools
[Parallel Agents](https://cursor.com/docs/configuration/worktrees) [Security](https://cursor.com/docs/agent/security)

## Customizing

[Plugins](https://cursor.com/docs/plugins) [Rules](https://cursor.com/docs/rules) [Skills](https://cursor.com/docs/skills) [Subagents](https://cursor.com/docs/subagents) [Hooks](https://cursor.com/docs/hooks) [MCP](https://cursor.com/docs/mcp)

## Cloud Agents

[Overview](https://cursor.com/docs/cloud-agent) [Setup](https://cursor.com/docs/cloud-agent/setup) [Capabilities](https://cursor.com/docs/cloud-agent/capabilities) [Bugbot](https://cursor.com/docs/bugbot) [Best Practices](https://cursor.com/docs/cloud-agent/best-practices) [Security & Network](https://cursor.com/docs/cloud-agent/security-network) [Settings](https://cursor.com/docs/cloud-agent/settings) [API](https://cursor.com/docs/cloud-agent/api/endpoints)

## Integrations

[Slack](https://cursor.com/docs/integrations/slack) [Linear](https://cursor.com/docs/integrations/linear) [GitHub](https://cursor.com/docs/integrations/github) [GitLab](https://cursor.com/docs/integrations/gitlab) [JetBrains](https://cursor.com/docs/integrations/jetbrains) [Deeplinks](https://cursor.com/docs/reference/deeplinks)

## CLI

[Overview](https://cursor.com/docs/cli/overview) [Installation](https://cursor.com/docs/cli/installation) [Capabilities](https://cursor.com/docs/cli/using) [Shell Mode](https://cursor.com/docs/cli/shell-mode) [ACP](https://cursor.com/docs/cli/acp) [Headless / CI](https://cursor.com/docs/cli/headless)
Reference

## Teams & Enterprise

Teams

Enterprise

Get Started

# sandbox.json reference

Configure [sandbox](https://cursor.com/docs/agent/tools/terminal#sandbox) behavior with a `sandbox.json` file to control network access, filesystem paths, and more.

## [File locations](https://cursor.com/docs/reference/sandbox\#file-locations)

Place `sandbox.json` in either or both of these locations:

| Location | Scope | Priority |
| --- | --- | --- |
| `~/.cursor/sandbox.json` | All workspaces (per-user) | Lower |
| `<workspace>/.cursor/sandbox.json` | Single workspace (per-repo) | Higher |

Both files are optional. When both exist, they are merged with per-repo settings taking priority. Enterprise team-admin policies and Cursor's hardcoded security rules layer on top and cannot be weakened by either file.

## [Top-level fields](https://cursor.com/docs/reference/sandbox\#top-level-fields)

All fields are optional. Missing fields use the defaults shown below.

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `type` | string | `"workspace_readwrite"` | Sandbox mode. `"workspace_readwrite"` gives read/write access in the workspace. `"workspace_readonly"` restricts to read-only. `"insecure_none"` disables the sandbox entirely. |
| `additionalReadwritePaths` | `string[]` | `[]` | Extra paths the agent can read and write. Only applies when `type` is `"workspace_readwrite"`. |
| `additionalReadonlyPaths` | `string[]` | `[]` | Extra paths the agent can read. |
| `disableTmpWrite` | `boolean` | `false` | When `true`, removes default write access to `/tmp` and system temp directories. |
| `enableSharedBuildCache` | `boolean` | `false` | Redirects build-tool caches (npm, cargo, pip, etc.) to a shared tmpdir so sandboxed and unsandboxed commands share the same caches. |

## [`networkPolicy` object](https://cursor.com/docs/reference/sandbox\#networkpolicy-object)

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `default` | `"allow"` \| `"deny"` | `"deny"` | Action when no allow/deny rule matches. |
| `allow` | `string[]` | `[]` | Patterns to allow. Supports exact domains, wildcards, and CIDR notation. |
| `deny` | `string[]` | `[]` | Patterns to deny. Highest priority; always blocks, even if a pattern also appears in `allow`. |

## [Network pattern syntax](https://cursor.com/docs/reference/sandbox\#network-pattern-syntax)

The `allow` and `deny` arrays accept three pattern formats:

| Format | Example | Matches |
| --- | --- | --- |
| Exact domain | `"registry.npmjs.org"` | That exact host |
| Wildcard | `"*.example.com"` | Any subdomain of `example.com`, including `example.com` itself |
| CIDR | `"10.0.0.0/8"` | Any IP in that range |

**Key rules:**

- Deny always beats allow. If a host matches both lists, it is blocked.
- Private/RFC 1918 addresses (`10.x`, `172.16.x`, `192.168.x`, `127.x`) and cloud metadata endpoints (`169.254.169.254`) are blocked by default to prevent SSRF.
- IPv6 private addresses (`::1`, `fe80::/10`, `fc00::/7`) are also blocked.
- URL paths are ignored; matching is domain/IP only.

## [How policies merge](https://cursor.com/docs/reference/sandbox\#how-policies-merge)

When multiple policy sources exist, they merge in priority order:

```
per-user  <  per-repo  <  team-admin  <  hardcoded
(lowest)                                (highest)
```

Merge rules:

- **Paths** (`additionalReadwritePaths`, `additionalReadonlyPaths`): unioned across all sources.
- **Network allow lists**: unioned, unless a team-admin allowlist is present (which replaces the union).
- **Network deny lists**: always unioned.
- **`networkPolicy.default`**: `"deny"` wins over `"allow"`.
- **Restrictive booleans** (`disableTmpWrite`, `networkPolicyStrict`): `true` wins.

## [Protected paths](https://cursor.com/docs/reference/sandbox\#protected-paths)

Certain paths are always write-protected, regardless of your `sandbox.json` configuration:

- `.cursor/*.json`, `.cursor/**/*.json`, `.cursor/.workspace-trusted`
- `.claude/*.json`, `.claude/**/*.json`
- `.vscode/**`
- `.code-workspace`
- `.git/hooks/**`, `.git/config`, `.git/info/attributes`
- `.cursorignore`

The following `.cursor` subdirectories **are** writable: `rules/`, `commands/`, `worktrees/`, `skills/`, `agents/`.

SSL certificate paths and `~/.ssh` are always readable.

## [Examples](https://cursor.com/docs/reference/sandbox\#examples)

### [Allow specific domains](https://cursor.com/docs/reference/sandbox\#allow-specific-domains)

```
{
  "networkPolicy": {
    "default": "deny",
    "allow": [\
      "registry.npmjs.org",\
      "pypi.org",\
      "*.githubusercontent.com"\
    ]
  }
}
```

Network traffic is denied by default. Only the listed domains are reachable.

### [Allow all network](https://cursor.com/docs/reference/sandbox\#allow-all-network)

```
{
  "networkPolicy": {
    "default": "allow"
  }
}
```

All outbound network traffic is permitted inside the sandbox.

### [Full-stack web project](https://cursor.com/docs/reference/sandbox\#full-stack-web-project)

A project where the agent needs to install packages, pull container images, access a database on the local network, and read a shared design-tokens repo:

```
{
  "networkPolicy": {
    "default": "deny",
    "allow": [\
      "registry.npmjs.org",\
      "registry.yarnpkg.com",\
      "pypi.org",\
      "files.pythonhosted.org",\
      "*.docker.io",\
      "ghcr.io",\
      "*.googleapis.com"\
    ],
    "deny": [\
      "*.internal.corp.example.com"\
    ]
  },
  "additionalReadwritePaths": [\
    "/home/me/.docker"\
  ],
  "additionalReadonlyPaths": [\
    "/opt/shared/design-tokens"\
  ],
  "enableSharedBuildCache": true
}
```

This configuration lets the agent:

- Install npm/pip packages and pull Docker images.
- Hit Google Cloud APIs.
- Block access to internal corporate services.
- Write to `~/.docker` for container operations.
- Read (but not modify) a shared design-tokens directory.
- Share npm/pip/cargo caches between sandboxed and unsandboxed runs.

English

- English
- 简体中文
- 日本語
- 繁體中文
- Español
- Français
- Português
- 한국어
- Русский
- Türkçe
- Bahasa Indonesia
- Deutsch

Agent

Sonnet 4.6

Tokenizer OffContext: 0/200k (0%)

Open chat