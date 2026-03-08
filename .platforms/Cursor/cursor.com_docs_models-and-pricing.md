[Skip to main content](https://cursor.com/docs/models-and-pricing#main-content)

## Command Palette

Search for a command to run...

## Get Started

[Welcome](https://cursor.com/docs) [Quickstart](https://cursor.com/docs/get-started/quickstart)
Models & Pricing

[Overview](https://cursor.com/docs/models-and-pricing)

[Claude 4.6 Sonnet](https://cursor.com/docs/models/claude-4-6-sonnet)

[Claude 4.6 Opus](https://cursor.com/docs/models/claude-opus-4-6)

[Gemini 3.1 Pro](https://cursor.com/docs/models/gemini-3-1-pro)

[Gemini 3 Flash](https://cursor.com/docs/models/gemini-3-flash)

[GPT-5.4](https://cursor.com/docs/models/gpt-5-4)

[GPT-5.3 Codex](https://cursor.com/docs/models/gpt-5-3-codex)

[Grok Code](https://cursor.com/docs/models/grok-code)

[Composer 1.5](https://cursor.com/docs/models/cursor-composer-1-5)

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

# Models & Pricing

Cursor supports all frontier coding models from OpenAI, Anthropic, Google, and more. Every individual plan includes two usage pools so you can pick the right balance of intelligence, speed, and cost.

## [Usage pools](https://cursor.com/docs/models-and-pricing\#usage-pools)

There are two separate usage pools, each resetting with your monthly billing cycle:

- **Auto + Composer**: Significantly more included usage when Auto or Composer 1.5 is selected. Designed for everyday agentic coding at a lower cost.
- **API**: Charged at the model's API price. Individual plans include at least $20 of API usage each month (more on higher tiers) with the option to pay for additional usage as needed.

Both pools are visible in your editor settings and on your [usage dashboard](https://cursor.com/dashboard?tab=usage).

## [Auto + Composer pool](https://cursor.com/docs/models-and-pricing\#auto-composer-pool)

Auto allows Cursor to select models that balance intelligence, cost efficiency, and reliability. It is useful for everyday tasks.

Composer 1.5 is Cursor's own model, trained to be highly capable for agentic coding. Both Auto and Composer 1.5 draw from this pool.

### [Auto pricing](https://cursor.com/docs/models-and-pricing\#auto-pricing)

| Token type | Price per 1M tokens |
| --- | --- |
| Input + Cache Write | $1.25 |
| Output | $6.00 |
| Cache Read | $0.25 |

## [API pool](https://cursor.com/docs/models-and-pricing\#api-pool)

When you select a specific model (or use Premium routing), usage is drawn from the API pool at that model's API rate.

### [Model pricing](https://cursor.com/docs/models-and-pricing\#model-pricing)

All prices are per million tokens, sourced from each provider's API pricing:

| Name | Input | Cache Write | Cache Read | Output |
| --- | --- | --- | --- | --- |
| ![Anthropic](https://cursor.com/docs-static/images/providers/anthropic-dark.svg)![Anthropic](https://cursor.com/docs-static/images/providers/anthropic-light.svg)<br>[Claude 4.6 Opus](https://cursor.com/docs/models/claude-opus-4-6) | $5 | $6.25 | $0.5 | $25 |
| ![Anthropic](https://cursor.com/docs-static/images/providers/anthropic-dark.svg)![Anthropic](https://cursor.com/docs-static/images/providers/anthropic-light.svg)<br>[Claude 4.6 Sonnet](https://cursor.com/docs/models/claude-4-6-sonnet) | $3 | $3.75 | $0.3 | $15 |
| ![Cursor](https://cursor.com/docs-static/images/providers/cursor.svg)<br>[Composer 1.5](https://cursor.com/docs/models/cursor-composer-1-5) | $3.5 | - | $0.35 | $17.5 |
| ![Google](https://cursor.com/docs-static/images/providers/google.svg)<br>[Gemini 3 Flash](https://cursor.com/docs/models/gemini-3-flash) | $0.5 | - | $0.05 | $3 |
| ![Google](https://cursor.com/docs-static/images/providers/google.svg)<br>[Gemini 3.1 Pro](https://cursor.com/docs/models/gemini-3-1-pro) | $2 | - | $0.2 | $12 |
| ![OpenAI](https://cursor.com/docs-static/images/providers/openai-dark.svg)![OpenAI](https://cursor.com/docs-static/images/providers/openai-light.svg)<br>[GPT-5.3 Codex](https://cursor.com/docs/models/gpt-5-3-codex) | $1.75 | - | $0.175 | $14 |
| ![OpenAI](https://cursor.com/docs-static/images/providers/openai-dark.svg)![OpenAI](https://cursor.com/docs-static/images/providers/openai-light.svg)<br>[GPT-5.4](https://cursor.com/docs/models/gpt-5-4) | $2.5 | - | $0.25 | $15 |
| ![xAI](https://cursor.com/docs-static/images/providers/xai-dark.svg)![xAI](https://cursor.com/docs-static/images/providers/xai-light.svg)<br>[Grok Code](https://cursor.com/docs/models/grok-code) | $0.2 | - | $0.02 | $1.5 |

Show more models

### [Premium routing](https://cursor.com/docs/models-and-pricing\#premium-routing)

Premium allows Cursor to select the most capable models for you, recommended for the most complex tasks. The Cursor team selects Premium models based on internal benchmarks, evaluations, and user feedback.

Premium pricing is based on the selected model's API rate. Check your [usage page](https://cursor.com/dashboard?tab=usage) to see cost and model selection at the request level.

## [Plans](https://cursor.com/docs/models-and-pricing\#plans)

All individual plans include unlimited tab completions, extended agent usage limits on all models, access to Bugbot, and access to Cloud Agents.

| Plan | Price | API usage included | Auto + Composer |
| --- | --- | --- | --- |
| **Pro** | $20/mo | $20 | Generous included usage |
| **Pro Plus** | $60/mo | $70 | Generous included usage |
| **Ultra** | $200/mo | $400 | Generous included usage |

Since different models have different API costs, your model selection affects how quickly your included usage is consumed.

### [How much usage do I need?](https://cursor.com/docs/models-and-pricing\#how-much-usage-do-i-need)

- **Daily Tab users**: Always stay within $20
- **Limited Agent users**: Often stay within the included $20
- **Daily Agent users**: Typically $60–$100/mo total usage
- **Power users (multiple agents/automation)**: Often $200+/mo total usage

### [What happens when I reach my limit?](https://cursor.com/docs/models-and-pricing\#what-happens-when-i-reach-my-limit)

When you exceed your included monthly usage, you can either:

- **Add on-demand usage**: Continue at the same API rates with pay-as-you-go billing
- **Upgrade your plan**: Move to a higher tier for more included usage

On-demand usage is billed monthly at the same rates. Requests are never downgraded in quality or speed.

### [Teams](https://cursor.com/docs/models-and-pricing\#teams)

There are two teams plans: Teams ($40/user/mo) and Enterprise (Custom).

Team plans provide additional features like privacy mode enforcement, admin dashboard with usage stats, centralized team billing, and SAML/OIDC SSO.

We recommend Teams for any customer that is happy self-serving. We recommend [Enterprise](https://cursor.com/contact-sales) for customers that need priority support, pooled usage, invoicing, SCIM, or advanced security controls.

Learn more about [Teams pricing](https://cursor.com/docs/account/teams/pricing).

## [Max Mode](https://cursor.com/docs/models-and-pricing\#max-mode)

Max Mode extends the context window to the maximum a model supports. More context gives models deeper understanding of your codebase, leading to better results on complex tasks. The models table above shows each model's maximum context size.

Max Mode uses token-based pricing at the model's API rate plus a 20% upcharge, so it consumes usage faster than the default context window.

## [FAQ](https://cursor.com/docs/models-and-pricing\#faq)

### Where are models hosted?

Models are hosted on US, Canada, & Iceland based infrastructure by the model's provider, a trusted partner, or Cursor directly.

When Privacy Mode is enabled, neither Cursor nor model providers store your data. All data is deleted after each request. For details see our [Privacy Policy](https://cursor.com/privacy) and [Security](https://cursor.com/security) pages.

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