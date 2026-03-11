[Skip to main content](https://cursor.com/docs/integrations/github#main-content)

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

Integrations

# GitHub

[Cloud Agents](https://cursor.com/docs/cloud-agent) and [Bugbot](https://cursor.com/docs/bugbot) require the Cursor GitHub app to clone repositories and push changes.

## [Installation](https://cursor.com/docs/integrations/github\#installation)

1. Go to [Integrations in Dashboard](https://cursor.com/dashboard?tab=integrations)
2. Click **Connect** next to GitHub
3. Choose repository either **All repositories** or **Selected repositories**

To disconnect your GitHub account, return to the integrations dashboard and click **Disconnect Account**.

## [Using Agent in GitHub](https://cursor.com/docs/integrations/github\#using-agent-in-github)

The GitHub integration enables cloud agent workflows directly from pull requests and issues. You can trigger an agent to read context, implement fixes, and push commits by commenting `@cursor [prompt]` on any PR or issue.

If you have [Bugbot](https://cursor.com/docs/bugbot) enabled, you can comment `@cursor fix` to read the suggested fix from Bugbot to trigger a cloud agent to address the issue.

## [Permissions](https://cursor.com/docs/integrations/github\#permissions)

The GitHub app requires specific permissions to work with cloud agents:

| Permission | Purpose |
| --- | --- |
| **Repository access** | Clone your code and create working branches |
| **Pull requests** | Create PRs with agent changes for your review |
| **Issues** | Track bugs and tasks that agents discover or fix |
| **Checks and statuses** | Report on code quality and test results |
| **Actions and workflows** | Monitor CI/CD pipelines and deployment status |

All permissions follow the principle of least privilege needed for cloud agent functionality.

## [IP Allow List Configuration](https://cursor.com/docs/integrations/github\#ip-allow-list-configuration)

If your organization uses GitHub's IP allow list feature to restrict access to your repositories, Cursor can be configured to use a hosted GitHub proxy with a narrow set of egress IPs.

Before configuring IP allowlists, contact [hi@cursor.com](mailto:hi@cursor.com) to enable this feature for your team. This is required for either configuration method below.

### [Enable IP allow list configuration for installed GitHub Apps (recommended)](https://cursor.com/docs/integrations/github\#enable-ip-allow-list-configuration-for-installed-github-apps-recommended)

The Cursor GitHub app has the IP list already pre-configured. You can enable the allowlist for installed apps to automatically inherit this list. This is the **recommended approach**, as it allows us to update the list and your organization receives updates automatically.

To enable this:

1. Go to your organization's Security settings
2. Navigate to IP allow list settings
3. Check **"Allow access by GitHub Apps"**

For detailed instructions, see [GitHub's documentation](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#allowing-access-by-github-apps).

### [Add IPs directly to your allowlist](https://cursor.com/docs/integrations/github\#add-ips-directly-to-your-allowlist)

If your organization uses IdP-defined allowlists in GitHub or otherwise cannot use the pre-configured allowlist, you can manually add the IP addresses:

```
184.73.225.134
3.209.66.12
52.44.113.131
```

The list of IP addresses may infrequently change. Teams using IP allow lists
will be given advanced notice before IP addresses are added or removed.

## [Troubleshooting](https://cursor.com/docs/integrations/github\#troubleshooting)

### Agent can't access repository

- Install the GitHub app with repository access
- Check repository permissions for private repos
- Verify your GitHub account permissions

### Permission denied for pull requests

- Grant the app write access to pull requests
- Check branch protection rules
- Reinstall if the app installation expired

### App not visible in GitHub settings

- Check if installed at organization level
- Reinstall from [github.com/apps/cursor](https://github.com/apps/cursor)
- Contact support if installation is corrupted

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