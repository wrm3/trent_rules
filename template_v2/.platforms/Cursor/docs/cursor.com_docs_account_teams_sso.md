[Skip to main content](https://cursor.com/docs/account/teams/sso#main-content)

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

[Get Started](https://cursor.com/docs/account/teams/setup)

[Pricing](https://cursor.com/docs/account/teams/pricing)

[Members & Roles](https://cursor.com/docs/account/teams/members)

[SSO](https://cursor.com/docs/account/teams/sso)

[Dashboard](https://cursor.com/docs/account/teams/dashboard)

[Analytics](https://cursor.com/docs/account/teams/analytics)

Enterprise

Teams & Enterprise

# SSO

## [Overview](https://cursor.com/docs/account/teams/sso\#overview)

SAML 2.0 SSO is available at no additional cost on Teams and Enterprise plans. Use your existing identity provider (IdP) to authenticate team members without separate Cursor accounts.

## [Prerequisites](https://cursor.com/docs/account/teams/sso\#prerequisites)

- Cursor Team plan
- Admin access to your identity provider (e.g., Okta)
- Admin access to your Cursor organization

## [Configuration Steps](https://cursor.com/docs/account/teams/sso\#configuration-steps)

1

### Sign in to your Cursor account

Navigate to [cursor.com/dashboard?tab=settings](https://www.cursor.com/dashboard?tab=settings) with an admin account.

2

### Locate the SSO configuration

Find the "Single Sign-On (SSO)" section and expand it.

3

### Begin the setup process

Click the "SSO Provider Connection settings" button to start SSO setup and follow the wizard.

4

### Configure your identity provider

In your identity provider (e.g., Okta):

- Create new SAML application
- Configure SAML settings using Cursor's information
- Set up Just-in-Time (JIT) provisioning

5

### Verify domain

Verify the domain of your users in Cursor by clicking the "Domain verification settings" button.

### [Identity Provider Setup Guides](https://cursor.com/docs/account/teams/sso\#identity-provider-setup-guides)

For provider-specific setup instructions:

[Identity Provider Guides\\
\\
Setup instructions for Okta, Azure AD, Google Workspace, and more.](https://workos.com/docs/integrations)

## [Additional Settings](https://cursor.com/docs/account/teams/sso\#additional-settings)

- Manage SSO enforcement through admin dashboard
- New users auto-enroll when signing in through SSO
- Handle user management through your identity provider

## [Multiple domains](https://cursor.com/docs/account/teams/sso\#multiple-domains)

To handle multiple domains in your organization:

1. **Verify each domain separately** in Cursor through the domain verification settings
2. **Configure each domain** in your identity provider
3. Each domain needs to go through the verification process independently

## [Troubleshooting](https://cursor.com/docs/account/teams/sso\#troubleshooting)

If issues occur:

- Verify domain is verified in Cursor
- Ensure SAML attributes are properly mapped
- Check SSO is enabled in admin dashboard
- Match first and last names between identity provider and Cursor
- Check provider-specific guides above
- Contact [hi@cursor.com](mailto:hi@cursor.com) if issues persist

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