[Skip to main content](https://code.claude.com/docs/en/authentication#content-area)

[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/light.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=d535f2e20f53cd911acc59ad1b64b2e0)![dark logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/dark.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=28e49a2ffe69101f4aae9bfa70b393d0)](https://code.claude.com/docs)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Administration

Authentication

[Getting started](https://code.claude.com/docs/en/overview) [Build with Claude Code](https://code.claude.com/docs/en/sub-agents) [Deployment](https://code.claude.com/docs/en/third-party-integrations) [Administration](https://code.claude.com/docs/en/setup) [Configuration](https://code.claude.com/docs/en/settings) [Reference](https://code.claude.com/docs/en/cli-reference) [Resources](https://code.claude.com/docs/en/legal-and-compliance)

On this page

- [Log in to Claude Code](https://code.claude.com/docs/en/authentication#log-in-to-claude-code)
- [Set up team authentication](https://code.claude.com/docs/en/authentication#set-up-team-authentication)
- [Claude for Teams or Enterprise](https://code.claude.com/docs/en/authentication#claude-for-teams-or-enterprise)
- [Claude Console authentication](https://code.claude.com/docs/en/authentication#claude-console-authentication)
- [Cloud provider authentication](https://code.claude.com/docs/en/authentication#cloud-provider-authentication)
- [Credential management](https://code.claude.com/docs/en/authentication#credential-management)

Claude Code supports multiple authentication methods depending on your setup. Individual users can log in with a Claude.ai account, while teams can use Claude for Teams or Enterprise, the Claude Console, or a cloud provider like Amazon Bedrock, Google Vertex AI, or Microsoft Foundry.

## [​](https://code.claude.com/docs/en/authentication\#log-in-to-claude-code)  Log in to Claude Code

After [installing Claude Code](https://code.claude.com/docs/en/setup#install-claude-code), run `claude` in your terminal. On first launch, Claude Code opens a browser window for you to log in.If the browser doesn’t open automatically, press `c` to copy the login URL to your clipboard, then paste it into your browser.You can authenticate with any of these account types:

- **Claude Pro or Max subscription**: log in with your Claude.ai account. Subscribe at [claude.com/pricing](https://claude.com/pricing).
- **Claude for Teams or Enterprise**: log in with the Claude.ai account your team admin invited you to.
- **Claude Console**: log in with your Console credentials. Your admin must have [invited you](https://code.claude.com/docs/en/authentication#claude-console-authentication) first.
- **Cloud providers**: if your organization uses [Amazon Bedrock](https://code.claude.com/docs/en/amazon-bedrock), [Google Vertex AI](https://code.claude.com/docs/en/google-vertex-ai), or [Microsoft Foundry](https://code.claude.com/docs/en/microsoft-foundry), set the required environment variables before running `claude`. No browser login is needed.

To log out and re-authenticate, type `/logout` at the Claude Code prompt.If you’re having trouble logging in, see [authentication troubleshooting](https://code.claude.com/docs/en/troubleshooting#authentication-issues).

## [​](https://code.claude.com/docs/en/authentication\#set-up-team-authentication)  Set up team authentication

For teams and organizations, you can configure Claude Code access in one of these ways:

- [Claude for Teams or Enterprise](https://code.claude.com/docs/en/authentication#claude-for-teams-or-enterprise), recommended for most teams
- [Claude Console](https://code.claude.com/docs/en/authentication#claude-console-authentication)
- [Amazon Bedrock](https://code.claude.com/docs/en/amazon-bedrock)
- [Google Vertex AI](https://code.claude.com/docs/en/google-vertex-ai)
- [Microsoft Foundry](https://code.claude.com/docs/en/microsoft-foundry)

### [​](https://code.claude.com/docs/en/authentication\#claude-for-teams-or-enterprise)  Claude for Teams or Enterprise

[Claude for Teams](https://claude.com/pricing#team-&-enterprise) and [Claude for Enterprise](https://anthropic.com/contact-sales) provide the best experience for organizations using Claude Code. Team members get access to both Claude Code and Claude on the web with centralized billing and team management.

- **Claude for Teams**: self-service plan with collaboration features, admin tools, and billing management. Best for smaller teams.
- **Claude for Enterprise**: adds SSO, domain capture, role-based permissions, compliance API, and managed policy settings for organization-wide Claude Code configurations. Best for larger organizations with security and compliance requirements.

1

[Navigate to header](https://code.claude.com/docs/en/authentication#)

Subscribe

Subscribe to [Claude for Teams](https://claude.com/pricing#team-&-enterprise) or contact sales for [Claude for Enterprise](https://anthropic.com/contact-sales).

2

[Navigate to header](https://code.claude.com/docs/en/authentication#)

Invite team members

Invite team members from the admin dashboard.

3

[Navigate to header](https://code.claude.com/docs/en/authentication#)

Install and log in

Team members install Claude Code and log in with their Claude.ai accounts.

### [​](https://code.claude.com/docs/en/authentication\#claude-console-authentication)  Claude Console authentication

For organizations that prefer API-based billing, you can set up access through the Claude Console.

1

[Navigate to header](https://code.claude.com/docs/en/authentication#)

Create or use a Console account

Use your existing Claude Console account or create a new one.

2

[Navigate to header](https://code.claude.com/docs/en/authentication#)

Add users

You can add users through either method:

- Bulk invite users from within the Console: Settings -> Members -> Invite
- [Set up SSO](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso)

3

[Navigate to header](https://code.claude.com/docs/en/authentication#)

Assign roles

When inviting users, assign one of:

- **Claude Code** role: users can only create Claude Code API keys
- **Developer** role: users can create any kind of API key

4

[Navigate to header](https://code.claude.com/docs/en/authentication#)

Users complete setup

Each invited user needs to:

- Accept the Console invite
- [Check system requirements](https://code.claude.com/docs/en/setup#system-requirements)
- [Install Claude Code](https://code.claude.com/docs/en/setup#install-claude-code)
- Log in with Console account credentials

### [​](https://code.claude.com/docs/en/authentication\#cloud-provider-authentication)  Cloud provider authentication

For teams using Amazon Bedrock, Google Vertex AI, or Microsoft Foundry:

1

[Navigate to header](https://code.claude.com/docs/en/authentication#)

Follow provider setup

Follow the [Bedrock docs](https://code.claude.com/docs/en/amazon-bedrock), [Vertex docs](https://code.claude.com/docs/en/google-vertex-ai), or [Microsoft Foundry docs](https://code.claude.com/docs/en/microsoft-foundry).

2

[Navigate to header](https://code.claude.com/docs/en/authentication#)

Distribute configuration

Distribute the environment variables and instructions for generating cloud credentials to your users. Read more about how to [manage configuration here](https://code.claude.com/docs/en/settings).

3

[Navigate to header](https://code.claude.com/docs/en/authentication#)

Install Claude Code

Users can [install Claude Code](https://code.claude.com/docs/en/setup#install-claude-code).

## [​](https://code.claude.com/docs/en/authentication\#credential-management)  Credential management

Claude Code securely manages your authentication credentials:

- **Storage location**: on macOS, credentials are stored in the encrypted macOS Keychain.
- **Supported authentication types**: Claude.ai credentials, Claude API credentials, Azure Auth, Bedrock Auth, and Vertex Auth.
- **Custom credential scripts**: the [`apiKeyHelper`](https://code.claude.com/docs/en/settings#available-settings) setting can be configured to run a shell script that returns an API key.
- **Refresh intervals**: by default, `apiKeyHelper` is called after 5 minutes or on HTTP 401 response. Set `CLAUDE_CODE_API_KEY_HELPER_TTL_MS` environment variable for custom refresh intervals.

Was this page helpful?

YesNo

[Advanced setup](https://code.claude.com/docs/en/setup) [Security](https://code.claude.com/docs/en/security)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.