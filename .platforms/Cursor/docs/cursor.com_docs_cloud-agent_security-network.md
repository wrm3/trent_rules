[Skip to main content](https://cursor.com/docs/cloud-agent/security-network#main-content)

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

Cloud Agents

# Security & Network

Cloud Agents are available in Privacy Mode. We never train on your code and only retain code for running the agent. [Learn more about Privacy mode](https://www.cursor.com/privacy-overview).

## [Secret protection](https://cursor.com/docs/cloud-agent/security-network\#secret-protection)

Secrets provided to Cloud Agents are encrypted at rest and in transit. They are not visible to anyone other than the Cloud Agent user.

You can classify secrets as "Redacted" for additional protection. Redacted secrets:

- Are scanned in commit messages and files, which are rejected if they contain the secret
- Are redacted from model tool calls, so they are not shown to the models or stored in chat transcripts

This prevents accidental exposure of credentials in version control and model context.

## [What you should know](https://cursor.com/docs/cloud-agent/security-network\#what-you-should-know)

1. Grant read-write privileges to our GitHub app for repos you want to edit. We use this to clone the repo and make changes.
2. Your code runs inside our AWS infrastructure in isolated VMs and is stored on VM disks while the agent is accessible.
3. The agent has internet access by default. You can configure [network egress controls](https://cursor.com/docs/cloud-agent/security-network#network-access) to restrict the domains the agent can access.
4. The agent auto-runs all terminal commands, letting it iterate on tests. This differs from the foreground agent, which requires user approval for every command. Auto-running introduces data exfiltration risk: attackers could execute prompt injection attacks, tricking the agent to upload code to malicious websites. See [OpenAI's explanation about risks of prompt injection for cloud agents](https://platform.openai.com/docs/codex/agent-network#risks-of-agent-internet-access).
5. If privacy mode is disabled, we collect prompts and dev environments to improve the product.
6. If you disable privacy mode when starting a cloud agent, then enable it during the agent's run, the agent continues with privacy mode disabled until it completes.

## [Network access](https://cursor.com/docs/cloud-agent/security-network\#network-access)

Control which network resources your Cloud Agents can reach. These settings are available on the [Cloud Agents dashboard](https://cursor.com/dashboard?tab=cloud-agents) for individual users and team admins.

### [Access modes](https://cursor.com/docs/cloud-agent/security-network\#access-modes)

Three modes control outbound network access for Cloud Agents:

| Mode | Behavior |
| --- | --- |
| **Allow all network access** | Cloud Agents can reach any external host. No domain restrictions apply. |
| **Default + allowlist** | Cloud Agents can reach the [default domains](https://cursor.com/docs/agent/tools/terminal#default-network-allowlist) plus any domains you add to your allowlist. |
| **Allowlist only** | Cloud Agents can only reach the domains you explicitly add to your allowlist. |

Even in **Allowlist only** mode, a small set of domains remain accessible so Cloud Agents can function. These include Cursor's own services and source control management (SCM) providers.

### [User-level settings](https://cursor.com/docs/cloud-agent/security-network\#user-level-settings)

Individual users can configure their network access mode from the [Cloud Agents dashboard](https://cursor.com/dashboard?tab=cloud-agents) under the **Security** header. Your user-level setting applies to all Cloud Agents you create.

When you select a mode that includes an allowlist ( **Default + allowlist** or **Allowlist only**), an allowlist configuration section appears below the setting where you can add your custom domains.

### [Team-level settings](https://cursor.com/docs/cloud-agent/security-network\#team-level-settings)

Team admins can set a default network access mode for the entire team from the same dashboard. The team-level allowlist is the same allowlist that admins configure for the [sandbox default network allowlist](https://cursor.com/docs/agent/tools/terminal#default-network-allowlist). There is no separate allowlist to manage; one allowlist controls both Cloud Agent network access and the sandbox defaults.

When a team-level setting exists:

- If a user has configured their own setting, the **user setting takes precedence**.
- If a user has not configured a setting, the **team default applies**.

### [Locking the setting (Enterprise)](https://cursor.com/docs/cloud-agent/security-network\#locking-the-setting-enterprise)

Locking is available for Enterprise teams only.

Enterprise team admins can lock the network access setting using the **Lock Network Access Policy** option. When locked:

- The team-level setting applies to every member, regardless of their individual preference.
- Users cannot override the locked setting from their own dashboard.

This gives admins full control over Cloud Agent network access across the organization.

### [Relationship to sandbox network policy](https://cursor.com/docs/cloud-agent/security-network\#relationship-to-sandbox-network-policy)

The "Default" domains in the **Default + allowlist** mode are the same [default network allowlist](https://cursor.com/docs/agent/tools/terminal#default-network-allowlist) used by the desktop Agent's sandbox. The team-level allowlist is also shared: when an admin configures an allowlist on the dashboard, it applies to both Cloud Agent network access and the [sandbox network policy](https://cursor.com/docs/reference/sandbox).

## [Egress IP ranges](https://cursor.com/docs/cloud-agent/security-network\#egress-ip-ranges)

Cloud Agents make network connections from specific IP address ranges when accessing external services, APIs, or repositories.

### [API endpoint](https://cursor.com/docs/cloud-agent/security-network\#api-endpoint)

The IP ranges are available via a [JSON API endpoint](https://cursor.com/docs/ips.json):

```
curl https://cursor.com/docs/ips.json
```

#### [Response format](https://cursor.com/docs/cloud-agent/security-network\#response-format)

```
{
  "version": 1,
  "modified": "2025-09-24T16:00:00.000Z",
  "cloudAgents": {
    "us3p": ["100.26.13.169/32", "34.195.201.10/32", "..."],
    "us4p": ["54.184.235.255/32", "35.167.37.158/32", "..."],
    "us5p": ["3.12.82.200/32", "52.14.104.140/32", "..."]
  }
}
```

- **version**: Schema version number for the API response
- **modified**: ISO 8601 timestamp of when the IP ranges were last updated
- **cloudAgents**: Object containing IP ranges, keyed by cluster

IP ranges published in [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing). You can use an online conversion tool to convert from CIDR notation to IP address ranges if needed.

### [Using the IP ranges](https://cursor.com/docs/cloud-agent/security-network\#using-the-ip-ranges)

These published IP ranges may be used by Cloud Agents to:

- Clone and push to remote repositories (unless using the [GitHub IP allow list](https://cursor.com/docs/integrations/github#ip-allow-list-configuration))
- Download packages and dependencies
- Make API calls to external services
- Access web resources during agent execution

If your organization uses firewall rules or IP allowlists to control network access, you may need to allowlist these IP ranges to ensure Cloud Agents can properly access your services.

**Important considerations:**

- We make changes to our IP addresses from time to time for scaling and operational needs.
- We do not recommend allowlisting by IP address as your primary security mechanism.
- If you must use these IP ranges, we strongly encourage regular monitoring of the JSON API endpoint.

### [GitHub proxy and IP allow list](https://cursor.com/docs/cloud-agent/security-network\#github-proxy-and-ip-allow-list)

Cursor supports a similar but distinct feature to [use a GitHub egress proxy for IP allow lists](https://cursor.com/docs/integrations/github#ip-allow-list-configuration). This proxy works for all GitHub-dependent Cursor features, including Cloud Agents.

We recommended that you use the GitHub-specific IP allow list for GitHub, as it is more deeply integrated with the Cursor GitHub app, and the above egress IP ranges for everything else.

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