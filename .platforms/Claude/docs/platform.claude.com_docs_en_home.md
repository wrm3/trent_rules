Home

Claude Developer Platform

# Start building  with Claude

Everything you need to integrate Claude into your applications. From first API call to production.

What do you want to build?

⌘K

[Quickstart](https://platform.claude.com/docs/en/get-started) [Get API key](https://platform.claude.com/settings/keys) [API reference](https://platform.claude.com/docs/en/api)

PythonTypeScriptGoJavaRubyPHPC#cURL

```
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
  model="claude-sonnet-4-6",
  max_tokens=1024,
  messages=[{\
    "role": "user",\
    "content": "Hello, Claude"\
  }]
)
print(message.content[0].text)
```

Platform

## Choose how you build

Pick the developer surface that matches your approach, and the infrastructure that fits your stack.

### Claude API

Send a request, get a response. You construct every turn, manage conversation state, and write your own tool loop.

[Quickstart](https://platform.claude.com/docs/en/get-started) [API reference](https://platform.claude.com/docs/en/api/messages/create) [Client SDKs](https://platform.claude.com/docs/en/api/client-sdks)

### Agent SDK

Claude Code as a library. Give Claude a task and the SDK runs the loop with built-in file, shell, and web tools.

[Agent SDK quickstart](https://platform.claude.com/docs/en/agent-sdk/quickstart) [TypeScript Agent SDK](https://platform.claude.com/docs/en/agent-sdk/typescript) [Python Agent SDK](https://platform.claude.com/docs/en/agent-sdk/python)

[AWS Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock) [Google Cloud Vertex AI](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai) [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)

Developer journey

## From idea to production

Follow the lifecycle or jump to what you need.

1. 1



### Get started







[Quickstart](https://platform.claude.com/docs/en/get-started) [Get API key](https://platform.claude.com/settings/keys) [Choose a model](https://platform.claude.com/docs/en/about-claude/models/overview) [Install an SDK](https://platform.claude.com/docs/en/api/client-sdks) [Try the Workbench](https://platform.claude.com/workbench)

2. 2



### Build







[Messages API](https://platform.claude.com/docs/en/api/messages/create) [Extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) [Vision](https://platform.claude.com/docs/en/build-with-claude/vision) [Tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) [Web search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool) [Code execution](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool) [Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) [Streaming](https://platform.claude.com/docs/en/build-with-claude/streaming)

3. 3



### Evaluate & ship







[Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) [Run evals](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests) [Batch testing](https://platform.claude.com/docs/en/build-with-claude/batch-processing) [Safety & guardrails](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency) [Rate limits & errors](https://platform.claude.com/docs/en/api/rate-limits) [Cost optimization](https://platform.claude.com/docs/en/about-claude/pricing)

4. 4



### Operate







[Workspaces & admin](https://platform.claude.com/docs/en/build-with-claude/workspaces) [API key management](https://platform.claude.com/settings/keys) [Usage monitoring](https://platform.claude.com/docs/en/build-with-claude/usage-cost-api) [Model migration](https://platform.claude.com/docs/en/about-claude/models/migration-guide)


Models

## The Claude model family

Choose the right model for your use case.

Most capable

[Opus 4.6](https://platform.claude.com/docs/en/about-claude/models/overview) claude-opus-4-6

Best for complex analysis, coding, and creative tasks requiring deep reasoning.

Best balance

[Sonnet 4.6](https://platform.claude.com/docs/en/about-claude/models/overview) claude-sonnet-4-6

Ideal balance of intelligence and speed for most production workloads.

Fastest

[Haiku 4.5](https://platform.claude.com/docs/en/about-claude/models/overview) claude-haiku-4-5

Lightning-fast responses for high-volume, latency-sensitive applications.

Resources

## Keep learning

[Courses\\
\\
Interactive courses to master Claude.](https://anthropic.skilljar.com/) [Cookbook\\
\\
Code samples and patterns.](https://platform.claude.com/cookbooks) [Quickstarts\\
\\
Deployable starter apps.](https://github.com/anthropics/anthropic-quickstarts) [What's new\\
\\
Latest features and updates.](https://platform.claude.com/docs/en/release-notes/overview) [Claude Code\\
\\
An agentic coding assistant in your terminal.](https://code.claude.com/docs/en/overview)

Ask Docs
![Chat avatar](https://platform.claude.com/docs/images/book-icon-light.svg)

a.claude.ai

# a.claude.ai is blocked

**a.claude.ai** refused to connect.

ERR\_BLOCKED\_BY\_RESPONSE

**a.claude.ai** refused to connect.

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)