[Skip to main content](https://code.claude.com/docs/en/llm-gateway#content-area)

[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/light.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=d535f2e20f53cd911acc59ad1b64b2e0)![dark logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/dark.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=28e49a2ffe69101f4aae9bfa70b393d0)](https://code.claude.com/docs)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Deployment

LLM gateway configuration

[Getting started](https://code.claude.com/docs/en/overview) [Build with Claude Code](https://code.claude.com/docs/en/sub-agents) [Deployment](https://code.claude.com/docs/en/third-party-integrations) [Administration](https://code.claude.com/docs/en/setup) [Configuration](https://code.claude.com/docs/en/settings) [Reference](https://code.claude.com/docs/en/cli-reference) [Resources](https://code.claude.com/docs/en/legal-and-compliance)

On this page

- [Gateway requirements](https://code.claude.com/docs/en/llm-gateway#gateway-requirements)
- [Configuration](https://code.claude.com/docs/en/llm-gateway#configuration)
- [Model selection](https://code.claude.com/docs/en/llm-gateway#model-selection)
- [LiteLLM configuration](https://code.claude.com/docs/en/llm-gateway#litellm-configuration)
- [Prerequisites](https://code.claude.com/docs/en/llm-gateway#prerequisites)
- [Basic LiteLLM setup](https://code.claude.com/docs/en/llm-gateway#basic-litellm-setup)
- [Authentication methods](https://code.claude.com/docs/en/llm-gateway#authentication-methods)
- [Unified endpoint (recommended)](https://code.claude.com/docs/en/llm-gateway#unified-endpoint-recommended)
- [Provider-specific pass-through endpoints (alternative)](https://code.claude.com/docs/en/llm-gateway#provider-specific-pass-through-endpoints-alternative)
- [Additional resources](https://code.claude.com/docs/en/llm-gateway#additional-resources)

LLM gateways provide a centralized proxy layer between Claude Code and model providers, often providing:

- **Centralized authentication** \- Single point for API key management
- **Usage tracking** \- Monitor usage across teams and projects
- **Cost controls** \- Implement budgets and rate limits
- **Audit logging** \- Track all model interactions for compliance
- **Model routing** \- Switch between providers without code changes

## [​](https://code.claude.com/docs/en/llm-gateway\#gateway-requirements)  Gateway requirements

For an LLM gateway to work with Claude Code, it must meet the following requirements:**API format**The gateway must expose to clients at least one of the following API formats:

1. **Anthropic Messages**: `/v1/messages`, `/v1/messages/count_tokens`   - Must forward request headers: `anthropic-beta`, `anthropic-version`
2. **Bedrock InvokeModel**: `/invoke`, `/invoke-with-response-stream`   - Must preserve request body fields: `anthropic_beta`, `anthropic_version`
3. **Vertex rawPredict**: `:rawPredict`, `:streamRawPredict`, `/count-tokens:rawPredict`   - Must forward request headers: `anthropic-beta`, `anthropic-version`

Failure to forward headers or preserve body fields may result in reduced functionality or inability to use Claude Code features.

Claude Code determines which features to enable based on the API format. When using the Anthropic Messages format with Bedrock or Vertex, you may need to set environment variable `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1`.

## [​](https://code.claude.com/docs/en/llm-gateway\#configuration)  Configuration

### [​](https://code.claude.com/docs/en/llm-gateway\#model-selection)  Model selection

By default, Claude Code will use standard model names for the selected API format.If you have configured custom model names in your gateway, use the environment variables documented in [Model configuration](https://code.claude.com/docs/en/model-config) to match your custom names.

## [​](https://code.claude.com/docs/en/llm-gateway\#litellm-configuration)  LiteLLM configuration

LiteLLM is a third-party proxy service. Anthropic doesn’t endorse, maintain, or audit LiteLLM’s security or functionality. This guide is provided for informational purposes and may become outdated. Use at your own discretion.

### [​](https://code.claude.com/docs/en/llm-gateway\#prerequisites)  Prerequisites

- Claude Code updated to the latest version
- LiteLLM Proxy Server deployed and accessible
- Access to Claude models through your chosen provider

### [​](https://code.claude.com/docs/en/llm-gateway\#basic-litellm-setup)  Basic LiteLLM setup

**Configure Claude Code**:

#### [​](https://code.claude.com/docs/en/llm-gateway\#authentication-methods)  Authentication methods

##### Static API key

Simplest method using a fixed API key:

Report incorrect code

Copy

Ask AI

```
# Set in environment
export ANTHROPIC_AUTH_TOKEN=sk-litellm-static-key

# Or in Claude Code settings
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "sk-litellm-static-key"
  }
}
```

This value will be sent as the `Authorization` header.

##### Dynamic API key with helper

For rotating keys or per-user authentication:

1. Create an API key helper script:

Report incorrect code

Copy

Ask AI

```
#!/bin/bash
# ~/bin/get-litellm-key.sh

# Example: Fetch key from vault
vault kv get -field=api_key secret/litellm/claude-code

# Example: Generate JWT token
jwt encode \
  --secret="${JWT_SECRET}" \
  --exp="+1h" \
  '{"user":"'${USER}'","team":"engineering"}'
```

2. Configure Claude Code settings to use the helper:

Report incorrect code

Copy

Ask AI

```
{
  "apiKeyHelper": "~/bin/get-litellm-key.sh"
}
```

3. Set token refresh interval:

Report incorrect code

Copy

Ask AI

```
# Refresh every hour (3600000 ms)
export CLAUDE_CODE_API_KEY_HELPER_TTL_MS=3600000
```

This value will be sent as `Authorization` and `X-Api-Key` headers. The `apiKeyHelper` has lower precedence than `ANTHROPIC_AUTH_TOKEN` or `ANTHROPIC_API_KEY`.

#### [​](https://code.claude.com/docs/en/llm-gateway\#unified-endpoint-recommended)  Unified endpoint (recommended)

Using LiteLLM’s [Anthropic format endpoint](https://docs.litellm.ai/docs/anthropic_unified):

Report incorrect code

Copy

Ask AI

```
export ANTHROPIC_BASE_URL=https://litellm-server:4000
```

**Benefits of the unified endpoint over pass-through endpoints:**

- Load balancing
- Fallbacks
- Consistent support for cost tracking and end-user tracking

#### [​](https://code.claude.com/docs/en/llm-gateway\#provider-specific-pass-through-endpoints-alternative)  Provider-specific pass-through endpoints (alternative)

##### Claude API through LiteLLM

Using [pass-through endpoint](https://docs.litellm.ai/docs/pass_through/anthropic_completion):

Report incorrect code

Copy

Ask AI

```
export ANTHROPIC_BASE_URL=https://litellm-server:4000/anthropic
```

##### Amazon Bedrock through LiteLLM

Using [pass-through endpoint](https://docs.litellm.ai/docs/pass_through/bedrock):

Report incorrect code

Copy

Ask AI

```
export ANTHROPIC_BEDROCK_BASE_URL=https://litellm-server:4000/bedrock
export CLAUDE_CODE_SKIP_BEDROCK_AUTH=1
export CLAUDE_CODE_USE_BEDROCK=1
```

##### Google Vertex AI through LiteLLM

Using [pass-through endpoint](https://docs.litellm.ai/docs/pass_through/vertex_ai):

Report incorrect code

Copy

Ask AI

```
export ANTHROPIC_VERTEX_BASE_URL=https://litellm-server:4000/vertex_ai/v1
export ANTHROPIC_VERTEX_PROJECT_ID=your-gcp-project-id
export CLAUDE_CODE_SKIP_VERTEX_AUTH=1
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=us-east5
```

For more detailed information, refer to the [LiteLLM documentation](https://docs.litellm.ai/).

## [​](https://code.claude.com/docs/en/llm-gateway\#additional-resources)  Additional resources

- [LiteLLM documentation](https://docs.litellm.ai/)
- [Claude Code settings](https://code.claude.com/docs/en/settings)
- [Enterprise network configuration](https://code.claude.com/docs/en/network-config)
- [Third-party integrations overview](https://code.claude.com/docs/en/third-party-integrations)

Was this page helpful?

YesNo

[Network configuration](https://code.claude.com/docs/en/network-config) [Development containers](https://code.claude.com/docs/en/devcontainer)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.