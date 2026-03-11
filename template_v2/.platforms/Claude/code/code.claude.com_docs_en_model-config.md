[Skip to main content](https://code.claude.com/docs/en/model-config#content-area)

[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/light.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=d535f2e20f53cd911acc59ad1b64b2e0)![dark logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/dark.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=28e49a2ffe69101f4aae9bfa70b393d0)](https://code.claude.com/docs)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Configuration

Model configuration

[Getting started](https://code.claude.com/docs/en/overview) [Build with Claude Code](https://code.claude.com/docs/en/sub-agents) [Deployment](https://code.claude.com/docs/en/third-party-integrations) [Administration](https://code.claude.com/docs/en/setup) [Configuration](https://code.claude.com/docs/en/settings) [Reference](https://code.claude.com/docs/en/cli-reference) [Resources](https://code.claude.com/docs/en/legal-and-compliance)

On this page

- [Available models](https://code.claude.com/docs/en/model-config#available-models)
- [Model aliases](https://code.claude.com/docs/en/model-config#model-aliases)
- [Setting your model](https://code.claude.com/docs/en/model-config#setting-your-model)
- [Restrict model selection](https://code.claude.com/docs/en/model-config#restrict-model-selection)
- [Default model behavior](https://code.claude.com/docs/en/model-config#default-model-behavior)
- [Control the model users run on](https://code.claude.com/docs/en/model-config#control-the-model-users-run-on)
- [Merge behavior](https://code.claude.com/docs/en/model-config#merge-behavior)
- [Special model behavior](https://code.claude.com/docs/en/model-config#special-model-behavior)
- [default model setting](https://code.claude.com/docs/en/model-config#default-model-setting)
- [opusplan model setting](https://code.claude.com/docs/en/model-config#opusplan-model-setting)
- [Adjust effort level](https://code.claude.com/docs/en/model-config#adjust-effort-level)
- [Extended context](https://code.claude.com/docs/en/model-config#extended-context)
- [Checking your current model](https://code.claude.com/docs/en/model-config#checking-your-current-model)
- [Environment variables](https://code.claude.com/docs/en/model-config#environment-variables)
- [Pin models for third-party deployments](https://code.claude.com/docs/en/model-config#pin-models-for-third-party-deployments)
- [Prompt caching configuration](https://code.claude.com/docs/en/model-config#prompt-caching-configuration)

## [​](https://code.claude.com/docs/en/model-config\#available-models)  Available models

For the `model` setting in Claude Code, you can configure either:

- A **model alias**
- A **model name**
  - Anthropic API: A full **[model name](https://platform.claude.com/docs/en/about-claude/models/overview)**
  - Bedrock: an inference profile ARN
  - Foundry: a deployment name
  - Vertex: a version name

### [​](https://code.claude.com/docs/en/model-config\#model-aliases)  Model aliases

Model aliases provide a convenient way to select model settings without
remembering exact version numbers:

| Model alias | Behavior |
| --- | --- |
| **`default`** | Recommended model setting, depending on your account type |
| **`sonnet`** | Uses the latest Sonnet model (currently Sonnet 4.6) for daily coding tasks |
| **`opus`** | Uses the latest Opus model (currently Opus 4.6) for complex reasoning tasks |
| **`haiku`** | Uses the fast and efficient Haiku model for simple tasks |
| **`sonnet[1m]`** | Uses Sonnet with a [1 million token context window](https://platform.claude.com/docs/en/build-with-claude/context-windows#1m-token-context-window) for long sessions |
| **`opusplan`** | Special mode that uses `opus` during plan mode, then switches to `sonnet` for execution |

Aliases always point to the latest version. To pin to a specific version, use the full model name (for example, `claude-opus-4-6`) or set the corresponding environment variable like `ANTHROPIC_DEFAULT_OPUS_MODEL`.

### [​](https://code.claude.com/docs/en/model-config\#setting-your-model)  Setting your model

You can configure your model in several ways, listed in order of priority:

1. **During session** \- Use `/model <alias|name>` to switch models mid-session
2. **At startup** \- Launch with `claude --model <alias|name>`
3. **Environment variable** \- Set `ANTHROPIC_MODEL=<alias|name>`
4. **Settings** \- Configure permanently in your settings file using the `model`
field.

Example usage:

Report incorrect code

Copy

Ask AI

```
# Start with Opus
claude --model opus

# Switch to Sonnet during session
/model sonnet
```

Example settings file:

Report incorrect code

Copy

Ask AI

```
{
    "permissions": {
        ...
    },
    "model": "opus"
}
```

## [​](https://code.claude.com/docs/en/model-config\#restrict-model-selection)  Restrict model selection

Enterprise administrators can use `availableModels` in [managed or policy settings](https://code.claude.com/docs/en/settings#settings-files) to restrict which models users can select.When `availableModels` is set, users cannot switch to models not in the list via `/model`, `--model` flag, Config tool, or `ANTHROPIC_MODEL` environment variable.

Report incorrect code

Copy

Ask AI

```
{
  "availableModels": ["sonnet", "haiku"]
}
```

### [​](https://code.claude.com/docs/en/model-config\#default-model-behavior)  Default model behavior

The Default option in the model picker is not affected by `availableModels`. It always remains available and represents the system’s runtime default [based on the user’s subscription tier](https://code.claude.com/docs/en/model-config#default-model-setting).Even with `availableModels: []`, users can still use Claude Code with the Default model for their tier.

### [​](https://code.claude.com/docs/en/model-config\#control-the-model-users-run-on)  Control the model users run on

To fully control the model experience, use `availableModels` together with the `model` setting:

- **availableModels**: restricts what users can switch to
- **model**: sets the explicit model override, taking precedence over the Default

This example ensures all users run Sonnet 4.6 and can only choose between Sonnet and Haiku:

Report incorrect code

Copy

Ask AI

```
{
  "model": "sonnet",
  "availableModels": ["sonnet", "haiku"]
}
```

### [​](https://code.claude.com/docs/en/model-config\#merge-behavior)  Merge behavior

When `availableModels` is set at multiple levels, such as user settings and project settings, arrays are merged and deduplicated. To enforce a strict allowlist, set `availableModels` in managed or policy settings which take highest priority.

## [​](https://code.claude.com/docs/en/model-config\#special-model-behavior)  Special model behavior

### [​](https://code.claude.com/docs/en/model-config\#default-model-setting)  `default` model setting

The behavior of `default` depends on your account type:

- **Max and Team Premium**: defaults to Opus 4.6
- **Pro and Team Standard**: defaults to Sonnet 4.6
- **Enterprise**: Opus 4.6 is available but not the default

Claude Code may automatically fall back to Sonnet if you hit a usage threshold with Opus.

### [​](https://code.claude.com/docs/en/model-config\#opusplan-model-setting)  `opusplan` model setting

The `opusplan` model alias provides an automated hybrid approach:

- **In plan mode** \- Uses `opus` for complex reasoning and architecture
decisions
- **In execution mode** \- Automatically switches to `sonnet` for code generation
and implementation

This gives you the best of both worlds: Opus’s superior reasoning for planning,
and Sonnet’s efficiency for execution.

### [​](https://code.claude.com/docs/en/model-config\#adjust-effort-level)  Adjust effort level

[Effort levels](https://platform.claude.com/docs/en/build-with-claude/effort) control adaptive reasoning, which dynamically allocates thinking based on task complexity. Lower effort is faster and cheaper for straightforward tasks, while higher effort provides deeper reasoning for complex problems.Three levels are available: **low**, **medium**, and **high**. Opus 4.6 defaults to medium effort for Max and Team subscribers.**Setting effort:**

- **In `/model`**: use left/right arrow keys to adjust the effort slider when selecting a model
- **Environment variable**: set `CLAUDE_CODE_EFFORT_LEVEL=low|medium|high`
- **Settings**: set `effortLevel` in your settings file

Effort is supported on Opus 4.6 and Sonnet 4.6. The effort slider appears in `/model` when a supported model is selected. The current effort level is also displayed next to the logo and spinner (for example, “with low effort”), so you can confirm which setting is active without opening `/model`.To disable adaptive reasoning on Opus 4.6 and Sonnet 4.6 and revert to the previous fixed thinking budget, set `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1`. When disabled, these models use the fixed budget controlled by `MAX_THINKING_TOKENS`. See [environment variables](https://code.claude.com/docs/en/settings#environment-variables).

### [​](https://code.claude.com/docs/en/model-config\#extended-context)  Extended context

Opus 4.6 and Sonnet 4.6 support a [1 million token context window](https://platform.claude.com/docs/en/build-with-claude/context-windows#1m-token-context-window) for long sessions with large codebases.

The 1M context window is currently in beta. Features, pricing, and availability may change.

Extended context is available for:

- **API and pay-as-you-go users**: full access to 1M context
- **Pro, Max, Teams, and Enterprise subscribers**: available with [extra usage](https://support.claude.com/en/articles/12429409-extra-usage-for-paid-claude-plans) enabled

To disable 1M context entirely, set `CLAUDE_CODE_DISABLE_1M_CONTEXT=1`. This removes 1M model variants from the model picker. See [environment variables](https://code.claude.com/docs/en/settings#environment-variables).Selecting a 1M model does not immediately change billing. Your session uses standard rates until it exceeds 200K tokens of context. Beyond 200K tokens, requests are charged at [long-context pricing](https://platform.claude.com/docs/en/about-claude/pricing#long-context-pricing) with dedicated [rate limits](https://platform.claude.com/docs/en/api/rate-limits#long-context-rate-limits). For subscribers, tokens beyond 200K are billed as extra usage rather than through the subscription.If your account supports 1M context, the option appears in the model picker (`/model`) in the latest versions of Claude Code. If you don’t see it, try restarting your session.You can also use the `[1m]` suffix with model aliases or full model names:

Report incorrect code

Copy

Ask AI

```
# Use the sonnet[1m] alias
/model sonnet[1m]

# Or append [1m] to a full model name
/model claude-sonnet-4-6[1m]
```

## [​](https://code.claude.com/docs/en/model-config\#checking-your-current-model)  Checking your current model

You can see which model you’re currently using in several ways:

1. In [status line](https://code.claude.com/docs/en/statusline) (if configured)
2. In `/status`, which also displays your account information.

## [​](https://code.claude.com/docs/en/model-config\#environment-variables)  Environment variables

You can use the following environment variables, which must be full **model**
**names** (or equivalent for your API provider), to control the model names that the aliases map to.

| Environment variable | Description |
| --- | --- |
| `ANTHROPIC_DEFAULT_OPUS_MODEL` | The model to use for `opus`, or for `opusplan` when Plan Mode is active. |
| `ANTHROPIC_DEFAULT_SONNET_MODEL` | The model to use for `sonnet`, or for `opusplan` when Plan Mode is not active. |
| `ANTHROPIC_DEFAULT_HAIKU_MODEL` | The model to use for `haiku`, or [background functionality](https://code.claude.com/docs/en/costs#background-token-usage) |
| `CLAUDE_CODE_SUBAGENT_MODEL` | The model to use for [subagents](https://code.claude.com/docs/en/sub-agents) |

Note: `ANTHROPIC_SMALL_FAST_MODEL` is deprecated in favor of
`ANTHROPIC_DEFAULT_HAIKU_MODEL`.

### [​](https://code.claude.com/docs/en/model-config\#pin-models-for-third-party-deployments)  Pin models for third-party deployments

When deploying Claude Code through [Bedrock](https://code.claude.com/docs/en/amazon-bedrock), [Vertex AI](https://code.claude.com/docs/en/google-vertex-ai), or [Foundry](https://code.claude.com/docs/en/microsoft-foundry), pin model versions before rolling out to users.Without pinning, Claude Code uses model aliases (`sonnet`, `opus`, `haiku`) that resolve to the latest version. When Anthropic releases a new model, users whose accounts don’t have the new version enabled will break silently.

Set all three model environment variables to specific version IDs as part of your initial setup. Skipping this step means a Claude Code update can break your users without any action on your part.

Use the following environment variables with version-specific model IDs for your provider:

| Provider | Example |
| --- | --- |
| Bedrock | `export ANTHROPIC_DEFAULT_OPUS_MODEL='us.anthropic.claude-opus-4-6-v1'` |
| Vertex AI | `export ANTHROPIC_DEFAULT_OPUS_MODEL='claude-opus-4-6'` |
| Foundry | `export ANTHROPIC_DEFAULT_OPUS_MODEL='claude-opus-4-6'` |

Apply the same pattern for `ANTHROPIC_DEFAULT_SONNET_MODEL` and `ANTHROPIC_DEFAULT_HAIKU_MODEL`. For current and legacy model IDs across all providers, see [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview). To upgrade users to a new model version, update these environment variables and redeploy.

The `settings.availableModels` allowlist still applies when using third-party providers. Filtering matches on the model alias (`opus`, `sonnet`, `haiku`), not the provider-specific model ID.

### [​](https://code.claude.com/docs/en/model-config\#prompt-caching-configuration)  Prompt caching configuration

Claude Code automatically uses [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) to optimize performance and reduce costs. You can disable prompt caching globally or for specific model tiers:

| Environment variable | Description |
| --- | --- |
| `DISABLE_PROMPT_CACHING` | Set to `1` to disable prompt caching for all models (takes precedence over per-model settings) |
| `DISABLE_PROMPT_CACHING_HAIKU` | Set to `1` to disable prompt caching for Haiku models only |
| `DISABLE_PROMPT_CACHING_SONNET` | Set to `1` to disable prompt caching for Sonnet models only |
| `DISABLE_PROMPT_CACHING_OPUS` | Set to `1` to disable prompt caching for Opus models only |

These environment variables give you fine-grained control over prompt caching behavior. The global `DISABLE_PROMPT_CACHING` setting takes precedence over the model-specific settings, allowing you to quickly disable all caching when needed. The per-model settings are useful for selective control, such as when debugging specific models or working with cloud providers that may have different caching implementations.

Was this page helpful?

YesNo

[Terminal configuration](https://code.claude.com/docs/en/terminal-config) [Speed up responses with fast mode](https://code.claude.com/docs/en/fast-mode)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.