[Skip to main content](https://cursor.com/docs/bugbot#main-content)

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

# Bugbot

Bugbot reviews pull requests and identifies bugs, security issues, and code quality problems.

On Teams and Individual Plans, Bugbot includes a free tier: every user gets a limited number of free PR reviews each month. When you reach the limit, reviews pause until your next billing cycle. You can start a 14‑day free Bugbot Pro trial for unlimited reviews (subject to standard abuse guardrails).

## [How it works](https://cursor.com/docs/bugbot\#how-it-works)

Bugbot analyzes PR diffs and leaves comments with explanations and fix suggestions. It runs automatically on each PR update or manually when triggered.

- Runs **automatic reviews** on every PR update
- **Manual trigger** by commenting `cursor review` or `bugbot run` on any PR
- **Uses existing PR comments as context**: reads GitHub PR comments (top‑level and inline) to avoid duplicate suggestions and build on prior feedback
- **Fix in Cursor** links open issues directly in Cursor
- **Fix in Web** links open issues directly in [cursor.com/agents](https://cursor.com/agents)

## [Setup](https://cursor.com/docs/bugbot\#setup)

GitHub.comGitLab.comGitHub Enterprise ServerGitLab Self-Hosted

Requires Cursor admin access and GitHub org admin access.

1. Go to [cursor.com/dashboard](https://cursor.com/dashboard?tab=integrations)
2. Navigate to the Integrations tab
3. Click `Connect GitHub` (or `Manage Connections` if already connected)
4. Follow the GitHub installation flow
5. Return to the dashboard to enable Bugbot on specific repositories

## [Configuration](https://cursor.com/docs/bugbot\#configuration)

IndividualTeam

### [Repository settings](https://cursor.com/docs/bugbot\#repository-settings-1)

Team admins can enable Bugbot per repository, configure allow/deny lists for reviewers, and set:

- Run **only once** per PR per installation, skipping subsequent commits

Bugbot runs for all contributors to enabled repositories, regardless of team membership.

### [Personal settings](https://cursor.com/docs/bugbot\#personal-settings-1)

Team members can override settings for their own PRs:

- Run **only when mentioned** by commenting `cursor review` or `bugbot run`
- Run **only once** per PR, skipping subsequent commits
- **Enable reviews on draft PRs** to include draft pull requests in automatic reviews

## [Analytics](https://cursor.com/docs/bugbot\#analytics)

![Bugbot dashboard](https://cursor.com/docs-static/_next/image?url=%2Fdocs-static%2Fimages%2Fbugbot%2Fbugbot-dashboard.png&w=1920&q=75&dpl=dpl_7zPiZUsTD7ownHrxp4Gk37N86tFn)

## [Rules](https://cursor.com/docs/bugbot\#rules)

Create `.cursor/BUGBOT.md` files to provide project-specific context for reviews. Bugbot always includes the root `.cursor/BUGBOT.md` file and any additional files found while traversing upward from changed files.

```
project/
  .cursor/BUGBOT.md          # Always included (project-wide rules)
  backend/
    .cursor/BUGBOT.md        # Included when reviewing backend files
    api/
      .cursor/BUGBOT.md      # Included when reviewing API files
  frontend/
    .cursor/BUGBOT.md        # Included when reviewing frontend files
```

### [Team rules](https://cursor.com/docs/bugbot\#team-rules)

Team admins can create rules from the [Bugbot dashboard](https://cursor.com/dashboard?tab=bugbot) that apply to all repositories in the team. These rules are available to every enabled repository, making it easy to enforce organization-wide standards.

When both Team Rules and project rule files (`.cursor/BUGBOT.md`) exist, Bugbot uses both. They are applied in this order: **Team Rules → project BUGBOT.md (including nested files) → User Rules**.

### [Examples](https://cursor.com/docs/bugbot\#examples)

### Security: Flag any use of eval() or exec()

```
If any changed file contains the string pattern /\beval\s*\(|\bexec\s*\(/i, then:
- Add a blocking Bug with title "Dangerous dynamic execution" and body:
  "Usage of eval/exec was found. Replace with safe alternatives or justify with a detailed comment and tests."
- Assign the Bug to the PR author.
- Apply label "security".
```

### OSS licenses: Prevent importing disallowed licenses

```
If the PR modifies dependency files (package.json, pnpm-lock.yaml, yarn.lock, requirements.txt, go.mod, Cargo.toml), then:
- Run the built-in License Scan.
- If any new or upgraded dependency has license in {GPL-2.0, GPL-3.0, AGPL-3.0}, then:
  - Add a blocking Bug titled "Disallowed license detected"
  - Include the offending package names, versions, and licenses in the Bug body
  - Apply labels "compliance" and "security"
```

### Language standards: Flag React componentWillMount usage

```
For files matching **/*.{js,jsx,ts,tsx} in React projects:
If a changed file contains /componentWillMount\s*\(/, then:
- Add a blocking Bug titled "Deprecated React lifecycle method"
- Body: "Replace componentWillMount with constructor or useEffect. See React docs."
- Suggest an autofix snippet that migrates side effects to useEffect.
```

### Standards: Require tests for backend changes

```
If the PR modifies files in {server/**, api/**, backend/**} and there are no changes in {**/*.test.*, **/__tests__/**, tests/**}, then:
- Add a blocking Bug titled "Missing tests for backend changes"
- Body: "This PR modifies backend code but includes no accompanying tests. Please add or update tests."
- Apply label "quality"
```

### Style: Disallow TODO comments

```
If any changed file contains /(?:^|\s)(TODO|FIXME)(?:\s*:|\s+)/, then:
- Add a non-blocking Bug titled "TODO/FIXME comment found"
- Body: "Replace TODO/FIXME with a tracked issue reference, e.g., `TODO(#1234): ...`, or remove it."
- If the TODO already references an issue pattern /#\d+|[A-Z]+-\d+/, mark the Bug as resolved automatically.
```

## [Autofix](https://cursor.com/docs/bugbot\#autofix)

Bugbot Autofix automatically spawns a [Cloud Agent](https://cursor.com/docs/cloud-agent#overview) to fix bugs found during PR reviews.

### [How it works](https://cursor.com/docs/bugbot\#how-it-works-1)

When Bugbot finds bugs during a PR review, it can automatically:

1. Spawn a Cloud Agent to analyze and fix the reported issues
2. Push fixes to the existing branch or a new branch (depending on your settings)
3. Post a comment on the original PR with the results

![Bugbot Autofix comment on a PR](https://cursor.com/docs-static/_next/image?url=%2Fdocs-static%2Fimages%2Fbugbot%2Fbugbot-autofix-comment.png&w=1920&q=75&dpl=dpl_7zPiZUsTD7ownHrxp4Gk37N86tFn)

### [Configuration](https://cursor.com/docs/bugbot\#configuration-1)

Configure autofix behavior from the [Bugbot dashboard](https://cursor.com/dashboard?tab=bugbot).

IndividualTeam

Team admins can set a default autofix mode for all team members in a GitHub organization:

- **Off** — autofix is disabled by default
- **Create New Branch** (Recommended) — Push fixes to a new branch for team members
- **Commit to Existing Branch** — Push fixes directly to the PR branch (max 3 attempts per PR to prevent loops)

Individual team members can override these defaults in their personal settings.

Autofix uses your **Default agent model** from [Settings → Models](https://cursor.com/dashboard?tab=settings). If you haven't set a personal model preference, autofix falls back to your team's default model (if you're on a team) or the system default.

### [Requirements](https://cursor.com/docs/bugbot\#requirements)

Autofix requires:

- [Usage-based pricing](https://cursor.com/docs/models-and-pricing) enabled
- Storage enabled (not in Legacy Privacy Mode)

### [Billing](https://cursor.com/docs/bugbot\#billing)

Autofix uses Cloud Agent credits and is billed at your plan rates. Cloud Agent billing follows your existing [pricing plan](https://cursor.com/docs/models-and-pricing).

## [Admin Configuration API](https://cursor.com/docs/bugbot\#admin-configuration-api)

Team admins can use the Bugbot Admin API to manage repositories and control which users can use Bugbot. Use it to automate repository management, enable Bugbot across multiple repositories, or integrate user provisioning with internal tools.

### [Authentication](https://cursor.com/docs/bugbot\#authentication)

All endpoints require a team Admin API Key passed as a Bearer token:

```
Authorization: Bearer $API_KEY
```

To create an API key:

1. Visit the [Settings tab in the Cursor dashboard](https://cursor.com/dashboard?tab=settings)
2. Under **Advanced**, click **New Admin API Key**
3. Save the API key

All endpoints are rate-limited to 60 requests per minute per team.

### [Enabling or disabling repositories](https://cursor.com/docs/bugbot\#enabling-or-disabling-repositories)

Use the `/bugbot/repo/update` endpoint to toggle Bugbot on or off for a repository:

```
curl -X POST https://api.cursor.com/bugbot/repo/update \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "repoUrl": "https://github.com/your-org/your-repo",
    "enabled": true
  }'
```

**Parameters:**

- `repoUrl` (string, required): The full URL of the repository
- `enabled` (boolean, required): `true` to enable Bugbot, `false` to disable it

The dashboard UI may take a moment to reflect changes made through the API due to caching. The API response shows the current state in the database.

### [Listing repositories](https://cursor.com/docs/bugbot\#listing-repositories)

Use the `/bugbot/repos` endpoint to list all repositories with their Bugbot settings for your team:

```
curl https://api.cursor.com/bugbot/repos \
  -H "Authorization: Bearer $API_KEY"
```

The response includes each repository's enabled status, manual-only setting, and timestamps.

### [Managing user access](https://cursor.com/docs/bugbot\#managing-user-access)

Use the `/bugbot/user/update` endpoint to control which GitHub or GitLab users can use your team's Bugbot licenses. Enterprises use this to integrate Bugbot provisioning with internal access-request tools.

#### [Prerequisites](https://cursor.com/docs/bugbot\#prerequisites)

Before calling this endpoint, enable an allowlist or blocklist mode in your [team Bugbot settings](https://cursor.com/dashboard?tab=bugbot):

- **Allowlist mode ("Only...")**: Only users on the list can use Bugbot
- **Blocklist mode ("Everyone but...")**: All users can use Bugbot except those on the list

If neither mode is enabled, the API returns an error.

#### [Adding or removing a user](https://cursor.com/docs/bugbot\#adding-or-removing-a-user)

```
curl -X POST https://api.cursor.com/bugbot/user/update \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "octocat",
    "allow": true
  }'
```

**Parameters:**

- `username` (string, required): The GitHub or GitLab username (case-insensitive)
- `allow` (boolean, required): Whether to grant or revoke access

How `allow` behaves depends on the active mode:

| Mode | `allow: true` | `allow: false` |
| --- | --- | --- |
| Allowlist | Adds user to list (can use Bugbot) | Removes user from list (cannot use Bugbot) |
| Blocklist | Removes user from blocklist (can use Bugbot) | Adds user to blocklist (cannot use Bugbot) |

**Response:**

```
{
  "outcome": "success",
  "message": "Updated team-level allowlist for @octocat",
  "updatedTeamSettings": true,
  "updatedInstallations": 0
}
```

The allowlist is stored at the team level and applies across all GitHub and GitLab installations owned by that team. Usernames are normalized to lowercase.

#### [Example: provisioning users through an internal tool](https://cursor.com/docs/bugbot\#example-provisioning-users-through-an-internal-tool)

Connect this API to an internal access-request portal. When an employee requests Bugbot access, the portal calls the API to add them. When they leave or lose access, it calls the API to remove them.

**Grant access:**

```
curl -X POST https://api.cursor.com/bugbot/user/update \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "employee-github-name", "allow": true}'
```

**Revoke access:**

```
curl -X POST https://api.cursor.com/bugbot/user/update \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "employee-github-name", "allow": false}'
```

## [Pricing](https://cursor.com/docs/bugbot\#pricing)

Bugbot offers two tiers: **Free** and **Pro**.

### [Free tier](https://cursor.com/docs/bugbot\#free-tier)

On Teams and Individual Cursor plans, every user gets a limited number of free PR reviews each month. For teams, each team member gets their own free reviews. When you reach the limit, reviews pause until your next billing cycle. You can upgrade anytime to a paid Bugbot plan for unlimited reviews.

### [Pro tier](https://cursor.com/docs/bugbot\#pro-tier)

IndividualsTeams

### [Per-user billing](https://cursor.com/docs/bugbot\#per-user-billing)

Teams pay $40 per user per month for unlimited reviews.

We count a user as someone who authored PRs reviewed by Bugbot in a month.

All licenses are relinquished at the start of each billing cycle, and will be assigned out on a first-come, first-served basis. If a user doesn't author any PRs reviewed by Bugbot in a month, the seat can be used by another user.

### [Seat limits](https://cursor.com/docs/bugbot\#seat-limits)

Team admins can set maximum Bugbot seats per month to control costs.

### [Getting started](https://cursor.com/docs/bugbot\#getting-started-1)

Subscribe through your team dashboard to enable billing.

### [Abuse guardrails](https://cursor.com/docs/bugbot\#abuse-guardrails)

In order to prevent abuse, we have a pooled cap of 200 pull requests per month for every Bugbot license. If you need more than 200 pull requests per month, please contact us at [hi@cursor.com](mailto:hi@cursor.com) and we'll be happy to help you out.

For example, if your team has 100 users, your organization will initially be able to review 20,000 pull requests per month. If you reach that limit naturally, please reach out to us and we'll be happy to increase the limit.

## [Troubleshooting](https://cursor.com/docs/bugbot\#troubleshooting)

If Bugbot isn't working:

1. **Enable verbose mode** by commenting `cursor review verbose=true` or `bugbot run verbose=true` for detailed logs and request ID
2. **Check permissions** to verify Bugbot has repository access
3. **Verify installation** to confirm the GitHub app is installed and enabled

Include the request ID from verbose mode when reporting issues.

## [FAQ](https://cursor.com/docs/bugbot\#faq)

### Does Bugbot read GitHub PR comments?

Yes. Bugbot reads both top‑level and inline GitHub pull request comments and includes them as context during reviews. This helps avoid duplicate suggestions and allows Bugbot to build on prior feedback from reviewers.

### Is Bugbot privacy-mode compliant?

Yes, Bugbot follows the same privacy compliance as Cursor and processes data identically to other Cursor requests.

### What happens when I hit the free tier limit?

When you reach your monthly free tier limit, Bugbot reviews pause until your next billing cycle. You can start a 14‑day free Bugbot Pro trial for unlimited reviews (subject to standard abuse guardrails).

### How do I give Bugbot access to my GitLab or GitHub Enterprise Server instance?

Self-hosted instances require secure inbound access for PR reviews and outbound access for webhook notifications. Bugbot supports multiple networking configurations:

### [1\. IP Whitelisting (Recommended)](https://cursor.com/docs/bugbot\#1-ip-whitelisting-recommended)

Add these IP addresses to your instance's allowlist:

```
184.73.225.134
3.209.66.12
52.44.113.131
```

**Best for:** Most self-hosted environments

**Security:** HTTPS encryption, optional IP allowlisting, service account access tokens

### [2\. PrivateLink (AWS) or Private Service Connect (GCP)](https://cursor.com/docs/bugbot\#2-privatelink-aws-or-private-service-connect-gcp)

Available with Enterprise Bugbot. Allow Cursor to access your instance over a private network connection. [Contact your Cursor representative](https://cursor.com/contact-sales?source=bugbot) for setup.

**Best for:** Instances behind a firewall on a private network in AWS, Azure, or GCP

**Security:** HTTPS encryption with optional mTLS, PrivateLink/Service Connect, VPC allowlisting, service account access tokens

**Drawbacks:** Only supports public clouds with private networking connections between VPCs

### [3\. Reverse Proxy](https://cursor.com/docs/bugbot\#3-reverse-proxy)

Available with Enterprise Bugbot. Run a reverse proxy on-premises that establishes a long-lived websocket connection to Cursor's servers. Network requests are forwarded through to your instance. Requires no inbound network access. [Contact your Cursor representative](https://cursor.com/contact-sales?source=bugbot) for setup.

**Best for:** Environments without inbound network access

**Security:** HTTPS encryption, service account access tokens

**Drawbacks:** Introduces additional complexity, maintenance requirements, and potential security considerations compared to more direct connection methods

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