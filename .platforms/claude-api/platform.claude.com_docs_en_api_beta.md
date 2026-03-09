API Reference

Beta

Copy page

# Beta

##### ModelsExpand Collapse

AnthropicBeta = stringor"message-batches-2024-09-24"or"prompt-caching-2024-07-31"or"computer-use-2024-10-22"or17 more

Accepts one of the following:

UnionMember0 = string

UnionMember1 = "message-batches-2024-09-24"or"prompt-caching-2024-07-31"or"computer-use-2024-10-22"or17 more

Accepts one of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

BetaAPIError = object {message, type}

message: string

type: "api\_error"

BetaAuthenticationError = object {message, type}

message: string

type: "authentication\_error"

BetaBillingError = object {message, type}

message: string

type: "billing\_error"

BetaError = [BetaInvalidRequestError](https://platform.claude.com/docs/en/api/beta#beta_invalid_request_error) { message, type } or[BetaAuthenticationError](https://platform.claude.com/docs/en/api/beta#beta_authentication_error) { message, type } or[BetaBillingError](https://platform.claude.com/docs/en/api/beta#beta_billing_error) { message, type } or6 more

Accepts one of the following:

BetaInvalidRequestError = object {message, type}

message: string

type: "invalid\_request\_error"

BetaAuthenticationError = object {message, type}

message: string

type: "authentication\_error"

BetaBillingError = object {message, type}

message: string

type: "billing\_error"

BetaPermissionError = object {message, type}

message: string

type: "permission\_error"

BetaNotFoundError = object {message, type}

message: string

type: "not\_found\_error"

BetaRateLimitError = object {message, type}

message: string

type: "rate\_limit\_error"

BetaGatewayTimeoutError = object {message, type}

message: string

type: "timeout\_error"

BetaAPIError = object {message, type}

message: string

type: "api\_error"

BetaOverloadedError = object {message, type}

message: string

type: "overloaded\_error"

BetaErrorResponse = object {error, request\_id, type}

error: [BetaError](https://platform.claude.com/docs/en/api/beta#beta_error)

Accepts one of the following:

BetaInvalidRequestError = object {message, type}

message: string

type: "invalid\_request\_error"

BetaAuthenticationError = object {message, type}

message: string

type: "authentication\_error"

BetaBillingError = object {message, type}

message: string

type: "billing\_error"

BetaPermissionError = object {message, type}

message: string

type: "permission\_error"

BetaNotFoundError = object {message, type}

message: string

type: "not\_found\_error"

BetaRateLimitError = object {message, type}

message: string

type: "rate\_limit\_error"

BetaGatewayTimeoutError = object {message, type}

message: string

type: "timeout\_error"

BetaAPIError = object {message, type}

message: string

type: "api\_error"

BetaOverloadedError = object {message, type}

message: string

type: "overloaded\_error"

request\_id: string

type: "error"

BetaGatewayTimeoutError = object {message, type}

message: string

type: "timeout\_error"

BetaInvalidRequestError = object {message, type}

message: string

type: "invalid\_request\_error"

BetaNotFoundError = object {message, type}

message: string

type: "not\_found\_error"

BetaOverloadedError = object {message, type}

message: string

type: "overloaded\_error"

BetaPermissionError = object {message, type}

message: string

type: "permission\_error"

BetaRateLimitError = object {message, type}

message: string

type: "rate\_limit\_error"

#### BetaModels

##### [List Models](https://platform.claude.com/docs/en/api/beta/models/list)

GET/v1/models

##### [Get a Model](https://platform.claude.com/docs/en/api/beta/models/retrieve)

GET/v1/models/{model\_id}

##### ModelsExpand Collapse

BetaModelInfo = object {id, created\_at, display\_name, type}

id: string

Unique model identifier.

created\_at: string

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

display\_name: string

A human-readable name for the model.

type: "model"

Object type.

For Models, this is always `"model"`.

#### BetaMessages

##### [Create a Message](https://platform.claude.com/docs/en/api/beta/messages/create)

POST/v1/messages

##### [Count tokens in a Message](https://platform.claude.com/docs/en/api/beta/messages/count_tokens)

POST/v1/messages/count\_tokens

##### ModelsExpand Collapse

BetaAllThinkingTurns = object {type}

type: "all"

BetaBase64ImageSource = object {data, media\_type, type}

data: string

media\_type: "image/jpeg"or"image/png"or"image/gif"or"image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaBase64PDFSource = object {data, media\_type, type}

data: string

media\_type: "application/pdf"

type: "base64"

BetaBashCodeExecutionOutputBlock = object {file\_id, type}

file\_id: string

type: "bash\_code\_execution\_output"

BetaBashCodeExecutionOutputBlockParam = object {file\_id, type}

file\_id: string

type: "bash\_code\_execution\_output"

BetaBashCodeExecutionResultBlock = object {content, return\_code, stderr, 2 more}

content: array of [BetaBashCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_output_block) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

BetaBashCodeExecutionResultBlockParam = object {content, return\_code, stderr, 2 more}

content: array of [BetaBashCodeExecutionOutputBlockParam](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_output_block_param) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

BetaBashCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaBashCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error\_code, type } or[BetaBashCodeExecutionResultBlock](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return\_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError = object {error\_code, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

BetaBashCodeExecutionResultBlock = object {content, return\_code, stderr, 2 more}

content: array of [BetaBashCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_output_block) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

BetaBashCodeExecutionToolResultBlockParam = object {content, tool\_use\_id, type, cache\_control}

content: [BetaBashCodeExecutionToolResultErrorParam](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_tool_result_error_param) { error\_code, type } or[BetaBashCodeExecutionResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_result_block_param) { content, return\_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultErrorParam = object {error\_code, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

BetaBashCodeExecutionResultBlockParam = object {content, return\_code, stderr, 2 more}

content: array of [BetaBashCodeExecutionOutputBlockParam](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_output_block_param) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaBashCodeExecutionToolResultError = object {error\_code, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

BetaBashCodeExecutionToolResultErrorParam = object {error\_code, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

BetaCacheControlEphemeral = object {type, ttl}

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaCacheCreation = object {ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens}

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

BetaCitationCharLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationCharLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationConfig = object {enabled}

enabled: boolean

BetaCitationContentBlockLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

BetaCitationContentBlockLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

BetaCitationPageLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationPageLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationSearchResultLocation = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

BetaCitationSearchResultLocationParam = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

BetaCitationWebSearchResultLocationParam = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationsConfigParam = object {enabled}

enabled: optional boolean

BetaCitationsDelta = object {citation, type}

citation: [BetaCitationCharLocation](https://platform.claude.com/docs/en/api/beta#beta_citation_char_location) { cited\_text, document\_index, document\_title, 4 more } or[BetaCitationPageLocation](https://platform.claude.com/docs/en/api/beta#beta_citation_page_location) { cited\_text, document\_index, document\_title, 4 more } or[BetaCitationContentBlockLocation](https://platform.claude.com/docs/en/api/beta#beta_citation_content_block_location) { cited\_text, document\_index, document\_title, 4 more } or2 more

Accepts one of the following:

BetaCitationCharLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

type: "citations\_delta"

BetaCitationsWebSearchResultLocation = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaClearThinking20251015Edit = object {type, keep}

type: "clear\_thinking\_20251015"

keep: optional [BetaThinkingTurns](https://platform.claude.com/docs/en/api/beta#beta_thinking_turns) { type, value } or[BetaAllThinkingTurns](https://platform.claude.com/docs/en/api/beta#beta_all_thinking_turns) { type } or"all"

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

Accepts one of the following:

BetaThinkingTurns = object {type, value}

type: "thinking\_turns"

value: number

BetaAllThinkingTurns = object {type}

type: "all"

UnionMember2 = "all"

BetaClearThinking20251015EditResponse = object {cleared\_input\_tokens, cleared\_thinking\_turns, type}

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.

BetaClearToolUses20250919Edit = object {type, clear\_at\_least, clear\_tool\_inputs, 3 more}

type: "clear\_tool\_uses\_20250919"

clear\_at\_least: optional [BetaInputTokensClearAtLeast](https://platform.claude.com/docs/en/api/beta#beta_input_tokens_clear_at_least) { type, value }

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: "input\_tokens"

value: number

clear\_tool\_inputs: optional booleanorarray of string

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

Accepts one of the following:

UnionMember0 = boolean

UnionMember1 = array of string

exclude\_tools: optional array of string

Tool names whose uses are preserved from clearing

keep: optional [BetaToolUsesKeep](https://platform.claude.com/docs/en/api/beta#beta_tool_uses_keep) { type, value }

Number of tool uses to retain in the conversation

type: "tool\_uses"

value: number

trigger: optional [BetaInputTokensTrigger](https://platform.claude.com/docs/en/api/beta#beta_input_tokens_trigger) { type, value } or[BetaToolUsesTrigger](https://platform.claude.com/docs/en/api/beta#beta_tool_uses_trigger) { type, value }

Condition that triggers the context management strategy

Accepts one of the following:

BetaInputTokensTrigger = object {type, value}

type: "input\_tokens"

value: number

BetaToolUsesTrigger = object {type, value}

type: "tool\_uses"

value: number

BetaClearToolUses20250919EditResponse = object {cleared\_input\_tokens, cleared\_tool\_uses, type}

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

BetaCodeExecutionOutputBlock = object {file\_id, type}

file\_id: string

type: "code\_execution\_output"

BetaCodeExecutionOutputBlockParam = object {file\_id, type}

file\_id: string

type: "code\_execution\_output"

BetaCodeExecutionResultBlock = object {content, return\_code, stderr, 2 more}

content: array of [BetaCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

BetaCodeExecutionResultBlockParam = object {content, return\_code, stderr, 2 more}

content: array of [BetaCodeExecutionOutputBlockParam](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block_param) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

BetaCodeExecutionTool20250522 = object {name, type, allowed\_callers, 3 more}

name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20250522"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaCodeExecutionTool20250825 = object {name, type, allowed\_callers, 3 more}

name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20250825"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaCodeExecutionTool20260120 = object {name, type, allowed\_callers, 3 more}

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20260120"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaCodeExecutionToolResultBlockContent](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

BetaCodeExecutionToolResultError = object {error\_code, type}

error\_code: [BetaCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

BetaCodeExecutionResultBlock = object {content, return\_code, stderr, 2 more}

content: array of [BetaCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

BetaEncryptedCodeExecutionResultBlock = object {content, encrypted\_stdout, return\_code, 2 more}

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

BetaCodeExecutionToolResultBlockContent = [BetaCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_error) { error\_code, type } or[BetaCodeExecutionResultBlock](https://platform.claude.com/docs/en/api/beta#beta_code_execution_result_block) { content, return\_code, stderr, 2 more } or[BetaEncryptedCodeExecutionResultBlock](https://platform.claude.com/docs/en/api/beta#beta_encrypted_code_execution_result_block) { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

BetaCodeExecutionToolResultError = object {error\_code, type}

error\_code: [BetaCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

BetaCodeExecutionResultBlock = object {content, return\_code, stderr, 2 more}

content: array of [BetaCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

BetaEncryptedCodeExecutionResultBlock = object {content, encrypted\_stdout, return\_code, 2 more}

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

BetaCodeExecutionToolResultBlockParam = object {content, tool\_use\_id, type, cache\_control}

content: [BetaCodeExecutionToolResultBlockParamContent](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_block_param_content)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

BetaCodeExecutionToolResultErrorParam = object {error\_code, type}

error\_code: [BetaCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

BetaCodeExecutionResultBlockParam = object {content, return\_code, stderr, 2 more}

content: array of [BetaCodeExecutionOutputBlockParam](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block_param) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

BetaEncryptedCodeExecutionResultBlockParam = object {content, encrypted\_stdout, return\_code, 2 more}

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlockParam](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block_param) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaCodeExecutionToolResultBlockParamContent = [BetaCodeExecutionToolResultErrorParam](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_error_param) { error\_code, type } or[BetaCodeExecutionResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_code_execution_result_block_param) { content, return\_code, stderr, 2 more } or[BetaEncryptedCodeExecutionResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_encrypted_code_execution_result_block_param) { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

BetaCodeExecutionToolResultErrorParam = object {error\_code, type}

error\_code: [BetaCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

BetaCodeExecutionResultBlockParam = object {content, return\_code, stderr, 2 more}

content: array of [BetaCodeExecutionOutputBlockParam](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block_param) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

BetaEncryptedCodeExecutionResultBlockParam = object {content, encrypted\_stdout, return\_code, 2 more}

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlockParam](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block_param) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

BetaCodeExecutionToolResultError = object {error\_code, type}

error\_code: [BetaCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

BetaCodeExecutionToolResultErrorCode = "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or"execution\_time\_exceeded"

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

BetaCodeExecutionToolResultErrorParam = object {error\_code, type}

error\_code: [BetaCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

BetaCompact20260112Edit = object {type, instructions, pause\_after\_compaction, trigger}

Automatically compact older context when reaching the configured trigger threshold.

type: "compact\_20260112"

instructions: optional string

Additional instructions for summarization.

pause\_after\_compaction: optional boolean

Whether to pause after compaction and return the compaction block to the user.

trigger: optional [BetaInputTokensTrigger](https://platform.claude.com/docs/en/api/beta#beta_input_tokens_trigger) { type, value }

When to trigger compaction. Defaults to 150000 input tokens.

type: "input\_tokens"

value: number

BetaCompactionBlock = object {content, type}

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

BetaCompactionBlockParam = object {content, type, cache\_control}

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

content: string

Summary of previously compacted content, or null if compaction failed

type: "compaction"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaCompactionContentBlockDelta = object {content, type}

content: string

type: "compaction\_delta"

BetaCompactionIterationUsage = object {cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more}

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

BetaContainer = object {id, expires\_at, skills}

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

skills: array of [BetaSkill](https://platform.claude.com/docs/en/api/beta#beta_skill) { skill\_id, type, version }

Skills loaded in the container

skill\_id: string

Skill ID

type: "anthropic"or"custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

BetaContainerParams = object {id, skills}

Container parameters with skills to be loaded.

id: optional string

Container id

skills: optional array of [BetaSkillParams](https://platform.claude.com/docs/en/api/beta#beta_skill_params) { skill\_id, type, version }

List of skills to load in the container

skill\_id: string

Skill ID

type: "anthropic"or"custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: optional string

Skill version or 'latest' for most recent version

BetaContainerUploadBlock = object {file\_id, type}

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

BetaContainerUploadBlockParam = object {file\_id, type, cache\_control}

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: string

type: "container\_upload"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaContentBlock = [BetaTextBlock](https://platform.claude.com/docs/en/api/beta#beta_text_block) { citations, text, type } or[BetaThinkingBlock](https://platform.claude.com/docs/en/api/beta#beta_thinking_block) { signature, thinking, type } or[BetaRedactedThinkingBlock](https://platform.claude.com/docs/en/api/beta#beta_redacted_thinking_block) { data, type } or12 more

Response model for a file uploaded to the container.

Accepts one of the following:

BetaTextBlock = object {citations, text, type}

citations: array of [BetaTextCitation](https://platform.claude.com/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

BetaThinkingBlock = object {signature, thinking, type}

signature: string

thinking: string

type: "thinking"

BetaRedactedThinkingBlock = object {data, type}

data: string

type: "redacted\_thinking"

BetaToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: string

type: "tool\_use"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaServerToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: "web\_search"or"web\_fetch"or"code\_execution"or4 more

Accepts one of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaWebSearchToolResultBlock = object {content, tool\_use\_id, type, caller}

content: [BetaWebSearchToolResultBlockContent](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError = object {error\_code, type}

error\_code: [BetaWebSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

UnionMember1 = array of [BetaWebSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_web_search_result_block) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaWebFetchToolResultBlock = object {content, tool\_use\_id, type, caller}

content: [BetaWebFetchToolResultErrorBlock](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error\_code, type } or[BetaWebFetchBlock](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_block) { content, retrieved\_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock = object {error\_code, type}

error\_code: [BetaWebFetchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

BetaWebFetchBlock = object {content, retrieved\_at, type, url}

content: [BetaDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](https://platform.claude.com/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](https://platform.claude.com/docs/en/api/beta#beta_base64_pdf_source) { data, media\_type, type } or[BetaPlainTextSource](https://platform.claude.com/docs/en/api/beta#beta_plain_text_source) { data, media\_type, type }

Accepts one of the following:

BetaBase64PDFSource = object {data, media\_type, type}

data: string

media\_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object {data, media\_type, type}

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaCodeExecutionToolResultBlockContent](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

BetaCodeExecutionToolResultError = object {error\_code, type}

error\_code: [BetaCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

BetaCodeExecutionResultBlock = object {content, return\_code, stderr, 2 more}

content: array of [BetaCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

BetaEncryptedCodeExecutionResultBlock = object {content, encrypted\_stdout, return\_code, 2 more}

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

BetaBashCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaBashCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error\_code, type } or[BetaBashCodeExecutionResultBlock](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return\_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError = object {error\_code, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

BetaBashCodeExecutionResultBlock = object {content, return\_code, stderr, 2 more}

content: array of [BetaBashCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_output_block) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

BetaTextEditorCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaTextEditorCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error\_code, error\_message, type } or[BetaTextEditorCodeExecutionViewResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file\_type, num\_lines, 3 more } or[BetaTextEditorCodeExecutionCreateResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is\_file\_update, type } or[BetaTextEditorCodeExecutionStrReplaceResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new\_lines, new\_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError = object {error\_code, error\_message, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

BetaTextEditorCodeExecutionViewResultBlock = object {content, file\_type, num\_lines, 3 more}

content: string

file\_type: "text"or"image"or"pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

BetaTextEditorCodeExecutionCreateResultBlock = object {is\_file\_update, type}

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock = object {lines, new\_lines, new\_start, 3 more}

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

BetaToolSearchToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaToolSearchToolResultError](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_result_error) { error\_code, error\_message, type } or[BetaToolSearchToolSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool\_references, type }

Accepts one of the following:

BetaToolSearchToolResultError = object {error\_code, error\_message, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or"execution\_time\_exceeded"

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

BetaToolSearchToolSearchResultBlock = object {tool\_references, type}

tool\_references: array of [BetaToolReferenceBlock](https://platform.claude.com/docs/en/api/beta#beta_tool_reference_block) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

BetaMCPToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

BetaMCPToolResultBlock = object {content, is\_error, tool\_use\_id, type}

content: stringorarray of [BetaTextBlock](https://platform.claude.com/docs/en/api/beta#beta_text_block) { citations, text, type }

Accepts one of the following:

UnionMember0 = string

BetaMCPToolResultBlockContent = array of [BetaTextBlock](https://platform.claude.com/docs/en/api/beta#beta_text_block) { citations, text, type }

citations: array of [BetaTextCitation](https://platform.claude.com/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"

BetaContainerUploadBlock = object {file\_id, type}

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

BetaCompactionBlock = object {content, type}

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

BetaContentBlockParam = [BetaTextBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_block_param) { text, type, cache\_control, citations } or[BetaImageBlockParam](https://platform.claude.com/docs/en/api/beta#beta_image_block_param) { source, type, cache\_control } or[BetaRequestDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_request_document_block) { source, type, cache\_control, 3 more } or16 more

Regular text content.

Accepts one of the following:

BetaTextBlockParam = object {text, type, cache\_control, citations}

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

BetaImageBlockParam = object {source, type, cache\_control}

source: [BetaBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_base64_image_source) { data, media\_type, type } or[BetaURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_url_image_source) { type, url } or[BetaFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_file_image_source) { file\_id, type }

Accepts one of the following:

BetaBase64ImageSource = object {data, media\_type, type}

data: string

media\_type: "image/jpeg"or"image/png"or"image/gif"or"image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object {type, url}

type: "url"

url: string

BetaFileImageSource = object {file\_id, type}

file\_id: string

type: "file"

type: "image"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaRequestDocumentBlock = object {source, type, cache\_control, 3 more}

source: [BetaBase64PDFSource](https://platform.claude.com/docs/en/api/beta#beta_base64_pdf_source) { data, media\_type, type } or[BetaPlainTextSource](https://platform.claude.com/docs/en/api/beta#beta_plain_text_source) { data, media\_type, type } or[BetaContentBlockSource](https://platform.claude.com/docs/en/api/beta#beta_content_block_source) { content, type } or2 more

Accepts one of the following:

BetaBase64PDFSource = object {data, media\_type, type}

data: string

media\_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object {data, media\_type, type}

data: string

media\_type: "text/plain"

type: "text"

BetaContentBlockSource = object {content, type}

content: stringorarray of [BetaContentBlockSourceContent](https://platform.claude.com/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

UnionMember0 = string

BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](https://platform.claude.com/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

BetaTextBlockParam = object {text, type, cache\_control, citations}

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

BetaImageBlockParam = object {source, type, cache\_control}

source: [BetaBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_base64_image_source) { data, media\_type, type } or[BetaURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_url_image_source) { type, url } or[BetaFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_file_image_source) { file\_id, type }

Accepts one of the following:

BetaBase64ImageSource = object {data, media\_type, type}

data: string

media\_type: "image/jpeg"or"image/png"or"image/gif"or"image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object {type, url}

type: "url"

url: string

BetaFileImageSource = object {file\_id, type}

file\_id: string

type: "file"

type: "image"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

BetaURLPDFSource = object {type, url}

type: "url"

url: string

BetaFileDocumentSource = object {file\_id, type}

file\_id: string

type: "file"

type: "document"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](https://platform.claude.com/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

context: optional string

title: optional string

BetaSearchResultBlockParam = object {content, source, title, 3 more}

content: array of [BetaTextBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_block_param) { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

source: string

title: string

type: "search\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](https://platform.claude.com/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

BetaThinkingBlockParam = object {signature, thinking, type}

signature: string

thinking: string

type: "thinking"

BetaRedactedThinkingBlockParam = object {data, type}

data: string

type: "redacted\_thinking"

BetaToolUseBlockParam = object {id, input, name, 3 more}

id: string

input: map\[unknown\]

name: string

type: "tool\_use"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaToolResultBlockParam = object {tool\_use\_id, type, cache\_control, 2 more}

tool\_use\_id: string

type: "tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content: optional stringorarray of [BetaTextBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_block_param) { text, type, cache\_control, citations } or[BetaImageBlockParam](https://platform.claude.com/docs/en/api/beta#beta_image_block_param) { source, type, cache\_control } or[BetaSearchResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_search_result_block_param) { content, source, title, 3 more } or2 more

Accepts one of the following:

UnionMember0 = string

UnionMember1 = array of [BetaTextBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_block_param) { text, type, cache\_control, citations } or[BetaImageBlockParam](https://platform.claude.com/docs/en/api/beta#beta_image_block_param) { source, type, cache\_control } or[BetaSearchResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_search_result_block_param) { content, source, title, 3 more } or2 more

Accepts one of the following:

BetaTextBlockParam = object {text, type, cache\_control, citations}

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

BetaImageBlockParam = object {source, type, cache\_control}

source: [BetaBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_base64_image_source) { data, media\_type, type } or[BetaURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_url_image_source) { type, url } or[BetaFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_file_image_source) { file\_id, type }

Accepts one of the following:

BetaBase64ImageSource = object {data, media\_type, type}

data: string

media\_type: "image/jpeg"or"image/png"or"image/gif"or"image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object {type, url}

type: "url"

url: string

BetaFileImageSource = object {file\_id, type}

file\_id: string

type: "file"

type: "image"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaSearchResultBlockParam = object {content, source, title, 3 more}

content: array of [BetaTextBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_block_param) { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

source: string

title: string

type: "search\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](https://platform.claude.com/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

BetaRequestDocumentBlock = object {source, type, cache\_control, 3 more}

source: [BetaBase64PDFSource](https://platform.claude.com/docs/en/api/beta#beta_base64_pdf_source) { data, media\_type, type } or[BetaPlainTextSource](https://platform.claude.com/docs/en/api/beta#beta_plain_text_source) { data, media\_type, type } or[BetaContentBlockSource](https://platform.claude.com/docs/en/api/beta#beta_content_block_source) { content, type } or2 more

Accepts one of the following:

BetaBase64PDFSource = object {data, media\_type, type}

data: string

media\_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object {data, media\_type, type}

data: string

media\_type: "text/plain"

type: "text"

BetaContentBlockSource = object {content, type}

content: stringorarray of [BetaContentBlockSourceContent](https://platform.claude.com/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

UnionMember0 = string

BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](https://platform.claude.com/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

BetaTextBlockParam = object {text, type, cache\_control, citations}

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

BetaImageBlockParam = object {source, type, cache\_control}

source: [BetaBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_base64_image_source) { data, media\_type, type } or[BetaURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_url_image_source) { type, url } or[BetaFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_file_image_source) { file\_id, type }

Accepts one of the following:

BetaBase64ImageSource = object {data, media\_type, type}

data: string

media\_type: "image/jpeg"or"image/png"or"image/gif"or"image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object {type, url}

type: "url"

url: string

BetaFileImageSource = object {file\_id, type}

file\_id: string

type: "file"

type: "image"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

BetaURLPDFSource = object {type, url}

type: "url"

url: string

BetaFileDocumentSource = object {file\_id, type}

file\_id: string

type: "file"

type: "document"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](https://platform.claude.com/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

context: optional string

title: optional string

BetaToolReferenceBlockParam = object {tool\_name, type, cache\_control}

Tool reference block that can be included in tool\_result content.

tool\_name: string

type: "tool\_reference"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

is\_error: optional boolean

BetaServerToolUseBlockParam = object {id, input, name, 3 more}

id: string

input: map\[unknown\]

name: "web\_search"or"web\_fetch"or"code\_execution"or4 more

Accepts one of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaWebSearchToolResultBlockParam = object {content, tool\_use\_id, type, 2 more}

content: [BetaWebSearchToolResultBlockParamContent](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_block_param_content)

Accepts one of the following:

ResultBlock = array of [BetaWebSearchResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_web_search_result_block_param) { encrypted\_content, title, type, 2 more }

encrypted\_content: string

title: string

type: "web\_search\_result"

url: string

page\_age: optional string

BetaWebSearchToolRequestError = object {error\_code, type}

error\_code: [BetaWebSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

tool\_use\_id: string

type: "web\_search\_tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaWebFetchToolResultBlockParam = object {content, tool\_use\_id, type, 2 more}

content: [BetaWebFetchToolResultErrorBlockParam](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_block_param) { error\_code, type } or[BetaWebFetchBlockParam](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_block_param) { content, type, url, retrieved\_at }

Accepts one of the following:

BetaWebFetchToolResultErrorBlockParam = object {error\_code, type}

error\_code: [BetaWebFetchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

BetaWebFetchBlockParam = object {content, type, url, retrieved\_at}

content: [BetaRequestDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_request_document_block) { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](https://platform.claude.com/docs/en/api/beta#beta_base64_pdf_source) { data, media\_type, type } or[BetaPlainTextSource](https://platform.claude.com/docs/en/api/beta#beta_plain_text_source) { data, media\_type, type } or[BetaContentBlockSource](https://platform.claude.com/docs/en/api/beta#beta_content_block_source) { content, type } or2 more

Accepts one of the following:

BetaBase64PDFSource = object {data, media\_type, type}

data: string

media\_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object {data, media\_type, type}

data: string

media\_type: "text/plain"

type: "text"

BetaContentBlockSource = object {content, type}

content: stringorarray of [BetaContentBlockSourceContent](https://platform.claude.com/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

UnionMember0 = string

BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](https://platform.claude.com/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

BetaTextBlockParam = object {text, type, cache\_control, citations}

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

BetaImageBlockParam = object {source, type, cache\_control}

source: [BetaBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_base64_image_source) { data, media\_type, type } or[BetaURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_url_image_source) { type, url } or[BetaFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_file_image_source) { file\_id, type }

Accepts one of the following:

BetaBase64ImageSource = object {data, media\_type, type}

data: string

media\_type: "image/jpeg"or"image/png"or"image/gif"or"image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object {type, url}

type: "url"

url: string

BetaFileImageSource = object {file\_id, type}

file\_id: string

type: "file"

type: "image"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

BetaURLPDFSource = object {type, url}

type: "url"

url: string

BetaFileDocumentSource = object {file\_id, type}

file\_id: string

type: "file"

type: "document"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](https://platform.claude.com/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

context: optional string

title: optional string

type: "web\_fetch\_result"

url: string

Fetched content URL

retrieved\_at: optional string

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaCodeExecutionToolResultBlockParam = object {content, tool\_use\_id, type, cache\_control}

content: [BetaCodeExecutionToolResultBlockParamContent](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_block_param_content)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

BetaCodeExecutionToolResultErrorParam = object {error\_code, type}

error\_code: [BetaCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

BetaCodeExecutionResultBlockParam = object {content, return\_code, stderr, 2 more}

content: array of [BetaCodeExecutionOutputBlockParam](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block_param) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

BetaEncryptedCodeExecutionResultBlockParam = object {content, encrypted\_stdout, return\_code, 2 more}

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlockParam](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block_param) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaBashCodeExecutionToolResultBlockParam = object {content, tool\_use\_id, type, cache\_control}

content: [BetaBashCodeExecutionToolResultErrorParam](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_tool_result_error_param) { error\_code, type } or[BetaBashCodeExecutionResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_result_block_param) { content, return\_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultErrorParam = object {error\_code, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

BetaBashCodeExecutionResultBlockParam = object {content, return\_code, stderr, 2 more}

content: array of [BetaBashCodeExecutionOutputBlockParam](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_output_block_param) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaTextEditorCodeExecutionToolResultBlockParam = object {content, tool\_use\_id, type, cache\_control}

content: [BetaTextEditorCodeExecutionToolResultErrorParam](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error_param) { error\_code, type, error\_message } or[BetaTextEditorCodeExecutionViewResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_view_result_block_param) { content, file\_type, type, 3 more } or[BetaTextEditorCodeExecutionCreateResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_create_result_block_param) { is\_file\_update, type } or[BetaTextEditorCodeExecutionStrReplaceResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block_param) { type, lines, new\_lines, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultErrorParam = object {error\_code, type, error\_message}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

type: "text\_editor\_code\_execution\_tool\_result\_error"

error\_message: optional string

BetaTextEditorCodeExecutionViewResultBlockParam = object {content, file\_type, type, 3 more}

content: string

file\_type: "text"or"image"or"pdf"

Accepts one of the following:

"text"

"image"

"pdf"

type: "text\_editor\_code\_execution\_view\_result"

num\_lines: optional number

start\_line: optional number

total\_lines: optional number

BetaTextEditorCodeExecutionCreateResultBlockParam = object {is\_file\_update, type}

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

BetaTextEditorCodeExecutionStrReplaceResultBlockParam = object {type, lines, new\_lines, 3 more}

type: "text\_editor\_code\_execution\_str\_replace\_result"

lines: optional array of string

new\_lines: optional number

new\_start: optional number

old\_lines: optional number

old\_start: optional number

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaToolSearchToolResultBlockParam = object {content, tool\_use\_id, type, cache\_control}

content: [BetaToolSearchToolResultErrorParam](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_result_error_param) { error\_code, type } or[BetaToolSearchToolSearchResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_search_result_block_param) { tool\_references, type }

Accepts one of the following:

BetaToolSearchToolResultErrorParam = object {error\_code, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or"execution\_time\_exceeded"

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "tool\_search\_tool\_result\_error"

BetaToolSearchToolSearchResultBlockParam = object {tool\_references, type}

tool\_references: array of [BetaToolReferenceBlockParam](https://platform.claude.com/docs/en/api/beta#beta_tool_reference_block_param) { tool\_name, type, cache\_control }

tool\_name: string

type: "tool\_reference"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaMCPToolUseBlockParam = object {id, input, name, 3 more}

id: string

input: map\[unknown\]

name: string

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaRequestMCPToolResultBlockParam = object {tool\_use\_id, type, cache\_control, 2 more}

tool\_use\_id: string

type: "mcp\_tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content: optional stringorarray of [BetaTextBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_block_param) { text, type, cache\_control, citations }

Accepts one of the following:

UnionMember0 = string

BetaMCPToolResultBlockParamContent = array of [BetaTextBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_block_param) { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

is\_error: optional boolean

BetaContainerUploadBlockParam = object {file\_id, type, cache\_control}

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: string

type: "container\_upload"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaCompactionBlockParam = object {content, type, cache\_control}

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

content: string

Summary of previously compacted content, or null if compaction failed

type: "compaction"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaContentBlockSource = object {content, type}

content: stringorarray of [BetaContentBlockSourceContent](https://platform.claude.com/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

UnionMember0 = string

BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](https://platform.claude.com/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

BetaTextBlockParam = object {text, type, cache\_control, citations}

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

BetaImageBlockParam = object {source, type, cache\_control}

source: [BetaBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_base64_image_source) { data, media\_type, type } or[BetaURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_url_image_source) { type, url } or[BetaFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_file_image_source) { file\_id, type }

Accepts one of the following:

BetaBase64ImageSource = object {data, media\_type, type}

data: string

media\_type: "image/jpeg"or"image/png"or"image/gif"or"image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object {type, url}

type: "url"

url: string

BetaFileImageSource = object {file\_id, type}

file\_id: string

type: "file"

type: "image"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

BetaContentBlockSourceContent = [BetaTextBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_block_param) { text, type, cache\_control, citations } or[BetaImageBlockParam](https://platform.claude.com/docs/en/api/beta#beta_image_block_param) { source, type, cache\_control }

Accepts one of the following:

BetaTextBlockParam = object {text, type, cache\_control, citations}

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

BetaImageBlockParam = object {source, type, cache\_control}

source: [BetaBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_base64_image_source) { data, media\_type, type } or[BetaURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_url_image_source) { type, url } or[BetaFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_file_image_source) { file\_id, type }

Accepts one of the following:

BetaBase64ImageSource = object {data, media\_type, type}

data: string

media\_type: "image/jpeg"or"image/png"or"image/gif"or"image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object {type, url}

type: "url"

url: string

BetaFileImageSource = object {file\_id, type}

file\_id: string

type: "file"

type: "image"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaContextManagementConfig = object {edits}

edits: optional array of [BetaClearToolUses20250919Edit](https://platform.claude.com/docs/en/api/beta#beta_clear_tool_uses_20250919_edit) { type, clear\_at\_least, clear\_tool\_inputs, 3 more } or[BetaClearThinking20251015Edit](https://platform.claude.com/docs/en/api/beta#beta_clear_thinking_20251015_edit) { type, keep } or[BetaCompact20260112Edit](https://platform.claude.com/docs/en/api/beta#beta_compact_20260112_edit) { type, instructions, pause\_after\_compaction, trigger }

List of context management edits to apply

Accepts one of the following:

BetaClearToolUses20250919Edit = object {type, clear\_at\_least, clear\_tool\_inputs, 3 more}

type: "clear\_tool\_uses\_20250919"

clear\_at\_least: optional [BetaInputTokensClearAtLeast](https://platform.claude.com/docs/en/api/beta#beta_input_tokens_clear_at_least) { type, value }

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: "input\_tokens"

value: number

clear\_tool\_inputs: optional booleanorarray of string

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

Accepts one of the following:

UnionMember0 = boolean

UnionMember1 = array of string

exclude\_tools: optional array of string

Tool names whose uses are preserved from clearing

keep: optional [BetaToolUsesKeep](https://platform.claude.com/docs/en/api/beta#beta_tool_uses_keep) { type, value }

Number of tool uses to retain in the conversation

type: "tool\_uses"

value: number

trigger: optional [BetaInputTokensTrigger](https://platform.claude.com/docs/en/api/beta#beta_input_tokens_trigger) { type, value } or[BetaToolUsesTrigger](https://platform.claude.com/docs/en/api/beta#beta_tool_uses_trigger) { type, value }

Condition that triggers the context management strategy

Accepts one of the following:

BetaInputTokensTrigger = object {type, value}

type: "input\_tokens"

value: number

BetaToolUsesTrigger = object {type, value}

type: "tool\_uses"

value: number

BetaClearThinking20251015Edit = object {type, keep}

type: "clear\_thinking\_20251015"

keep: optional [BetaThinkingTurns](https://platform.claude.com/docs/en/api/beta#beta_thinking_turns) { type, value } or[BetaAllThinkingTurns](https://platform.claude.com/docs/en/api/beta#beta_all_thinking_turns) { type } or"all"

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

Accepts one of the following:

BetaThinkingTurns = object {type, value}

type: "thinking\_turns"

value: number

BetaAllThinkingTurns = object {type}

type: "all"

UnionMember2 = "all"

BetaCompact20260112Edit = object {type, instructions, pause\_after\_compaction, trigger}

Automatically compact older context when reaching the configured trigger threshold.

type: "compact\_20260112"

instructions: optional string

Additional instructions for summarization.

pause\_after\_compaction: optional boolean

Whether to pause after compaction and return the compaction block to the user.

trigger: optional [BetaInputTokensTrigger](https://platform.claude.com/docs/en/api/beta#beta_input_tokens_trigger) { type, value }

When to trigger compaction. Defaults to 150000 input tokens.

type: "input\_tokens"

value: number

BetaContextManagementResponse = object {applied\_edits}

applied\_edits: array of [BetaClearToolUses20250919EditResponse](https://platform.claude.com/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared\_input\_tokens, cleared\_tool\_uses, type } or[BetaClearThinking20251015EditResponse](https://platform.claude.com/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared\_input\_tokens, cleared\_thinking\_turns, type }

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse = object {cleared\_input\_tokens, cleared\_tool\_uses, type}

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

BetaClearThinking20251015EditResponse = object {cleared\_input\_tokens, cleared\_thinking\_turns, type}

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.

BetaCountTokensContextManagementResponse = object {original\_input\_tokens}

original\_input\_tokens: number

The original token count before context management was applied

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaDocumentBlock = object {citations, source, title, type}

citations: [BetaCitationConfig](https://platform.claude.com/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](https://platform.claude.com/docs/en/api/beta#beta_base64_pdf_source) { data, media\_type, type } or[BetaPlainTextSource](https://platform.claude.com/docs/en/api/beta#beta_plain_text_source) { data, media\_type, type }

Accepts one of the following:

BetaBase64PDFSource = object {data, media\_type, type}

data: string

media\_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object {data, media\_type, type}

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

BetaEncryptedCodeExecutionResultBlock = object {content, encrypted\_stdout, return\_code, 2 more}

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

BetaEncryptedCodeExecutionResultBlockParam = object {content, encrypted\_stdout, return\_code, 2 more}

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlockParam](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block_param) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

BetaFileDocumentSource = object {file\_id, type}

file\_id: string

type: "file"

BetaFileImageSource = object {file\_id, type}

file\_id: string

type: "file"

BetaImageBlockParam = object {source, type, cache\_control}

source: [BetaBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_base64_image_source) { data, media\_type, type } or[BetaURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_url_image_source) { type, url } or[BetaFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_file_image_source) { file\_id, type }

Accepts one of the following:

BetaBase64ImageSource = object {data, media\_type, type}

data: string

media\_type: "image/jpeg"or"image/png"or"image/gif"or"image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object {type, url}

type: "url"

url: string

BetaFileImageSource = object {file\_id, type}

file\_id: string

type: "file"

type: "image"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaInputJSONDelta = object {partial\_json, type}

partial\_json: string

type: "input\_json\_delta"

BetaInputTokensClearAtLeast = object {type, value}

type: "input\_tokens"

value: number

BetaInputTokensTrigger = object {type, value}

type: "input\_tokens"

value: number

BetaIterationsUsage = array of [BetaMessageIterationUsage](https://platform.claude.com/docs/en/api/beta#beta_message_iteration_usage) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } or[BetaCompactionIterationUsage](https://platform.claude.com/docs/en/api/beta#beta_compaction_iteration_usage) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage = object {cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more}

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

BetaCompactionIterationUsage = object {cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more}

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

BetaJSONOutputFormat = object {schema, type}

schema: map\[unknown\]

The JSON schema of the format

type: "json\_schema"

BetaMCPToolConfig = object {defer\_loading, enabled}

Configuration for a specific tool in an MCP toolset.

defer\_loading: optional boolean

enabled: optional boolean

BetaMCPToolDefaultConfig = object {defer\_loading, enabled}

Default configuration for tools in an MCP toolset.

defer\_loading: optional boolean

enabled: optional boolean

BetaMCPToolResultBlock = object {content, is\_error, tool\_use\_id, type}

content: stringorarray of [BetaTextBlock](https://platform.claude.com/docs/en/api/beta#beta_text_block) { citations, text, type }

Accepts one of the following:

UnionMember0 = string

BetaMCPToolResultBlockContent = array of [BetaTextBlock](https://platform.claude.com/docs/en/api/beta#beta_text_block) { citations, text, type }

citations: array of [BetaTextCitation](https://platform.claude.com/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"

BetaMCPToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

BetaMCPToolUseBlockParam = object {id, input, name, 3 more}

id: string

input: map\[unknown\]

name: string

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaMCPToolset = object {mcp\_server\_name, type, cache\_control, 2 more}

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

mcp\_server\_name: string

Name of the MCP server to configure tools for

type: "mcp\_toolset"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

configs: optional map\[[BetaMCPToolConfig](https://platform.claude.com/docs/en/api/beta#beta_mcp_tool_config) { defer\_loading, enabled } \]

Configuration overrides for specific tools, keyed by tool name

defer\_loading: optional boolean

enabled: optional boolean

default\_config: optional [BetaMCPToolDefaultConfig](https://platform.claude.com/docs/en/api/beta#beta_mcp_tool_default_config) { defer\_loading, enabled }

Default configuration applied to all tools from this server

defer\_loading: optional boolean

enabled: optional boolean

BetaMemoryTool20250818 = object {name, type, allowed\_callers, 4 more}

name: "memory"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "memory\_20250818"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaMemoryTool20250818Command = [BetaMemoryTool20250818ViewCommand](https://platform.claude.com/docs/en/api/beta#beta_memory_tool_20250818_view_command) { command, path, view\_range } or[BetaMemoryTool20250818CreateCommand](https://platform.claude.com/docs/en/api/beta#beta_memory_tool_20250818_create_command) { command, file\_text, path } or[BetaMemoryTool20250818StrReplaceCommand](https://platform.claude.com/docs/en/api/beta#beta_memory_tool_20250818_str_replace_command) { command, new\_str, old\_str, path } or3 more

Accepts one of the following:

BetaMemoryTool20250818ViewCommand = object {command, path, view\_range}

command: "view"

Command type identifier

path: string

Path to directory or file to view

view\_range: optional array of number

Optional line range for viewing specific lines

BetaMemoryTool20250818CreateCommand = object {command, file\_text, path}

command: "create"

Command type identifier

file\_text: string

Content to write to the file

path: string

Path where the file should be created

BetaMemoryTool20250818StrReplaceCommand = object {command, new\_str, old\_str, path}

command: "str\_replace"

Command type identifier

new\_str: string

Text to replace with

old\_str: string

Text to search for and replace

path: string

Path to the file where text should be replaced

BetaMemoryTool20250818InsertCommand = object {command, insert\_line, insert\_text, path}

command: "insert"

Command type identifier

insert\_line: number

Line number where text should be inserted

insert\_text: string

Text to insert at the specified line

path: string

Path to the file where text should be inserted

BetaMemoryTool20250818DeleteCommand = object {command, path}

command: "delete"

Command type identifier

path: string

Path to the file or directory to delete

BetaMemoryTool20250818RenameCommand = object {command, new\_path, old\_path}

command: "rename"

Command type identifier

new\_path: string

New path for the file or directory

old\_path: string

Current path of the file or directory

BetaMemoryTool20250818CreateCommand = object {command, file\_text, path}

command: "create"

Command type identifier

file\_text: string

Content to write to the file

path: string

Path where the file should be created

BetaMemoryTool20250818DeleteCommand = object {command, path}

command: "delete"

Command type identifier

path: string

Path to the file or directory to delete

BetaMemoryTool20250818InsertCommand = object {command, insert\_line, insert\_text, path}

command: "insert"

Command type identifier

insert\_line: number

Line number where text should be inserted

insert\_text: string

Text to insert at the specified line

path: string

Path to the file where text should be inserted

BetaMemoryTool20250818RenameCommand = object {command, new\_path, old\_path}

command: "rename"

Command type identifier

new\_path: string

New path for the file or directory

old\_path: string

Current path of the file or directory

BetaMemoryTool20250818StrReplaceCommand = object {command, new\_str, old\_str, path}

command: "str\_replace"

Command type identifier

new\_str: string

Text to replace with

old\_str: string

Text to search for and replace

path: string

Path to the file where text should be replaced

BetaMemoryTool20250818ViewCommand = object {command, path, view\_range}

command: "view"

Command type identifier

path: string

Path to directory or file to view

view\_range: optional array of number

Optional line range for viewing specific lines

BetaMessage = object {id, container, content, 7 more}

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](https://platform.claude.com/docs/en/api/beta#beta_container) { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

skills: array of [BetaSkill](https://platform.claude.com/docs/en/api/beta#beta_skill) { skill\_id, type, version }

Skills loaded in the container

skill\_id: string

Skill ID

type: "anthropic"or"custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

content: array of [BetaContentBlock](https://platform.claude.com/docs/en/api/beta#beta_content_block)

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```
[{"type": "text", "text": "Hi, I'm Claude."}]
```

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```
[\
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},\
  {"role": "assistant", "content": "The best answer is ("}\
]
```

Then the response `content` might be:

```
[{"type": "text", "text": "B)"}]
```

Accepts one of the following:

BetaTextBlock = object {citations, text, type}

citations: array of [BetaTextCitation](https://platform.claude.com/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

BetaThinkingBlock = object {signature, thinking, type}

signature: string

thinking: string

type: "thinking"

BetaRedactedThinkingBlock = object {data, type}

data: string

type: "redacted\_thinking"

BetaToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: string

type: "tool\_use"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaServerToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: "web\_search"or"web\_fetch"or"code\_execution"or4 more

Accepts one of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaWebSearchToolResultBlock = object {content, tool\_use\_id, type, caller}

content: [BetaWebSearchToolResultBlockContent](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError = object {error\_code, type}

error\_code: [BetaWebSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

UnionMember1 = array of [BetaWebSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_web_search_result_block) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaWebFetchToolResultBlock = object {content, tool\_use\_id, type, caller}

content: [BetaWebFetchToolResultErrorBlock](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error\_code, type } or[BetaWebFetchBlock](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_block) { content, retrieved\_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock = object {error\_code, type}

error\_code: [BetaWebFetchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

BetaWebFetchBlock = object {content, retrieved\_at, type, url}

content: [BetaDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](https://platform.claude.com/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](https://platform.claude.com/docs/en/api/beta#beta_base64_pdf_source) { data, media\_type, type } or[BetaPlainTextSource](https://platform.claude.com/docs/en/api/beta#beta_plain_text_source) { data, media\_type, type }

Accepts one of the following:

BetaBase64PDFSource = object {data, media\_type, type}

data: string

media\_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object {data, media\_type, type}

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaCodeExecutionToolResultBlockContent](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

BetaCodeExecutionToolResultError = object {error\_code, type}

error\_code: [BetaCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

BetaCodeExecutionResultBlock = object {content, return\_code, stderr, 2 more}

content: array of [BetaCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

BetaEncryptedCodeExecutionResultBlock = object {content, encrypted\_stdout, return\_code, 2 more}

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

BetaBashCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaBashCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error\_code, type } or[BetaBashCodeExecutionResultBlock](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return\_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError = object {error\_code, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

BetaBashCodeExecutionResultBlock = object {content, return\_code, stderr, 2 more}

content: array of [BetaBashCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_output_block) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

BetaTextEditorCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaTextEditorCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error\_code, error\_message, type } or[BetaTextEditorCodeExecutionViewResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file\_type, num\_lines, 3 more } or[BetaTextEditorCodeExecutionCreateResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is\_file\_update, type } or[BetaTextEditorCodeExecutionStrReplaceResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new\_lines, new\_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError = object {error\_code, error\_message, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

BetaTextEditorCodeExecutionViewResultBlock = object {content, file\_type, num\_lines, 3 more}

content: string

file\_type: "text"or"image"or"pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

BetaTextEditorCodeExecutionCreateResultBlock = object {is\_file\_update, type}

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock = object {lines, new\_lines, new\_start, 3 more}

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

BetaToolSearchToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaToolSearchToolResultError](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_result_error) { error\_code, error\_message, type } or[BetaToolSearchToolSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool\_references, type }

Accepts one of the following:

BetaToolSearchToolResultError = object {error\_code, error\_message, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or"execution\_time\_exceeded"

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

BetaToolSearchToolSearchResultBlock = object {tool\_references, type}

tool\_references: array of [BetaToolReferenceBlock](https://platform.claude.com/docs/en/api/beta#beta_tool_reference_block) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

BetaMCPToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

BetaMCPToolResultBlock = object {content, is\_error, tool\_use\_id, type}

content: stringorarray of [BetaTextBlock](https://platform.claude.com/docs/en/api/beta#beta_text_block) { citations, text, type }

Accepts one of the following:

UnionMember0 = string

BetaMCPToolResultBlockContent = array of [BetaTextBlock](https://platform.claude.com/docs/en/api/beta#beta_text_block) { citations, text, type }

citations: array of [BetaTextCitation](https://platform.claude.com/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"

BetaContainerUploadBlock = object {file\_id, type}

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

BetaCompactionBlock = object {content, type}

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

context\_management: [BetaContextManagementResponse](https://platform.claude.com/docs/en/api/beta#beta_context_management_response) { applied\_edits }

Context management response.

Information about context management strategies applied during the request.

applied\_edits: array of [BetaClearToolUses20250919EditResponse](https://platform.claude.com/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared\_input\_tokens, cleared\_tool\_uses, type } or[BetaClearThinking20251015EditResponse](https://platform.claude.com/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared\_input\_tokens, cleared\_thinking\_turns, type }

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse = object {cleared\_input\_tokens, cleared\_tool\_uses, type}

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

BetaClearThinking20251015EditResponse = object {cleared\_input\_tokens, cleared\_thinking\_turns, type}

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.

model: [Model](https://platform.claude.com/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = "claude-opus-4-6"or"claude-sonnet-4-6"or"claude-haiku-4-5"or12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

"claude-opus-4-0"

Powerful model for complex tasks

"claude-opus-4-20250514"

Powerful model for complex tasks

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-3-haiku-20240307"

Fast and cost-effective model

UnionMember1 = string

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_reason: [BetaStopReason](https://platform.claude.com/docs/en/api/beta#beta_stop_reason)

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

Accepts one of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: [BetaUsage](https://platform.claude.com/docs/en/api/beta#beta_usage) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

inference\_geo: string

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.

iterations: [BetaIterationsUsage](https://platform.claude.com/docs/en/api/beta#beta_iterations_usage) { ,  }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage = object {cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more}

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

BetaCompactionIterationUsage = object {cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more}

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output\_tokens: number

The number of output tokens which were used.

server\_tool\_use: [BetaServerToolUsage](https://platform.claude.com/docs/en/api/beta#beta_server_tool_usage) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

service\_tier: "standard"or"priority"or"batch"

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

speed: "standard"or"fast"

The inference speed mode used for this request.

Accepts one of the following:

"standard"

"fast"

BetaMessageDeltaUsage = object {cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 3 more}

cache\_creation\_input\_tokens: number

The cumulative number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The cumulative number of input tokens read from the cache.

input\_tokens: number

The cumulative number of input tokens which were used.

iterations: [BetaIterationsUsage](https://platform.claude.com/docs/en/api/beta#beta_iterations_usage) { ,  }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage = object {cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more}

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

BetaCompactionIterationUsage = object {cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more}

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output\_tokens: number

The cumulative number of output tokens which were used.

server\_tool\_use: [BetaServerToolUsage](https://platform.claude.com/docs/en/api/beta#beta_server_tool_usage) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

BetaMessageIterationUsage = object {cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more}

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

BetaMessageParam = object {content, role}

content: stringorarray of [BetaContentBlockParam](https://platform.claude.com/docs/en/api/beta#beta_content_block_param)

Accepts one of the following:

UnionMember0 = string

UnionMember1 = array of [BetaContentBlockParam](https://platform.claude.com/docs/en/api/beta#beta_content_block_param)

Accepts one of the following:

BetaTextBlockParam = object {text, type, cache\_control, citations}

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

BetaImageBlockParam = object {source, type, cache\_control}

source: [BetaBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_base64_image_source) { data, media\_type, type } or[BetaURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_url_image_source) { type, url } or[BetaFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_file_image_source) { file\_id, type }

Accepts one of the following:

BetaBase64ImageSource = object {data, media\_type, type}

data: string

media\_type: "image/jpeg"or"image/png"or"image/gif"or"image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object {type, url}

type: "url"

url: string

BetaFileImageSource = object {file\_id, type}

file\_id: string

type: "file"

type: "image"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaRequestDocumentBlock = object {source, type, cache\_control, 3 more}

source: [BetaBase64PDFSource](https://platform.claude.com/docs/en/api/beta#beta_base64_pdf_source) { data, media\_type, type } or[BetaPlainTextSource](https://platform.claude.com/docs/en/api/beta#beta_plain_text_source) { data, media\_type, type } or[BetaContentBlockSource](https://platform.claude.com/docs/en/api/beta#beta_content_block_source) { content, type } or2 more

Accepts one of the following:

BetaBase64PDFSource = object {data, media\_type, type}

data: string

media\_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object {data, media\_type, type}

data: string

media\_type: "text/plain"

type: "text"

BetaContentBlockSource = object {content, type}

content: stringorarray of [BetaContentBlockSourceContent](https://platform.claude.com/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

UnionMember0 = string

BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](https://platform.claude.com/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

BetaTextBlockParam = object {text, type, cache\_control, citations}

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

BetaImageBlockParam = object {source, type, cache\_control}

source: [BetaBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_base64_image_source) { data, media\_type, type } or[BetaURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_url_image_source) { type, url } or[BetaFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_file_image_source) { file\_id, type }

Accepts one of the following:

BetaBase64ImageSource = object {data, media\_type, type}

data: string

media\_type: "image/jpeg"or"image/png"or"image/gif"or"image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object {type, url}

type: "url"

url: string

BetaFileImageSource = object {file\_id, type}

file\_id: string

type: "file"

type: "image"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

BetaURLPDFSource = object {type, url}

type: "url"

url: string

BetaFileDocumentSource = object {file\_id, type}

file\_id: string

type: "file"

type: "document"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](https://platform.claude.com/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

context: optional string

title: optional string

BetaSearchResultBlockParam = object {content, source, title, 3 more}

content: array of [BetaTextBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_block_param) { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

source: string

title: string

type: "search\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](https://platform.claude.com/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

BetaThinkingBlockParam = object {signature, thinking, type}

signature: string

thinking: string

type: "thinking"

BetaRedactedThinkingBlockParam = object {data, type}

data: string

type: "redacted\_thinking"

BetaToolUseBlockParam = object {id, input, name, 3 more}

id: string

input: map\[unknown\]

name: string

type: "tool\_use"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaToolResultBlockParam = object {tool\_use\_id, type, cache\_control, 2 more}

tool\_use\_id: string

type: "tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content: optional stringorarray of [BetaTextBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_block_param) { text, type, cache\_control, citations } or[BetaImageBlockParam](https://platform.claude.com/docs/en/api/beta#beta_image_block_param) { source, type, cache\_control } or[BetaSearchResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_search_result_block_param) { content, source, title, 3 more } or2 more

Accepts one of the following:

UnionMember0 = string

UnionMember1 = array of [BetaTextBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_block_param) { text, type, cache\_control, citations } or[BetaImageBlockParam](https://platform.claude.com/docs/en/api/beta#beta_image_block_param) { source, type, cache\_control } or[BetaSearchResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_search_result_block_param) { content, source, title, 3 more } or2 more

Accepts one of the following:

BetaTextBlockParam = object {text, type, cache\_control, citations}

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

BetaImageBlockParam = object {source, type, cache\_control}

source: [BetaBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_base64_image_source) { data, media\_type, type } or[BetaURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_url_image_source) { type, url } or[BetaFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_file_image_source) { file\_id, type }

Accepts one of the following:

BetaBase64ImageSource = object {data, media\_type, type}

data: string

media\_type: "image/jpeg"or"image/png"or"image/gif"or"image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object {type, url}

type: "url"

url: string

BetaFileImageSource = object {file\_id, type}

file\_id: string

type: "file"

type: "image"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaSearchResultBlockParam = object {content, source, title, 3 more}

content: array of [BetaTextBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_block_param) { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

source: string

title: string

type: "search\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](https://platform.claude.com/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

BetaRequestDocumentBlock = object {source, type, cache\_control, 3 more}

source: [BetaBase64PDFSource](https://platform.claude.com/docs/en/api/beta#beta_base64_pdf_source) { data, media\_type, type } or[BetaPlainTextSource](https://platform.claude.com/docs/en/api/beta#beta_plain_text_source) { data, media\_type, type } or[BetaContentBlockSource](https://platform.claude.com/docs/en/api/beta#beta_content_block_source) { content, type } or2 more

Accepts one of the following:

BetaBase64PDFSource = object {data, media\_type, type}

data: string

media\_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object {data, media\_type, type}

data: string

media\_type: "text/plain"

type: "text"

BetaContentBlockSource = object {content, type}

content: stringorarray of [BetaContentBlockSourceContent](https://platform.claude.com/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

UnionMember0 = string

BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](https://platform.claude.com/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

BetaTextBlockParam = object {text, type, cache\_control, citations}

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

BetaImageBlockParam = object {source, type, cache\_control}

source: [BetaBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_base64_image_source) { data, media\_type, type } or[BetaURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_url_image_source) { type, url } or[BetaFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_file_image_source) { file\_id, type }

Accepts one of the following:

BetaBase64ImageSource = object {data, media\_type, type}

data: string

media\_type: "image/jpeg"or"image/png"or"image/gif"or"image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object {type, url}

type: "url"

url: string

BetaFileImageSource = object {file\_id, type}

file\_id: string

type: "file"

type: "image"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

BetaURLPDFSource = object {type, url}

type: "url"

url: string

BetaFileDocumentSource = object {file\_id, type}

file\_id: string

type: "file"

type: "document"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](https://platform.claude.com/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

context: optional string

title: optional string

BetaToolReferenceBlockParam = object {tool\_name, type, cache\_control}

Tool reference block that can be included in tool\_result content.

tool\_name: string

type: "tool\_reference"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

is\_error: optional boolean

BetaServerToolUseBlockParam = object {id, input, name, 3 more}

id: string

input: map\[unknown\]

name: "web\_search"or"web\_fetch"or"code\_execution"or4 more

Accepts one of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaWebSearchToolResultBlockParam = object {content, tool\_use\_id, type, 2 more}

content: [BetaWebSearchToolResultBlockParamContent](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_block_param_content)

Accepts one of the following:

ResultBlock = array of [BetaWebSearchResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_web_search_result_block_param) { encrypted\_content, title, type, 2 more }

encrypted\_content: string

title: string

type: "web\_search\_result"

url: string

page\_age: optional string

BetaWebSearchToolRequestError = object {error\_code, type}

error\_code: [BetaWebSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

tool\_use\_id: string

type: "web\_search\_tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaWebFetchToolResultBlockParam = object {content, tool\_use\_id, type, 2 more}

content: [BetaWebFetchToolResultErrorBlockParam](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_block_param) { error\_code, type } or[BetaWebFetchBlockParam](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_block_param) { content, type, url, retrieved\_at }

Accepts one of the following:

BetaWebFetchToolResultErrorBlockParam = object {error\_code, type}

error\_code: [BetaWebFetchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

BetaWebFetchBlockParam = object {content, type, url, retrieved\_at}

content: [BetaRequestDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_request_document_block) { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](https://platform.claude.com/docs/en/api/beta#beta_base64_pdf_source) { data, media\_type, type } or[BetaPlainTextSource](https://platform.claude.com/docs/en/api/beta#beta_plain_text_source) { data, media\_type, type } or[BetaContentBlockSource](https://platform.claude.com/docs/en/api/beta#beta_content_block_source) { content, type } or2 more

Accepts one of the following:

BetaBase64PDFSource = object {data, media\_type, type}

data: string

media\_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object {data, media\_type, type}

data: string

media\_type: "text/plain"

type: "text"

BetaContentBlockSource = object {content, type}

content: stringorarray of [BetaContentBlockSourceContent](https://platform.claude.com/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

UnionMember0 = string

BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](https://platform.claude.com/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

BetaTextBlockParam = object {text, type, cache\_control, citations}

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

BetaImageBlockParam = object {source, type, cache\_control}

source: [BetaBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_base64_image_source) { data, media\_type, type } or[BetaURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_url_image_source) { type, url } or[BetaFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_file_image_source) { file\_id, type }

Accepts one of the following:

BetaBase64ImageSource = object {data, media\_type, type}

data: string

media\_type: "image/jpeg"or"image/png"or"image/gif"or"image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object {type, url}

type: "url"

url: string

BetaFileImageSource = object {file\_id, type}

file\_id: string

type: "file"

type: "image"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

BetaURLPDFSource = object {type, url}

type: "url"

url: string

BetaFileDocumentSource = object {file\_id, type}

file\_id: string

type: "file"

type: "document"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](https://platform.claude.com/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

context: optional string

title: optional string

type: "web\_fetch\_result"

url: string

Fetched content URL

retrieved\_at: optional string

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaCodeExecutionToolResultBlockParam = object {content, tool\_use\_id, type, cache\_control}

content: [BetaCodeExecutionToolResultBlockParamContent](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_block_param_content)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

BetaCodeExecutionToolResultErrorParam = object {error\_code, type}

error\_code: [BetaCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

BetaCodeExecutionResultBlockParam = object {content, return\_code, stderr, 2 more}

content: array of [BetaCodeExecutionOutputBlockParam](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block_param) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

BetaEncryptedCodeExecutionResultBlockParam = object {content, encrypted\_stdout, return\_code, 2 more}

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlockParam](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block_param) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaBashCodeExecutionToolResultBlockParam = object {content, tool\_use\_id, type, cache\_control}

content: [BetaBashCodeExecutionToolResultErrorParam](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_tool_result_error_param) { error\_code, type } or[BetaBashCodeExecutionResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_result_block_param) { content, return\_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultErrorParam = object {error\_code, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

BetaBashCodeExecutionResultBlockParam = object {content, return\_code, stderr, 2 more}

content: array of [BetaBashCodeExecutionOutputBlockParam](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_output_block_param) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaTextEditorCodeExecutionToolResultBlockParam = object {content, tool\_use\_id, type, cache\_control}

content: [BetaTextEditorCodeExecutionToolResultErrorParam](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error_param) { error\_code, type, error\_message } or[BetaTextEditorCodeExecutionViewResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_view_result_block_param) { content, file\_type, type, 3 more } or[BetaTextEditorCodeExecutionCreateResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_create_result_block_param) { is\_file\_update, type } or[BetaTextEditorCodeExecutionStrReplaceResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block_param) { type, lines, new\_lines, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultErrorParam = object {error\_code, type, error\_message}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

type: "text\_editor\_code\_execution\_tool\_result\_error"

error\_message: optional string

BetaTextEditorCodeExecutionViewResultBlockParam = object {content, file\_type, type, 3 more}

content: string

file\_type: "text"or"image"or"pdf"

Accepts one of the following:

"text"

"image"

"pdf"

type: "text\_editor\_code\_execution\_view\_result"

num\_lines: optional number

start\_line: optional number

total\_lines: optional number

BetaTextEditorCodeExecutionCreateResultBlockParam = object {is\_file\_update, type}

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

BetaTextEditorCodeExecutionStrReplaceResultBlockParam = object {type, lines, new\_lines, 3 more}

type: "text\_editor\_code\_execution\_str\_replace\_result"

lines: optional array of string

new\_lines: optional number

new\_start: optional number

old\_lines: optional number

old\_start: optional number

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaToolSearchToolResultBlockParam = object {content, tool\_use\_id, type, cache\_control}

content: [BetaToolSearchToolResultErrorParam](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_result_error_param) { error\_code, type } or[BetaToolSearchToolSearchResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_search_result_block_param) { tool\_references, type }

Accepts one of the following:

BetaToolSearchToolResultErrorParam = object {error\_code, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or"execution\_time\_exceeded"

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "tool\_search\_tool\_result\_error"

BetaToolSearchToolSearchResultBlockParam = object {tool\_references, type}

tool\_references: array of [BetaToolReferenceBlockParam](https://platform.claude.com/docs/en/api/beta#beta_tool_reference_block_param) { tool\_name, type, cache\_control }

tool\_name: string

type: "tool\_reference"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaMCPToolUseBlockParam = object {id, input, name, 3 more}

id: string

input: map\[unknown\]

name: string

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaRequestMCPToolResultBlockParam = object {tool\_use\_id, type, cache\_control, 2 more}

tool\_use\_id: string

type: "mcp\_tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content: optional stringorarray of [BetaTextBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_block_param) { text, type, cache\_control, citations }

Accepts one of the following:

UnionMember0 = string

BetaMCPToolResultBlockParamContent = array of [BetaTextBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_block_param) { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

is\_error: optional boolean

BetaContainerUploadBlockParam = object {file\_id, type, cache\_control}

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: string

type: "container\_upload"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaCompactionBlockParam = object {content, type, cache\_control}

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

content: string

Summary of previously compacted content, or null if compaction failed

type: "compaction"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

role: "user"or"assistant"

Accepts one of the following:

"user"

"assistant"

BetaMessageTokensCount = object {context\_management, input\_tokens}

context\_management: [BetaCountTokensContextManagementResponse](https://platform.claude.com/docs/en/api/beta#beta_count_tokens_context_management_response) { original\_input\_tokens }

Information about context management applied to the message.

original\_input\_tokens: number

The original token count before context management was applied

input\_tokens: number

The total number of tokens across the provided list of messages, system prompt, and tools.

BetaMetadata = object {user\_id}

user\_id: optional string

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength256

BetaOutputConfig = object {effort, format}

effort: optional "low"or"medium"or"high"or"max"

All possible effort levels.

Accepts one of the following:

"low"

"medium"

"high"

"max"

format: optional [BetaJSONOutputFormat](https://platform.claude.com/docs/en/api/beta#beta_json_output_format) { schema, type }

A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

schema: map\[unknown\]

The JSON schema of the format

type: "json\_schema"

BetaPlainTextSource = object {data, media\_type, type}

data: string

media\_type: "text/plain"

type: "text"

BetaRawContentBlockDelta = [BetaTextDelta](https://platform.claude.com/docs/en/api/beta#beta_text_delta) { text, type } or[BetaInputJSONDelta](https://platform.claude.com/docs/en/api/beta#beta_input_json_delta) { partial\_json, type } or[BetaCitationsDelta](https://platform.claude.com/docs/en/api/beta#beta_citations_delta) { citation, type } or3 more

Accepts one of the following:

BetaTextDelta = object {text, type}

text: string

type: "text\_delta"

BetaInputJSONDelta = object {partial\_json, type}

partial\_json: string

type: "input\_json\_delta"

BetaCitationsDelta = object {citation, type}

citation: [BetaCitationCharLocation](https://platform.claude.com/docs/en/api/beta#beta_citation_char_location) { cited\_text, document\_index, document\_title, 4 more } or[BetaCitationPageLocation](https://platform.claude.com/docs/en/api/beta#beta_citation_page_location) { cited\_text, document\_index, document\_title, 4 more } or[BetaCitationContentBlockLocation](https://platform.claude.com/docs/en/api/beta#beta_citation_content_block_location) { cited\_text, document\_index, document\_title, 4 more } or2 more

Accepts one of the following:

BetaCitationCharLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

type: "citations\_delta"

BetaThinkingDelta = object {thinking, type}

thinking: string

type: "thinking\_delta"

BetaSignatureDelta = object {signature, type}

signature: string

type: "signature\_delta"

BetaCompactionContentBlockDelta = object {content, type}

content: string

type: "compaction\_delta"

BetaRawContentBlockDeltaEvent = object {delta, index, type}

delta: [BetaRawContentBlockDelta](https://platform.claude.com/docs/en/api/beta#beta_raw_content_block_delta)

Accepts one of the following:

BetaTextDelta = object {text, type}

text: string

type: "text\_delta"

BetaInputJSONDelta = object {partial\_json, type}

partial\_json: string

type: "input\_json\_delta"

BetaCitationsDelta = object {citation, type}

citation: [BetaCitationCharLocation](https://platform.claude.com/docs/en/api/beta#beta_citation_char_location) { cited\_text, document\_index, document\_title, 4 more } or[BetaCitationPageLocation](https://platform.claude.com/docs/en/api/beta#beta_citation_page_location) { cited\_text, document\_index, document\_title, 4 more } or[BetaCitationContentBlockLocation](https://platform.claude.com/docs/en/api/beta#beta_citation_content_block_location) { cited\_text, document\_index, document\_title, 4 more } or2 more

Accepts one of the following:

BetaCitationCharLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

type: "citations\_delta"

BetaThinkingDelta = object {thinking, type}

thinking: string

type: "thinking\_delta"

BetaSignatureDelta = object {signature, type}

signature: string

type: "signature\_delta"

BetaCompactionContentBlockDelta = object {content, type}

content: string

type: "compaction\_delta"

index: number

type: "content\_block\_delta"

BetaRawContentBlockStartEvent = object {content\_block, index, type}

content\_block: [BetaTextBlock](https://platform.claude.com/docs/en/api/beta#beta_text_block) { citations, text, type } or[BetaThinkingBlock](https://platform.claude.com/docs/en/api/beta#beta_thinking_block) { signature, thinking, type } or[BetaRedactedThinkingBlock](https://platform.claude.com/docs/en/api/beta#beta_redacted_thinking_block) { data, type } or12 more

Response model for a file uploaded to the container.

Accepts one of the following:

BetaTextBlock = object {citations, text, type}

citations: array of [BetaTextCitation](https://platform.claude.com/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

BetaThinkingBlock = object {signature, thinking, type}

signature: string

thinking: string

type: "thinking"

BetaRedactedThinkingBlock = object {data, type}

data: string

type: "redacted\_thinking"

BetaToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: string

type: "tool\_use"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaServerToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: "web\_search"or"web\_fetch"or"code\_execution"or4 more

Accepts one of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaWebSearchToolResultBlock = object {content, tool\_use\_id, type, caller}

content: [BetaWebSearchToolResultBlockContent](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError = object {error\_code, type}

error\_code: [BetaWebSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

UnionMember1 = array of [BetaWebSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_web_search_result_block) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaWebFetchToolResultBlock = object {content, tool\_use\_id, type, caller}

content: [BetaWebFetchToolResultErrorBlock](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error\_code, type } or[BetaWebFetchBlock](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_block) { content, retrieved\_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock = object {error\_code, type}

error\_code: [BetaWebFetchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

BetaWebFetchBlock = object {content, retrieved\_at, type, url}

content: [BetaDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](https://platform.claude.com/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](https://platform.claude.com/docs/en/api/beta#beta_base64_pdf_source) { data, media\_type, type } or[BetaPlainTextSource](https://platform.claude.com/docs/en/api/beta#beta_plain_text_source) { data, media\_type, type }

Accepts one of the following:

BetaBase64PDFSource = object {data, media\_type, type}

data: string

media\_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object {data, media\_type, type}

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaCodeExecutionToolResultBlockContent](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

BetaCodeExecutionToolResultError = object {error\_code, type}

error\_code: [BetaCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

BetaCodeExecutionResultBlock = object {content, return\_code, stderr, 2 more}

content: array of [BetaCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

BetaEncryptedCodeExecutionResultBlock = object {content, encrypted\_stdout, return\_code, 2 more}

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

BetaBashCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaBashCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error\_code, type } or[BetaBashCodeExecutionResultBlock](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return\_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError = object {error\_code, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

BetaBashCodeExecutionResultBlock = object {content, return\_code, stderr, 2 more}

content: array of [BetaBashCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_output_block) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

BetaTextEditorCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaTextEditorCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error\_code, error\_message, type } or[BetaTextEditorCodeExecutionViewResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file\_type, num\_lines, 3 more } or[BetaTextEditorCodeExecutionCreateResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is\_file\_update, type } or[BetaTextEditorCodeExecutionStrReplaceResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new\_lines, new\_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError = object {error\_code, error\_message, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

BetaTextEditorCodeExecutionViewResultBlock = object {content, file\_type, num\_lines, 3 more}

content: string

file\_type: "text"or"image"or"pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

BetaTextEditorCodeExecutionCreateResultBlock = object {is\_file\_update, type}

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock = object {lines, new\_lines, new\_start, 3 more}

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

BetaToolSearchToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaToolSearchToolResultError](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_result_error) { error\_code, error\_message, type } or[BetaToolSearchToolSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool\_references, type }

Accepts one of the following:

BetaToolSearchToolResultError = object {error\_code, error\_message, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or"execution\_time\_exceeded"

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

BetaToolSearchToolSearchResultBlock = object {tool\_references, type}

tool\_references: array of [BetaToolReferenceBlock](https://platform.claude.com/docs/en/api/beta#beta_tool_reference_block) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

BetaMCPToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

BetaMCPToolResultBlock = object {content, is\_error, tool\_use\_id, type}

content: stringorarray of [BetaTextBlock](https://platform.claude.com/docs/en/api/beta#beta_text_block) { citations, text, type }

Accepts one of the following:

UnionMember0 = string

BetaMCPToolResultBlockContent = array of [BetaTextBlock](https://platform.claude.com/docs/en/api/beta#beta_text_block) { citations, text, type }

citations: array of [BetaTextCitation](https://platform.claude.com/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"

BetaContainerUploadBlock = object {file\_id, type}

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

BetaCompactionBlock = object {content, type}

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

index: number

type: "content\_block\_start"

BetaRawContentBlockStopEvent = object {index, type}

index: number

type: "content\_block\_stop"

BetaRawMessageDeltaEvent = object {context\_management, delta, type, usage}

context\_management: [BetaContextManagementResponse](https://platform.claude.com/docs/en/api/beta#beta_context_management_response) { applied\_edits }

Information about context management strategies applied during the request

applied\_edits: array of [BetaClearToolUses20250919EditResponse](https://platform.claude.com/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared\_input\_tokens, cleared\_tool\_uses, type } or[BetaClearThinking20251015EditResponse](https://platform.claude.com/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared\_input\_tokens, cleared\_thinking\_turns, type }

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse = object {cleared\_input\_tokens, cleared\_tool\_uses, type}

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

BetaClearThinking20251015EditResponse = object {cleared\_input\_tokens, cleared\_thinking\_turns, type}

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.

delta: object {container, stop\_reason, stop\_sequence}

container: [BetaContainer](https://platform.claude.com/docs/en/api/beta#beta_container) { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

skills: array of [BetaSkill](https://platform.claude.com/docs/en/api/beta#beta_skill) { skill\_id, type, version }

Skills loaded in the container

skill\_id: string

Skill ID

type: "anthropic"or"custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

stop\_reason: [BetaStopReason](https://platform.claude.com/docs/en/api/beta#beta_stop_reason)

Accepts one of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: string

type: "message\_delta"

usage: [BetaMessageDeltaUsage](https://platform.claude.com/docs/en/api/beta#beta_message_delta_usage) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 3 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation\_input\_tokens: number

The cumulative number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The cumulative number of input tokens read from the cache.

input\_tokens: number

The cumulative number of input tokens which were used.

iterations: [BetaIterationsUsage](https://platform.claude.com/docs/en/api/beta#beta_iterations_usage) { ,  }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage = object {cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more}

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

BetaCompactionIterationUsage = object {cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more}

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output\_tokens: number

The cumulative number of output tokens which were used.

server\_tool\_use: [BetaServerToolUsage](https://platform.claude.com/docs/en/api/beta#beta_server_tool_usage) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

BetaRawMessageStartEvent = object {message, type}

message: [BetaMessage](https://platform.claude.com/docs/en/api/beta#beta_message) { id, container, content, 7 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](https://platform.claude.com/docs/en/api/beta#beta_container) { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

skills: array of [BetaSkill](https://platform.claude.com/docs/en/api/beta#beta_skill) { skill\_id, type, version }

Skills loaded in the container

skill\_id: string

Skill ID

type: "anthropic"or"custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

content: array of [BetaContentBlock](https://platform.claude.com/docs/en/api/beta#beta_content_block)

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```
[{"type": "text", "text": "Hi, I'm Claude."}]
```

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```
[\
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},\
  {"role": "assistant", "content": "The best answer is ("}\
]
```

Then the response `content` might be:

```
[{"type": "text", "text": "B)"}]
```

Accepts one of the following:

BetaTextBlock = object {citations, text, type}

citations: array of [BetaTextCitation](https://platform.claude.com/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

BetaThinkingBlock = object {signature, thinking, type}

signature: string

thinking: string

type: "thinking"

BetaRedactedThinkingBlock = object {data, type}

data: string

type: "redacted\_thinking"

BetaToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: string

type: "tool\_use"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaServerToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: "web\_search"or"web\_fetch"or"code\_execution"or4 more

Accepts one of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaWebSearchToolResultBlock = object {content, tool\_use\_id, type, caller}

content: [BetaWebSearchToolResultBlockContent](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError = object {error\_code, type}

error\_code: [BetaWebSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

UnionMember1 = array of [BetaWebSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_web_search_result_block) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaWebFetchToolResultBlock = object {content, tool\_use\_id, type, caller}

content: [BetaWebFetchToolResultErrorBlock](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error\_code, type } or[BetaWebFetchBlock](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_block) { content, retrieved\_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock = object {error\_code, type}

error\_code: [BetaWebFetchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

BetaWebFetchBlock = object {content, retrieved\_at, type, url}

content: [BetaDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](https://platform.claude.com/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](https://platform.claude.com/docs/en/api/beta#beta_base64_pdf_source) { data, media\_type, type } or[BetaPlainTextSource](https://platform.claude.com/docs/en/api/beta#beta_plain_text_source) { data, media\_type, type }

Accepts one of the following:

BetaBase64PDFSource = object {data, media\_type, type}

data: string

media\_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object {data, media\_type, type}

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaCodeExecutionToolResultBlockContent](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

BetaCodeExecutionToolResultError = object {error\_code, type}

error\_code: [BetaCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

BetaCodeExecutionResultBlock = object {content, return\_code, stderr, 2 more}

content: array of [BetaCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

BetaEncryptedCodeExecutionResultBlock = object {content, encrypted\_stdout, return\_code, 2 more}

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

BetaBashCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaBashCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error\_code, type } or[BetaBashCodeExecutionResultBlock](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return\_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError = object {error\_code, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

BetaBashCodeExecutionResultBlock = object {content, return\_code, stderr, 2 more}

content: array of [BetaBashCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_output_block) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

BetaTextEditorCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaTextEditorCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error\_code, error\_message, type } or[BetaTextEditorCodeExecutionViewResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file\_type, num\_lines, 3 more } or[BetaTextEditorCodeExecutionCreateResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is\_file\_update, type } or[BetaTextEditorCodeExecutionStrReplaceResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new\_lines, new\_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError = object {error\_code, error\_message, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

BetaTextEditorCodeExecutionViewResultBlock = object {content, file\_type, num\_lines, 3 more}

content: string

file\_type: "text"or"image"or"pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

BetaTextEditorCodeExecutionCreateResultBlock = object {is\_file\_update, type}

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock = object {lines, new\_lines, new\_start, 3 more}

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

BetaToolSearchToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaToolSearchToolResultError](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_result_error) { error\_code, error\_message, type } or[BetaToolSearchToolSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool\_references, type }

Accepts one of the following:

BetaToolSearchToolResultError = object {error\_code, error\_message, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or"execution\_time\_exceeded"

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

BetaToolSearchToolSearchResultBlock = object {tool\_references, type}

tool\_references: array of [BetaToolReferenceBlock](https://platform.claude.com/docs/en/api/beta#beta_tool_reference_block) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

BetaMCPToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

BetaMCPToolResultBlock = object {content, is\_error, tool\_use\_id, type}

content: stringorarray of [BetaTextBlock](https://platform.claude.com/docs/en/api/beta#beta_text_block) { citations, text, type }

Accepts one of the following:

UnionMember0 = string

BetaMCPToolResultBlockContent = array of [BetaTextBlock](https://platform.claude.com/docs/en/api/beta#beta_text_block) { citations, text, type }

citations: array of [BetaTextCitation](https://platform.claude.com/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"

BetaContainerUploadBlock = object {file\_id, type}

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

BetaCompactionBlock = object {content, type}

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

context\_management: [BetaContextManagementResponse](https://platform.claude.com/docs/en/api/beta#beta_context_management_response) { applied\_edits }

Context management response.

Information about context management strategies applied during the request.

applied\_edits: array of [BetaClearToolUses20250919EditResponse](https://platform.claude.com/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared\_input\_tokens, cleared\_tool\_uses, type } or[BetaClearThinking20251015EditResponse](https://platform.claude.com/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared\_input\_tokens, cleared\_thinking\_turns, type }

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse = object {cleared\_input\_tokens, cleared\_tool\_uses, type}

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

BetaClearThinking20251015EditResponse = object {cleared\_input\_tokens, cleared\_thinking\_turns, type}

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.

model: [Model](https://platform.claude.com/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = "claude-opus-4-6"or"claude-sonnet-4-6"or"claude-haiku-4-5"or12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

"claude-opus-4-0"

Powerful model for complex tasks

"claude-opus-4-20250514"

Powerful model for complex tasks

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-3-haiku-20240307"

Fast and cost-effective model

UnionMember1 = string

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_reason: [BetaStopReason](https://platform.claude.com/docs/en/api/beta#beta_stop_reason)

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

Accepts one of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: [BetaUsage](https://platform.claude.com/docs/en/api/beta#beta_usage) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

inference\_geo: string

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.

iterations: [BetaIterationsUsage](https://platform.claude.com/docs/en/api/beta#beta_iterations_usage) { ,  }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage = object {cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more}

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

BetaCompactionIterationUsage = object {cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more}

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output\_tokens: number

The number of output tokens which were used.

server\_tool\_use: [BetaServerToolUsage](https://platform.claude.com/docs/en/api/beta#beta_server_tool_usage) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

service\_tier: "standard"or"priority"or"batch"

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

speed: "standard"or"fast"

The inference speed mode used for this request.

Accepts one of the following:

"standard"

"fast"

type: "message\_start"

BetaRawMessageStopEvent = object {type}

type: "message\_stop"

BetaRawMessageStreamEvent = [BetaRawMessageStartEvent](https://platform.claude.com/docs/en/api/beta#beta_raw_message_start_event) { message, type } or[BetaRawMessageDeltaEvent](https://platform.claude.com/docs/en/api/beta#beta_raw_message_delta_event) { context\_management, delta, type, usage } or[BetaRawMessageStopEvent](https://platform.claude.com/docs/en/api/beta#beta_raw_message_stop_event) { type } or3 more

Accepts one of the following:

BetaRawMessageStartEvent = object {message, type}

message: [BetaMessage](https://platform.claude.com/docs/en/api/beta#beta_message) { id, container, content, 7 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](https://platform.claude.com/docs/en/api/beta#beta_container) { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

skills: array of [BetaSkill](https://platform.claude.com/docs/en/api/beta#beta_skill) { skill\_id, type, version }

Skills loaded in the container

skill\_id: string

Skill ID

type: "anthropic"or"custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

content: array of [BetaContentBlock](https://platform.claude.com/docs/en/api/beta#beta_content_block)

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```
[{"type": "text", "text": "Hi, I'm Claude."}]
```

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```
[\
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},\
  {"role": "assistant", "content": "The best answer is ("}\
]
```

Then the response `content` might be:

```
[{"type": "text", "text": "B)"}]
```

Accepts one of the following:

BetaTextBlock = object {citations, text, type}

citations: array of [BetaTextCitation](https://platform.claude.com/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

BetaThinkingBlock = object {signature, thinking, type}

signature: string

thinking: string

type: "thinking"

BetaRedactedThinkingBlock = object {data, type}

data: string

type: "redacted\_thinking"

BetaToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: string

type: "tool\_use"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaServerToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: "web\_search"or"web\_fetch"or"code\_execution"or4 more

Accepts one of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaWebSearchToolResultBlock = object {content, tool\_use\_id, type, caller}

content: [BetaWebSearchToolResultBlockContent](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError = object {error\_code, type}

error\_code: [BetaWebSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

UnionMember1 = array of [BetaWebSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_web_search_result_block) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaWebFetchToolResultBlock = object {content, tool\_use\_id, type, caller}

content: [BetaWebFetchToolResultErrorBlock](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error\_code, type } or[BetaWebFetchBlock](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_block) { content, retrieved\_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock = object {error\_code, type}

error\_code: [BetaWebFetchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

BetaWebFetchBlock = object {content, retrieved\_at, type, url}

content: [BetaDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](https://platform.claude.com/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](https://platform.claude.com/docs/en/api/beta#beta_base64_pdf_source) { data, media\_type, type } or[BetaPlainTextSource](https://platform.claude.com/docs/en/api/beta#beta_plain_text_source) { data, media\_type, type }

Accepts one of the following:

BetaBase64PDFSource = object {data, media\_type, type}

data: string

media\_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object {data, media\_type, type}

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaCodeExecutionToolResultBlockContent](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

BetaCodeExecutionToolResultError = object {error\_code, type}

error\_code: [BetaCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

BetaCodeExecutionResultBlock = object {content, return\_code, stderr, 2 more}

content: array of [BetaCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

BetaEncryptedCodeExecutionResultBlock = object {content, encrypted\_stdout, return\_code, 2 more}

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

BetaBashCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaBashCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error\_code, type } or[BetaBashCodeExecutionResultBlock](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return\_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError = object {error\_code, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

BetaBashCodeExecutionResultBlock = object {content, return\_code, stderr, 2 more}

content: array of [BetaBashCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_output_block) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

BetaTextEditorCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaTextEditorCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error\_code, error\_message, type } or[BetaTextEditorCodeExecutionViewResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file\_type, num\_lines, 3 more } or[BetaTextEditorCodeExecutionCreateResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is\_file\_update, type } or[BetaTextEditorCodeExecutionStrReplaceResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new\_lines, new\_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError = object {error\_code, error\_message, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

BetaTextEditorCodeExecutionViewResultBlock = object {content, file\_type, num\_lines, 3 more}

content: string

file\_type: "text"or"image"or"pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

BetaTextEditorCodeExecutionCreateResultBlock = object {is\_file\_update, type}

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock = object {lines, new\_lines, new\_start, 3 more}

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

BetaToolSearchToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaToolSearchToolResultError](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_result_error) { error\_code, error\_message, type } or[BetaToolSearchToolSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool\_references, type }

Accepts one of the following:

BetaToolSearchToolResultError = object {error\_code, error\_message, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or"execution\_time\_exceeded"

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

BetaToolSearchToolSearchResultBlock = object {tool\_references, type}

tool\_references: array of [BetaToolReferenceBlock](https://platform.claude.com/docs/en/api/beta#beta_tool_reference_block) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

BetaMCPToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

BetaMCPToolResultBlock = object {content, is\_error, tool\_use\_id, type}

content: stringorarray of [BetaTextBlock](https://platform.claude.com/docs/en/api/beta#beta_text_block) { citations, text, type }

Accepts one of the following:

UnionMember0 = string

BetaMCPToolResultBlockContent = array of [BetaTextBlock](https://platform.claude.com/docs/en/api/beta#beta_text_block) { citations, text, type }

citations: array of [BetaTextCitation](https://platform.claude.com/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"

BetaContainerUploadBlock = object {file\_id, type}

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

BetaCompactionBlock = object {content, type}

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

context\_management: [BetaContextManagementResponse](https://platform.claude.com/docs/en/api/beta#beta_context_management_response) { applied\_edits }

Context management response.

Information about context management strategies applied during the request.

applied\_edits: array of [BetaClearToolUses20250919EditResponse](https://platform.claude.com/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared\_input\_tokens, cleared\_tool\_uses, type } or[BetaClearThinking20251015EditResponse](https://platform.claude.com/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared\_input\_tokens, cleared\_thinking\_turns, type }

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse = object {cleared\_input\_tokens, cleared\_tool\_uses, type}

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

BetaClearThinking20251015EditResponse = object {cleared\_input\_tokens, cleared\_thinking\_turns, type}

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.

model: [Model](https://platform.claude.com/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = "claude-opus-4-6"or"claude-sonnet-4-6"or"claude-haiku-4-5"or12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

"claude-opus-4-0"

Powerful model for complex tasks

"claude-opus-4-20250514"

Powerful model for complex tasks

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-3-haiku-20240307"

Fast and cost-effective model

UnionMember1 = string

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_reason: [BetaStopReason](https://platform.claude.com/docs/en/api/beta#beta_stop_reason)

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

Accepts one of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: [BetaUsage](https://platform.claude.com/docs/en/api/beta#beta_usage) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

inference\_geo: string

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.

iterations: [BetaIterationsUsage](https://platform.claude.com/docs/en/api/beta#beta_iterations_usage) { ,  }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage = object {cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more}

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

BetaCompactionIterationUsage = object {cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more}

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output\_tokens: number

The number of output tokens which were used.

server\_tool\_use: [BetaServerToolUsage](https://platform.claude.com/docs/en/api/beta#beta_server_tool_usage) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

service\_tier: "standard"or"priority"or"batch"

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

speed: "standard"or"fast"

The inference speed mode used for this request.

Accepts one of the following:

"standard"

"fast"

type: "message\_start"

BetaRawMessageDeltaEvent = object {context\_management, delta, type, usage}

context\_management: [BetaContextManagementResponse](https://platform.claude.com/docs/en/api/beta#beta_context_management_response) { applied\_edits }

Information about context management strategies applied during the request

applied\_edits: array of [BetaClearToolUses20250919EditResponse](https://platform.claude.com/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared\_input\_tokens, cleared\_tool\_uses, type } or[BetaClearThinking20251015EditResponse](https://platform.claude.com/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared\_input\_tokens, cleared\_thinking\_turns, type }

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse = object {cleared\_input\_tokens, cleared\_tool\_uses, type}

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

BetaClearThinking20251015EditResponse = object {cleared\_input\_tokens, cleared\_thinking\_turns, type}

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.

delta: object {container, stop\_reason, stop\_sequence}

container: [BetaContainer](https://platform.claude.com/docs/en/api/beta#beta_container) { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

skills: array of [BetaSkill](https://platform.claude.com/docs/en/api/beta#beta_skill) { skill\_id, type, version }

Skills loaded in the container

skill\_id: string

Skill ID

type: "anthropic"or"custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

stop\_reason: [BetaStopReason](https://platform.claude.com/docs/en/api/beta#beta_stop_reason)

Accepts one of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: string

type: "message\_delta"

usage: [BetaMessageDeltaUsage](https://platform.claude.com/docs/en/api/beta#beta_message_delta_usage) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 3 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation\_input\_tokens: number

The cumulative number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The cumulative number of input tokens read from the cache.

input\_tokens: number

The cumulative number of input tokens which were used.

iterations: [BetaIterationsUsage](https://platform.claude.com/docs/en/api/beta#beta_iterations_usage) { ,  }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage = object {cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more}

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

BetaCompactionIterationUsage = object {cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more}

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output\_tokens: number

The cumulative number of output tokens which were used.

server\_tool\_use: [BetaServerToolUsage](https://platform.claude.com/docs/en/api/beta#beta_server_tool_usage) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

BetaRawMessageStopEvent = object {type}

type: "message\_stop"

BetaRawContentBlockStartEvent = object {content\_block, index, type}

content\_block: [BetaTextBlock](https://platform.claude.com/docs/en/api/beta#beta_text_block) { citations, text, type } or[BetaThinkingBlock](https://platform.claude.com/docs/en/api/beta#beta_thinking_block) { signature, thinking, type } or[BetaRedactedThinkingBlock](https://platform.claude.com/docs/en/api/beta#beta_redacted_thinking_block) { data, type } or12 more

Response model for a file uploaded to the container.

Accepts one of the following:

BetaTextBlock = object {citations, text, type}

citations: array of [BetaTextCitation](https://platform.claude.com/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

BetaThinkingBlock = object {signature, thinking, type}

signature: string

thinking: string

type: "thinking"

BetaRedactedThinkingBlock = object {data, type}

data: string

type: "redacted\_thinking"

BetaToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: string

type: "tool\_use"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaServerToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: "web\_search"or"web\_fetch"or"code\_execution"or4 more

Accepts one of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaWebSearchToolResultBlock = object {content, tool\_use\_id, type, caller}

content: [BetaWebSearchToolResultBlockContent](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError = object {error\_code, type}

error\_code: [BetaWebSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

UnionMember1 = array of [BetaWebSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_web_search_result_block) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaWebFetchToolResultBlock = object {content, tool\_use\_id, type, caller}

content: [BetaWebFetchToolResultErrorBlock](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error\_code, type } or[BetaWebFetchBlock](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_block) { content, retrieved\_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock = object {error\_code, type}

error\_code: [BetaWebFetchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

BetaWebFetchBlock = object {content, retrieved\_at, type, url}

content: [BetaDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](https://platform.claude.com/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](https://platform.claude.com/docs/en/api/beta#beta_base64_pdf_source) { data, media\_type, type } or[BetaPlainTextSource](https://platform.claude.com/docs/en/api/beta#beta_plain_text_source) { data, media\_type, type }

Accepts one of the following:

BetaBase64PDFSource = object {data, media\_type, type}

data: string

media\_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object {data, media\_type, type}

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaCodeExecutionToolResultBlockContent](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

BetaCodeExecutionToolResultError = object {error\_code, type}

error\_code: [BetaCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

BetaCodeExecutionResultBlock = object {content, return\_code, stderr, 2 more}

content: array of [BetaCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

BetaEncryptedCodeExecutionResultBlock = object {content, encrypted\_stdout, return\_code, 2 more}

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

BetaBashCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaBashCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error\_code, type } or[BetaBashCodeExecutionResultBlock](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return\_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError = object {error\_code, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

BetaBashCodeExecutionResultBlock = object {content, return\_code, stderr, 2 more}

content: array of [BetaBashCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_output_block) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

BetaTextEditorCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaTextEditorCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error\_code, error\_message, type } or[BetaTextEditorCodeExecutionViewResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file\_type, num\_lines, 3 more } or[BetaTextEditorCodeExecutionCreateResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is\_file\_update, type } or[BetaTextEditorCodeExecutionStrReplaceResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new\_lines, new\_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError = object {error\_code, error\_message, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

BetaTextEditorCodeExecutionViewResultBlock = object {content, file\_type, num\_lines, 3 more}

content: string

file\_type: "text"or"image"or"pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

BetaTextEditorCodeExecutionCreateResultBlock = object {is\_file\_update, type}

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock = object {lines, new\_lines, new\_start, 3 more}

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

BetaToolSearchToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaToolSearchToolResultError](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_result_error) { error\_code, error\_message, type } or[BetaToolSearchToolSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool\_references, type }

Accepts one of the following:

BetaToolSearchToolResultError = object {error\_code, error\_message, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or"execution\_time\_exceeded"

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

BetaToolSearchToolSearchResultBlock = object {tool\_references, type}

tool\_references: array of [BetaToolReferenceBlock](https://platform.claude.com/docs/en/api/beta#beta_tool_reference_block) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

BetaMCPToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

BetaMCPToolResultBlock = object {content, is\_error, tool\_use\_id, type}

content: stringorarray of [BetaTextBlock](https://platform.claude.com/docs/en/api/beta#beta_text_block) { citations, text, type }

Accepts one of the following:

UnionMember0 = string

BetaMCPToolResultBlockContent = array of [BetaTextBlock](https://platform.claude.com/docs/en/api/beta#beta_text_block) { citations, text, type }

citations: array of [BetaTextCitation](https://platform.claude.com/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"

BetaContainerUploadBlock = object {file\_id, type}

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

BetaCompactionBlock = object {content, type}

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

index: number

type: "content\_block\_start"

BetaRawContentBlockDeltaEvent = object {delta, index, type}

delta: [BetaRawContentBlockDelta](https://platform.claude.com/docs/en/api/beta#beta_raw_content_block_delta)

Accepts one of the following:

BetaTextDelta = object {text, type}

text: string

type: "text\_delta"

BetaInputJSONDelta = object {partial\_json, type}

partial\_json: string

type: "input\_json\_delta"

BetaCitationsDelta = object {citation, type}

citation: [BetaCitationCharLocation](https://platform.claude.com/docs/en/api/beta#beta_citation_char_location) { cited\_text, document\_index, document\_title, 4 more } or[BetaCitationPageLocation](https://platform.claude.com/docs/en/api/beta#beta_citation_page_location) { cited\_text, document\_index, document\_title, 4 more } or[BetaCitationContentBlockLocation](https://platform.claude.com/docs/en/api/beta#beta_citation_content_block_location) { cited\_text, document\_index, document\_title, 4 more } or2 more

Accepts one of the following:

BetaCitationCharLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

type: "citations\_delta"

BetaThinkingDelta = object {thinking, type}

thinking: string

type: "thinking\_delta"

BetaSignatureDelta = object {signature, type}

signature: string

type: "signature\_delta"

BetaCompactionContentBlockDelta = object {content, type}

content: string

type: "compaction\_delta"

index: number

type: "content\_block\_delta"

BetaRawContentBlockStopEvent = object {index, type}

index: number

type: "content\_block\_stop"

BetaRedactedThinkingBlock = object {data, type}

data: string

type: "redacted\_thinking"

BetaRedactedThinkingBlockParam = object {data, type}

data: string

type: "redacted\_thinking"

BetaRequestDocumentBlock = object {source, type, cache\_control, 3 more}

source: [BetaBase64PDFSource](https://platform.claude.com/docs/en/api/beta#beta_base64_pdf_source) { data, media\_type, type } or[BetaPlainTextSource](https://platform.claude.com/docs/en/api/beta#beta_plain_text_source) { data, media\_type, type } or[BetaContentBlockSource](https://platform.claude.com/docs/en/api/beta#beta_content_block_source) { content, type } or2 more

Accepts one of the following:

BetaBase64PDFSource = object {data, media\_type, type}

data: string

media\_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object {data, media\_type, type}

data: string

media\_type: "text/plain"

type: "text"

BetaContentBlockSource = object {content, type}

content: stringorarray of [BetaContentBlockSourceContent](https://platform.claude.com/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

UnionMember0 = string

BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](https://platform.claude.com/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

BetaTextBlockParam = object {text, type, cache\_control, citations}

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

BetaImageBlockParam = object {source, type, cache\_control}

source: [BetaBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_base64_image_source) { data, media\_type, type } or[BetaURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_url_image_source) { type, url } or[BetaFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_file_image_source) { file\_id, type }

Accepts one of the following:

BetaBase64ImageSource = object {data, media\_type, type}

data: string

media\_type: "image/jpeg"or"image/png"or"image/gif"or"image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object {type, url}

type: "url"

url: string

BetaFileImageSource = object {file\_id, type}

file\_id: string

type: "file"

type: "image"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

BetaURLPDFSource = object {type, url}

type: "url"

url: string

BetaFileDocumentSource = object {file\_id, type}

file\_id: string

type: "file"

type: "document"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](https://platform.claude.com/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

context: optional string

title: optional string

BetaRequestMCPServerToolConfiguration = object {allowed\_tools, enabled}

allowed\_tools: optional array of string

enabled: optional boolean

BetaRequestMCPServerURLDefinition = object {name, type, url, 2 more}

name: string

type: "url"

url: string

authorization\_token: optional string

tool\_configuration: optional [BetaRequestMCPServerToolConfiguration](https://platform.claude.com/docs/en/api/beta#beta_request_mcp_server_tool_configuration) { allowed\_tools, enabled }

allowed\_tools: optional array of string

enabled: optional boolean

BetaRequestMCPToolResultBlockParam = object {tool\_use\_id, type, cache\_control, 2 more}

tool\_use\_id: string

type: "mcp\_tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content: optional stringorarray of [BetaTextBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_block_param) { text, type, cache\_control, citations }

Accepts one of the following:

UnionMember0 = string

BetaMCPToolResultBlockParamContent = array of [BetaTextBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_block_param) { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

is\_error: optional boolean

BetaSearchResultBlockParam = object {content, source, title, 3 more}

content: array of [BetaTextBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_block_param) { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

source: string

title: string

type: "search\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](https://platform.claude.com/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaServerToolUsage = object {web\_fetch\_requests, web\_search\_requests}

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

BetaServerToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: "web\_search"or"web\_fetch"or"code\_execution"or4 more

Accepts one of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaServerToolUseBlockParam = object {id, input, name, 3 more}

id: string

input: map\[unknown\]

name: "web\_search"or"web\_fetch"or"code\_execution"or4 more

Accepts one of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaSignatureDelta = object {signature, type}

signature: string

type: "signature\_delta"

BetaSkill = object {skill\_id, type, version}

A skill that was loaded in a container (response model).

skill\_id: string

Skill ID

type: "anthropic"or"custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

BetaSkillParams = object {skill\_id, type, version}

Specification for a skill to be loaded in a container (request model).

skill\_id: string

Skill ID

type: "anthropic"or"custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: optional string

Skill version or 'latest' for most recent version

BetaStopReason = "end\_turn"or"max\_tokens"or"stop\_sequence"or5 more

Accepts one of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

BetaTextBlock = object {citations, text, type}

citations: array of [BetaTextCitation](https://platform.claude.com/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

BetaTextBlockParam = object {text, type, cache\_control, citations}

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

BetaTextCitation = [BetaCitationCharLocation](https://platform.claude.com/docs/en/api/beta#beta_citation_char_location) { cited\_text, document\_index, document\_title, 4 more } or[BetaCitationPageLocation](https://platform.claude.com/docs/en/api/beta#beta_citation_page_location) { cited\_text, document\_index, document\_title, 4 more } or[BetaCitationContentBlockLocation](https://platform.claude.com/docs/en/api/beta#beta_citation_content_block_location) { cited\_text, document\_index, document\_title, 4 more } or2 more

Accepts one of the following:

BetaCitationCharLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

BetaTextCitationParam = [BetaCitationCharLocationParam](https://platform.claude.com/docs/en/api/beta#beta_citation_char_location_param) { cited\_text, document\_index, document\_title, 3 more } or[BetaCitationPageLocationParam](https://platform.claude.com/docs/en/api/beta#beta_citation_page_location_param) { cited\_text, document\_index, document\_title, 3 more } or[BetaCitationContentBlockLocationParam](https://platform.claude.com/docs/en/api/beta#beta_citation_content_block_location_param) { cited\_text, document\_index, document\_title, 3 more } or2 more

Accepts one of the following:

BetaCitationCharLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

BetaTextDelta = object {text, type}

text: string

type: "text\_delta"

BetaTextEditorCodeExecutionCreateResultBlock = object {is\_file\_update, type}

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

BetaTextEditorCodeExecutionCreateResultBlockParam = object {is\_file\_update, type}

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock = object {lines, new\_lines, new\_start, 3 more}

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

BetaTextEditorCodeExecutionStrReplaceResultBlockParam = object {type, lines, new\_lines, 3 more}

type: "text\_editor\_code\_execution\_str\_replace\_result"

lines: optional array of string

new\_lines: optional number

new\_start: optional number

old\_lines: optional number

old\_start: optional number

BetaTextEditorCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaTextEditorCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error\_code, error\_message, type } or[BetaTextEditorCodeExecutionViewResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file\_type, num\_lines, 3 more } or[BetaTextEditorCodeExecutionCreateResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is\_file\_update, type } or[BetaTextEditorCodeExecutionStrReplaceResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new\_lines, new\_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError = object {error\_code, error\_message, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

BetaTextEditorCodeExecutionViewResultBlock = object {content, file\_type, num\_lines, 3 more}

content: string

file\_type: "text"or"image"or"pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

BetaTextEditorCodeExecutionCreateResultBlock = object {is\_file\_update, type}

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock = object {lines, new\_lines, new\_start, 3 more}

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

BetaTextEditorCodeExecutionToolResultBlockParam = object {content, tool\_use\_id, type, cache\_control}

content: [BetaTextEditorCodeExecutionToolResultErrorParam](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error_param) { error\_code, type, error\_message } or[BetaTextEditorCodeExecutionViewResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_view_result_block_param) { content, file\_type, type, 3 more } or[BetaTextEditorCodeExecutionCreateResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_create_result_block_param) { is\_file\_update, type } or[BetaTextEditorCodeExecutionStrReplaceResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block_param) { type, lines, new\_lines, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultErrorParam = object {error\_code, type, error\_message}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

type: "text\_editor\_code\_execution\_tool\_result\_error"

error\_message: optional string

BetaTextEditorCodeExecutionViewResultBlockParam = object {content, file\_type, type, 3 more}

content: string

file\_type: "text"or"image"or"pdf"

Accepts one of the following:

"text"

"image"

"pdf"

type: "text\_editor\_code\_execution\_view\_result"

num\_lines: optional number

start\_line: optional number

total\_lines: optional number

BetaTextEditorCodeExecutionCreateResultBlockParam = object {is\_file\_update, type}

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

BetaTextEditorCodeExecutionStrReplaceResultBlockParam = object {type, lines, new\_lines, 3 more}

type: "text\_editor\_code\_execution\_str\_replace\_result"

lines: optional array of string

new\_lines: optional number

new\_start: optional number

old\_lines: optional number

old\_start: optional number

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaTextEditorCodeExecutionToolResultError = object {error\_code, error\_message, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

BetaTextEditorCodeExecutionToolResultErrorParam = object {error\_code, type, error\_message}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

type: "text\_editor\_code\_execution\_tool\_result\_error"

error\_message: optional string

BetaTextEditorCodeExecutionViewResultBlock = object {content, file\_type, num\_lines, 3 more}

content: string

file\_type: "text"or"image"or"pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

BetaTextEditorCodeExecutionViewResultBlockParam = object {content, file\_type, type, 3 more}

content: string

file\_type: "text"or"image"or"pdf"

Accepts one of the following:

"text"

"image"

"pdf"

type: "text\_editor\_code\_execution\_view\_result"

num\_lines: optional number

start\_line: optional number

total\_lines: optional number

BetaThinkingBlock = object {signature, thinking, type}

signature: string

thinking: string

type: "thinking"

BetaThinkingBlockParam = object {signature, thinking, type}

signature: string

thinking: string

type: "thinking"

BetaThinkingConfigAdaptive = object {type}

type: "adaptive"

BetaThinkingConfigDisabled = object {type}

type: "disabled"

BetaThinkingConfigEnabled = object {budget\_tokens, type}

budget\_tokens: number

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: "enabled"

BetaThinkingConfigParam = [BetaThinkingConfigEnabled](https://platform.claude.com/docs/en/api/beta#beta_thinking_config_enabled) { budget\_tokens, type } or[BetaThinkingConfigDisabled](https://platform.claude.com/docs/en/api/beta#beta_thinking_config_disabled) { type } or[BetaThinkingConfigAdaptive](https://platform.claude.com/docs/en/api/beta#beta_thinking_config_adaptive) { type }

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

Accepts one of the following:

BetaThinkingConfigEnabled = object {budget\_tokens, type}

budget\_tokens: number

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: "enabled"

BetaThinkingConfigDisabled = object {type}

type: "disabled"

BetaThinkingConfigAdaptive = object {type}

type: "adaptive"

BetaThinkingDelta = object {thinking, type}

thinking: string

type: "thinking\_delta"

BetaThinkingTurns = object {type, value}

type: "thinking\_turns"

value: number

BetaTool = object {input\_schema, name, allowed\_callers, 7 more}

input\_schema: object {type, properties, required}

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: "object"

properties: optional map\[unknown\]

required: optional array of string

name: string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

description: optional string

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager\_input\_streaming: optional boolean

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

input\_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

type: optional "custom"

BetaToolBash20241022 = object {name, type, allowed\_callers, 4 more}

name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "bash\_20241022"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolBash20250124 = object {name, type, allowed\_callers, 4 more}

name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "bash\_20250124"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolChoice = [BetaToolChoiceAuto](https://platform.claude.com/docs/en/api/beta#beta_tool_choice_auto) { type, disable\_parallel\_tool\_use } or[BetaToolChoiceAny](https://platform.claude.com/docs/en/api/beta#beta_tool_choice_any) { type, disable\_parallel\_tool\_use } or[BetaToolChoiceTool](https://platform.claude.com/docs/en/api/beta#beta_tool_choice_tool) { name, type, disable\_parallel\_tool\_use } or[BetaToolChoiceNone](https://platform.claude.com/docs/en/api/beta#beta_tool_choice_none) { type }

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Accepts one of the following:

BetaToolChoiceAuto = object {type, disable\_parallel\_tool\_use}

The model will automatically decide whether to use tools.

type: "auto"

disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

BetaToolChoiceAny = object {type, disable\_parallel\_tool\_use}

The model will use any available tools.

type: "any"

disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

BetaToolChoiceTool = object {name, type, disable\_parallel\_tool\_use}

The model will use the specified tool with `tool_choice.name`.

name: string

The name of the tool to use.

type: "tool"

disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

BetaToolChoiceNone = object {type}

The model will not be allowed to use tools.

type: "none"

BetaToolChoiceAny = object {type, disable\_parallel\_tool\_use}

The model will use any available tools.

type: "any"

disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

BetaToolChoiceAuto = object {type, disable\_parallel\_tool\_use}

The model will automatically decide whether to use tools.

type: "auto"

disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

BetaToolChoiceNone = object {type}

The model will not be allowed to use tools.

type: "none"

BetaToolChoiceTool = object {name, type, disable\_parallel\_tool\_use}

The model will use the specified tool with `tool_choice.name`.

name: string

The name of the tool to use.

type: "tool"

disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

BetaToolComputerUse20241022 = object {display\_height\_px, display\_width\_px, name, 7 more}

display\_height\_px: number

The height of the display in pixels.

display\_width\_px: number

The width of the display in pixels.

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer\_20241022"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: optional number

The X11 display number (e.g. 0, 1) for the display.

input\_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolComputerUse20250124 = object {display\_height\_px, display\_width\_px, name, 7 more}

display\_height\_px: number

The height of the display in pixels.

display\_width\_px: number

The width of the display in pixels.

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer\_20250124"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: optional number

The X11 display number (e.g. 0, 1) for the display.

input\_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolComputerUse20251124 = object {display\_height\_px, display\_width\_px, name, 8 more}

display\_height\_px: number

The height of the display in pixels.

display\_width\_px: number

The width of the display in pixels.

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer\_20251124"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: optional number

The X11 display number (e.g. 0, 1) for the display.

enable\_zoom: optional boolean

Whether to enable an action to take a zoomed-in screenshot of the screen.

input\_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolReferenceBlock = object {tool\_name, type}

tool\_name: string

type: "tool\_reference"

BetaToolReferenceBlockParam = object {tool\_name, type, cache\_control}

Tool reference block that can be included in tool\_result content.

tool\_name: string

type: "tool\_reference"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaToolResultBlockParam = object {tool\_use\_id, type, cache\_control, 2 more}

tool\_use\_id: string

type: "tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content: optional stringorarray of [BetaTextBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_block_param) { text, type, cache\_control, citations } or[BetaImageBlockParam](https://platform.claude.com/docs/en/api/beta#beta_image_block_param) { source, type, cache\_control } or[BetaSearchResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_search_result_block_param) { content, source, title, 3 more } or2 more

Accepts one of the following:

UnionMember0 = string

UnionMember1 = array of [BetaTextBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_block_param) { text, type, cache\_control, citations } or[BetaImageBlockParam](https://platform.claude.com/docs/en/api/beta#beta_image_block_param) { source, type, cache\_control } or[BetaSearchResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_search_result_block_param) { content, source, title, 3 more } or2 more

Accepts one of the following:

BetaTextBlockParam = object {text, type, cache\_control, citations}

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

BetaImageBlockParam = object {source, type, cache\_control}

source: [BetaBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_base64_image_source) { data, media\_type, type } or[BetaURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_url_image_source) { type, url } or[BetaFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_file_image_source) { file\_id, type }

Accepts one of the following:

BetaBase64ImageSource = object {data, media\_type, type}

data: string

media\_type: "image/jpeg"or"image/png"or"image/gif"or"image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object {type, url}

type: "url"

url: string

BetaFileImageSource = object {file\_id, type}

file\_id: string

type: "file"

type: "image"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaSearchResultBlockParam = object {content, source, title, 3 more}

content: array of [BetaTextBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_block_param) { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

source: string

title: string

type: "search\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](https://platform.claude.com/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

BetaRequestDocumentBlock = object {source, type, cache\_control, 3 more}

source: [BetaBase64PDFSource](https://platform.claude.com/docs/en/api/beta#beta_base64_pdf_source) { data, media\_type, type } or[BetaPlainTextSource](https://platform.claude.com/docs/en/api/beta#beta_plain_text_source) { data, media\_type, type } or[BetaContentBlockSource](https://platform.claude.com/docs/en/api/beta#beta_content_block_source) { content, type } or2 more

Accepts one of the following:

BetaBase64PDFSource = object {data, media\_type, type}

data: string

media\_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object {data, media\_type, type}

data: string

media\_type: "text/plain"

type: "text"

BetaContentBlockSource = object {content, type}

content: stringorarray of [BetaContentBlockSourceContent](https://platform.claude.com/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

UnionMember0 = string

BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](https://platform.claude.com/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

BetaTextBlockParam = object {text, type, cache\_control, citations}

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

BetaImageBlockParam = object {source, type, cache\_control}

source: [BetaBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_base64_image_source) { data, media\_type, type } or[BetaURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_url_image_source) { type, url } or[BetaFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_file_image_source) { file\_id, type }

Accepts one of the following:

BetaBase64ImageSource = object {data, media\_type, type}

data: string

media\_type: "image/jpeg"or"image/png"or"image/gif"or"image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object {type, url}

type: "url"

url: string

BetaFileImageSource = object {file\_id, type}

file\_id: string

type: "file"

type: "image"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

BetaURLPDFSource = object {type, url}

type: "url"

url: string

BetaFileDocumentSource = object {file\_id, type}

file\_id: string

type: "file"

type: "document"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](https://platform.claude.com/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

context: optional string

title: optional string

BetaToolReferenceBlockParam = object {tool\_name, type, cache\_control}

Tool reference block that can be included in tool\_result content.

tool\_name: string

type: "tool\_reference"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

is\_error: optional boolean

BetaToolSearchToolBm25\_20251119 = object {name, type, allowed\_callers, 3 more}

name: "tool\_search\_tool\_bm25"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "tool\_search\_tool\_bm25\_20251119"or"tool\_search\_tool\_bm25"

Accepts one of the following:

"tool\_search\_tool\_bm25\_20251119"

"tool\_search\_tool\_bm25"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolSearchToolRegex20251119 = object {name, type, allowed\_callers, 3 more}

name: "tool\_search\_tool\_regex"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "tool\_search\_tool\_regex\_20251119"or"tool\_search\_tool\_regex"

Accepts one of the following:

"tool\_search\_tool\_regex\_20251119"

"tool\_search\_tool\_regex"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolSearchToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaToolSearchToolResultError](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_result_error) { error\_code, error\_message, type } or[BetaToolSearchToolSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool\_references, type }

Accepts one of the following:

BetaToolSearchToolResultError = object {error\_code, error\_message, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or"execution\_time\_exceeded"

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

BetaToolSearchToolSearchResultBlock = object {tool\_references, type}

tool\_references: array of [BetaToolReferenceBlock](https://platform.claude.com/docs/en/api/beta#beta_tool_reference_block) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

BetaToolSearchToolResultBlockParam = object {content, tool\_use\_id, type, cache\_control}

content: [BetaToolSearchToolResultErrorParam](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_result_error_param) { error\_code, type } or[BetaToolSearchToolSearchResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_search_result_block_param) { tool\_references, type }

Accepts one of the following:

BetaToolSearchToolResultErrorParam = object {error\_code, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or"execution\_time\_exceeded"

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "tool\_search\_tool\_result\_error"

BetaToolSearchToolSearchResultBlockParam = object {tool\_references, type}

tool\_references: array of [BetaToolReferenceBlockParam](https://platform.claude.com/docs/en/api/beta#beta_tool_reference_block_param) { tool\_name, type, cache\_control }

tool\_name: string

type: "tool\_reference"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaToolSearchToolResultError = object {error\_code, error\_message, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or"execution\_time\_exceeded"

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

BetaToolSearchToolResultErrorParam = object {error\_code, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or"execution\_time\_exceeded"

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "tool\_search\_tool\_result\_error"

BetaToolSearchToolSearchResultBlock = object {tool\_references, type}

tool\_references: array of [BetaToolReferenceBlock](https://platform.claude.com/docs/en/api/beta#beta_tool_reference_block) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

BetaToolSearchToolSearchResultBlockParam = object {tool\_references, type}

tool\_references: array of [BetaToolReferenceBlockParam](https://platform.claude.com/docs/en/api/beta#beta_tool_reference_block_param) { tool\_name, type, cache\_control }

tool\_name: string

type: "tool\_reference"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "tool\_search\_tool\_search\_result"

BetaToolTextEditor20241022 = object {name, type, allowed\_callers, 4 more}

name: "str\_replace\_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20241022"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolTextEditor20250124 = object {name, type, allowed\_callers, 4 more}

name: "str\_replace\_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250124"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolTextEditor20250429 = object {name, type, allowed\_callers, 4 more}

name: "str\_replace\_based\_edit\_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250429"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolTextEditor20250728 = object {name, type, allowed\_callers, 5 more}

name: "str\_replace\_based\_edit\_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250728"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map\[unknown\]

max\_characters: optional number

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolUnion = [BetaTool](https://platform.claude.com/docs/en/api/beta#beta_tool) { input\_schema, name, allowed\_callers, 7 more } or[BetaToolBash20241022](https://platform.claude.com/docs/en/api/beta#beta_tool_bash_20241022) { name, type, allowed\_callers, 4 more } or[BetaToolBash20250124](https://platform.claude.com/docs/en/api/beta#beta_tool_bash_20250124) { name, type, allowed\_callers, 4 more } or18 more

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

Accepts one of the following:

BetaTool = object {input\_schema, name, allowed\_callers, 7 more}

input\_schema: object {type, properties, required}

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: "object"

properties: optional map\[unknown\]

required: optional array of string

name: string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

description: optional string

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager\_input\_streaming: optional boolean

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

input\_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

type: optional "custom"

BetaToolBash20241022 = object {name, type, allowed\_callers, 4 more}

name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "bash\_20241022"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolBash20250124 = object {name, type, allowed\_callers, 4 more}

name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "bash\_20250124"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaCodeExecutionTool20250522 = object {name, type, allowed\_callers, 3 more}

name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20250522"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaCodeExecutionTool20250825 = object {name, type, allowed\_callers, 3 more}

name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20250825"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaCodeExecutionTool20260120 = object {name, type, allowed\_callers, 3 more}

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20260120"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolComputerUse20241022 = object {display\_height\_px, display\_width\_px, name, 7 more}

display\_height\_px: number

The height of the display in pixels.

display\_width\_px: number

The width of the display in pixels.

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer\_20241022"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: optional number

The X11 display number (e.g. 0, 1) for the display.

input\_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaMemoryTool20250818 = object {name, type, allowed\_callers, 4 more}

name: "memory"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "memory\_20250818"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolComputerUse20250124 = object {display\_height\_px, display\_width\_px, name, 7 more}

display\_height\_px: number

The height of the display in pixels.

display\_width\_px: number

The width of the display in pixels.

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer\_20250124"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: optional number

The X11 display number (e.g. 0, 1) for the display.

input\_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolTextEditor20241022 = object {name, type, allowed\_callers, 4 more}

name: "str\_replace\_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20241022"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolComputerUse20251124 = object {display\_height\_px, display\_width\_px, name, 8 more}

display\_height\_px: number

The height of the display in pixels.

display\_width\_px: number

The width of the display in pixels.

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer\_20251124"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: optional number

The X11 display number (e.g. 0, 1) for the display.

enable\_zoom: optional boolean

Whether to enable an action to take a zoomed-in screenshot of the screen.

input\_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolTextEditor20250124 = object {name, type, allowed\_callers, 4 more}

name: "str\_replace\_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250124"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolTextEditor20250429 = object {name, type, allowed\_callers, 4 more}

name: "str\_replace\_based\_edit\_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250429"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolTextEditor20250728 = object {name, type, allowed\_callers, 5 more}

name: "str\_replace\_based\_edit\_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250728"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map\[unknown\]

max\_characters: optional number

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaWebSearchTool20250305 = object {name, type, allowed\_callers, 7 more}

name: "web\_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_search\_20250305"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: optional array of string

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

user\_location: optional [BetaUserLocation](https://platform.claude.com/docs/en/api/beta#beta_user_location) { type, city, country, 2 more }

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city: optional string

The city of the user.

country: optional string

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: optional string

The region of the user.

timezone: optional string

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

BetaWebFetchTool20250910 = object {name, type, allowed\_callers, 8 more}

name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20250910"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

List of domains to allow fetching from

blocked\_domains: optional array of string

List of domains to block fetching from

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](https://platform.claude.com/docs/en/api/beta#beta_citations_config_param) { enabled }

Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: optional number

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaWebSearchTool20260209 = object {name, type, allowed\_callers, 7 more}

name: "web\_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_search\_20260209"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: optional array of string

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

user\_location: optional [BetaUserLocation](https://platform.claude.com/docs/en/api/beta#beta_user_location) { type, city, country, 2 more }

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city: optional string

The city of the user.

country: optional string

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: optional string

The region of the user.

timezone: optional string

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

BetaWebFetchTool20260209 = object {name, type, allowed\_callers, 8 more}

name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20260209"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

List of domains to allow fetching from

blocked\_domains: optional array of string

List of domains to block fetching from

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](https://platform.claude.com/docs/en/api/beta#beta_citations_config_param) { enabled }

Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: optional number

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolSearchToolBm25\_20251119 = object {name, type, allowed\_callers, 3 more}

name: "tool\_search\_tool\_bm25"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "tool\_search\_tool\_bm25\_20251119"or"tool\_search\_tool\_bm25"

Accepts one of the following:

"tool\_search\_tool\_bm25\_20251119"

"tool\_search\_tool\_bm25"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolSearchToolRegex20251119 = object {name, type, allowed\_callers, 3 more}

name: "tool\_search\_tool\_regex"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "tool\_search\_tool\_regex\_20251119"or"tool\_search\_tool\_regex"

Accepts one of the following:

"tool\_search\_tool\_regex\_20251119"

"tool\_search\_tool\_regex"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaMCPToolset = object {mcp\_server\_name, type, cache\_control, 2 more}

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

mcp\_server\_name: string

Name of the MCP server to configure tools for

type: "mcp\_toolset"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

configs: optional map\[[BetaMCPToolConfig](https://platform.claude.com/docs/en/api/beta#beta_mcp_tool_config) { defer\_loading, enabled } \]

Configuration overrides for specific tools, keyed by tool name

defer\_loading: optional boolean

enabled: optional boolean

default\_config: optional [BetaMCPToolDefaultConfig](https://platform.claude.com/docs/en/api/beta#beta_mcp_tool_default_config) { defer\_loading, enabled }

Default configuration applied to all tools from this server

defer\_loading: optional boolean

enabled: optional boolean

BetaToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: string

type: "tool\_use"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaToolUseBlockParam = object {id, input, name, 3 more}

id: string

input: map\[unknown\]

name: string

type: "tool\_use"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaToolUsesKeep = object {type, value}

type: "tool\_uses"

value: number

BetaToolUsesTrigger = object {type, value}

type: "tool\_uses"

value: number

BetaURLImageSource = object {type, url}

type: "url"

url: string

BetaURLPDFSource = object {type, url}

type: "url"

url: string

BetaUsage = object {cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 7 more}

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

inference\_geo: string

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.

iterations: [BetaIterationsUsage](https://platform.claude.com/docs/en/api/beta#beta_iterations_usage) { ,  }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage = object {cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more}

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

BetaCompactionIterationUsage = object {cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more}

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output\_tokens: number

The number of output tokens which were used.

server\_tool\_use: [BetaServerToolUsage](https://platform.claude.com/docs/en/api/beta#beta_server_tool_usage) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

service\_tier: "standard"or"priority"or"batch"

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

speed: "standard"or"fast"

The inference speed mode used for this request.

Accepts one of the following:

"standard"

"fast"

BetaUserLocation = object {type, city, country, 2 more}

type: "approximate"

city: optional string

The city of the user.

country: optional string

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: optional string

The region of the user.

timezone: optional string

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

BetaWebFetchBlock = object {content, retrieved\_at, type, url}

content: [BetaDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](https://platform.claude.com/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](https://platform.claude.com/docs/en/api/beta#beta_base64_pdf_source) { data, media\_type, type } or[BetaPlainTextSource](https://platform.claude.com/docs/en/api/beta#beta_plain_text_source) { data, media\_type, type }

Accepts one of the following:

BetaBase64PDFSource = object {data, media\_type, type}

data: string

media\_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object {data, media\_type, type}

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

BetaWebFetchBlockParam = object {content, type, url, retrieved\_at}

content: [BetaRequestDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_request_document_block) { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](https://platform.claude.com/docs/en/api/beta#beta_base64_pdf_source) { data, media\_type, type } or[BetaPlainTextSource](https://platform.claude.com/docs/en/api/beta#beta_plain_text_source) { data, media\_type, type } or[BetaContentBlockSource](https://platform.claude.com/docs/en/api/beta#beta_content_block_source) { content, type } or2 more

Accepts one of the following:

BetaBase64PDFSource = object {data, media\_type, type}

data: string

media\_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object {data, media\_type, type}

data: string

media\_type: "text/plain"

type: "text"

BetaContentBlockSource = object {content, type}

content: stringorarray of [BetaContentBlockSourceContent](https://platform.claude.com/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

UnionMember0 = string

BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](https://platform.claude.com/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

BetaTextBlockParam = object {text, type, cache\_control, citations}

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

BetaImageBlockParam = object {source, type, cache\_control}

source: [BetaBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_base64_image_source) { data, media\_type, type } or[BetaURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_url_image_source) { type, url } or[BetaFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_file_image_source) { file\_id, type }

Accepts one of the following:

BetaBase64ImageSource = object {data, media\_type, type}

data: string

media\_type: "image/jpeg"or"image/png"or"image/gif"or"image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object {type, url}

type: "url"

url: string

BetaFileImageSource = object {file\_id, type}

file\_id: string

type: "file"

type: "image"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

BetaURLPDFSource = object {type, url}

type: "url"

url: string

BetaFileDocumentSource = object {file\_id, type}

file\_id: string

type: "file"

type: "document"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](https://platform.claude.com/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

context: optional string

title: optional string

type: "web\_fetch\_result"

url: string

Fetched content URL

retrieved\_at: optional string

ISO 8601 timestamp when the content was retrieved

BetaWebFetchTool20250910 = object {name, type, allowed\_callers, 8 more}

name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20250910"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

List of domains to allow fetching from

blocked\_domains: optional array of string

List of domains to block fetching from

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](https://platform.claude.com/docs/en/api/beta#beta_citations_config_param) { enabled }

Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: optional number

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaWebFetchTool20260209 = object {name, type, allowed\_callers, 8 more}

name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20260209"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

List of domains to allow fetching from

blocked\_domains: optional array of string

List of domains to block fetching from

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](https://platform.claude.com/docs/en/api/beta#beta_citations_config_param) { enabled }

Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: optional number

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaWebFetchToolResultBlock = object {content, tool\_use\_id, type, caller}

content: [BetaWebFetchToolResultErrorBlock](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error\_code, type } or[BetaWebFetchBlock](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_block) { content, retrieved\_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock = object {error\_code, type}

error\_code: [BetaWebFetchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

BetaWebFetchBlock = object {content, retrieved\_at, type, url}

content: [BetaDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](https://platform.claude.com/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](https://platform.claude.com/docs/en/api/beta#beta_base64_pdf_source) { data, media\_type, type } or[BetaPlainTextSource](https://platform.claude.com/docs/en/api/beta#beta_plain_text_source) { data, media\_type, type }

Accepts one of the following:

BetaBase64PDFSource = object {data, media\_type, type}

data: string

media\_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object {data, media\_type, type}

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaWebFetchToolResultBlockParam = object {content, tool\_use\_id, type, 2 more}

content: [BetaWebFetchToolResultErrorBlockParam](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_block_param) { error\_code, type } or[BetaWebFetchBlockParam](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_block_param) { content, type, url, retrieved\_at }

Accepts one of the following:

BetaWebFetchToolResultErrorBlockParam = object {error\_code, type}

error\_code: [BetaWebFetchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

BetaWebFetchBlockParam = object {content, type, url, retrieved\_at}

content: [BetaRequestDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_request_document_block) { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](https://platform.claude.com/docs/en/api/beta#beta_base64_pdf_source) { data, media\_type, type } or[BetaPlainTextSource](https://platform.claude.com/docs/en/api/beta#beta_plain_text_source) { data, media\_type, type } or[BetaContentBlockSource](https://platform.claude.com/docs/en/api/beta#beta_content_block_source) { content, type } or2 more

Accepts one of the following:

BetaBase64PDFSource = object {data, media\_type, type}

data: string

media\_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object {data, media\_type, type}

data: string

media\_type: "text/plain"

type: "text"

BetaContentBlockSource = object {content, type}

content: stringorarray of [BetaContentBlockSourceContent](https://platform.claude.com/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

UnionMember0 = string

BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](https://platform.claude.com/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

BetaTextBlockParam = object {text, type, cache\_control, citations}

text: string

type: "text"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocationParam = object {cited\_text, document\_index, document\_title, 3 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

BetaCitationWebSearchResultLocationParam = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocationParam = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

BetaImageBlockParam = object {source, type, cache\_control}

source: [BetaBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_base64_image_source) { data, media\_type, type } or[BetaURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_url_image_source) { type, url } or[BetaFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_file_image_source) { file\_id, type }

Accepts one of the following:

BetaBase64ImageSource = object {data, media\_type, type}

data: string

media\_type: "image/jpeg"or"image/png"or"image/gif"or"image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object {type, url}

type: "url"

url: string

BetaFileImageSource = object {file\_id, type}

file\_id: string

type: "file"

type: "image"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

BetaURLPDFSource = object {type, url}

type: "url"

url: string

BetaFileDocumentSource = object {file\_id, type}

file\_id: string

type: "file"

type: "document"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](https://platform.claude.com/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

context: optional string

title: optional string

type: "web\_fetch\_result"

url: string

Fetched content URL

retrieved\_at: optional string

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaWebFetchToolResultErrorBlock = object {error\_code, type}

error\_code: [BetaWebFetchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

BetaWebFetchToolResultErrorBlockParam = object {error\_code, type}

error\_code: [BetaWebFetchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

BetaWebFetchToolResultErrorCode = "invalid\_tool\_input"or"url\_too\_long"or"url\_not\_allowed"or5 more

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

BetaWebSearchResultBlock = object {encrypted\_content, page\_age, title, 2 more}

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

BetaWebSearchResultBlockParam = object {encrypted\_content, title, type, 2 more}

encrypted\_content: string

title: string

type: "web\_search\_result"

url: string

page\_age: optional string

BetaWebSearchTool20250305 = object {name, type, allowed\_callers, 7 more}

name: "web\_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_search\_20250305"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: optional array of string

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

user\_location: optional [BetaUserLocation](https://platform.claude.com/docs/en/api/beta#beta_user_location) { type, city, country, 2 more }

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city: optional string

The city of the user.

country: optional string

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: optional string

The region of the user.

timezone: optional string

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

BetaWebSearchTool20260209 = object {name, type, allowed\_callers, 7 more}

name: "web\_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_search\_20260209"

allowed\_callers: optional array of "direct"or"code\_execution\_20250825"or"code\_execution\_20260120"

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: optional array of string

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

user\_location: optional [BetaUserLocation](https://platform.claude.com/docs/en/api/beta#beta_user_location) { type, city, country, 2 more }

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city: optional string

The city of the user.

country: optional string

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: optional string

The region of the user.

timezone: optional string

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

BetaWebSearchToolRequestError = object {error\_code, type}

error\_code: [BetaWebSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

BetaWebSearchToolResultBlock = object {content, tool\_use\_id, type, caller}

content: [BetaWebSearchToolResultBlockContent](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError = object {error\_code, type}

error\_code: [BetaWebSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

UnionMember1 = array of [BetaWebSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_web_search_result_block) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaWebSearchToolResultBlockContent = [BetaWebSearchToolResultError](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_error) { error\_code, type } orarray of [BetaWebSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_web_search_result_block) { encrypted\_content, page\_age, title, 2 more }

Accepts one of the following:

BetaWebSearchToolResultError = object {error\_code, type}

error\_code: [BetaWebSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

UnionMember1 = array of [BetaWebSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_web_search_result_block) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

BetaWebSearchToolResultBlockParam = object {content, tool\_use\_id, type, 2 more}

content: [BetaWebSearchToolResultBlockParamContent](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_block_param_content)

Accepts one of the following:

ResultBlock = array of [BetaWebSearchResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_web_search_result_block_param) { encrypted\_content, title, type, 2 more }

encrypted\_content: string

title: string

type: "web\_search\_result"

url: string

page\_age: optional string

BetaWebSearchToolRequestError = object {error\_code, type}

error\_code: [BetaWebSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

tool\_use\_id: string

type: "web\_search\_tool\_result"

cache\_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m"or"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaWebSearchToolResultBlockParamContent = array of [BetaWebSearchResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_web_search_result_block_param) { encrypted\_content, title, type, 2 more } or[BetaWebSearchToolRequestError](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_request_error) { error\_code, type }

Accepts one of the following:

ResultBlock = array of [BetaWebSearchResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_web_search_result_block_param) { encrypted\_content, title, type, 2 more }

encrypted\_content: string

title: string

type: "web\_search\_result"

url: string

page\_age: optional string

BetaWebSearchToolRequestError = object {error\_code, type}

error\_code: [BetaWebSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

BetaWebSearchToolResultError = object {error\_code, type}

error\_code: [BetaWebSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

BetaWebSearchToolResultErrorCode = "invalid\_tool\_input"or"unavailable"or"max\_uses\_exceeded"or3 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

#### BetaMessagesBatches

##### [Create a Message Batch](https://platform.claude.com/docs/en/api/beta/messages/batches/create)

POST/v1/messages/batches

##### [Retrieve a Message Batch](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve)

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](https://platform.claude.com/docs/en/api/beta/messages/batches/list)

GET/v1/messages/batches

##### [Cancel a Message Batch](https://platform.claude.com/docs/en/api/beta/messages/batches/cancel)

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](https://platform.claude.com/docs/en/api/beta/messages/batches/delete)

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](https://platform.claude.com/docs/en/api/beta/messages/batches/results)

GET/v1/messages/batches/{message\_batch\_id}/results

##### ModelsExpand Collapse

BetaDeletedMessageBatch = object {id, type}

id: string

ID of the Message Batch.

type: "message\_batch\_deleted"

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

BetaMessageBatch = object {id, archived\_at, cancel\_initiated\_at, 7 more}

id: string

Unique object identifier.

The format and length of IDs may change over time.

archived\_at: string

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

cancel\_initiated\_at: string

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

created\_at: string

RFC 3339 datetime string representing the time at which the Message Batch was created.

ended\_at: string

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

expires\_at: string

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

processing\_status: "in\_progress"or"canceling"or"ended"

Processing status of the Message Batch.

Accepts one of the following:

"in\_progress"

"canceling"

"ended"

request\_counts: [BetaMessageBatchRequestCounts](https://platform.claude.com/docs/en/api/beta#beta_message_batch_request_counts) { canceled, errored, expired, 2 more }

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

canceled: number

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: number

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: number

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: number

Number of requests in the Message Batch that are processing.

succeeded: number

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

results\_url: string

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

type: "message\_batch"

Object type.

For Message Batches, this is always `"message_batch"`.

BetaMessageBatchCanceledResult = object {type}

type: "canceled"

BetaMessageBatchErroredResult = object {error, type}

error: [BetaErrorResponse](https://platform.claude.com/docs/en/api/beta#beta_error_response) { error, request\_id, type }

error: [BetaError](https://platform.claude.com/docs/en/api/beta#beta_error)

Accepts one of the following:

BetaInvalidRequestError = object {message, type}

message: string

type: "invalid\_request\_error"

BetaAuthenticationError = object {message, type}

message: string

type: "authentication\_error"

BetaBillingError = object {message, type}

message: string

type: "billing\_error"

BetaPermissionError = object {message, type}

message: string

type: "permission\_error"

BetaNotFoundError = object {message, type}

message: string

type: "not\_found\_error"

BetaRateLimitError = object {message, type}

message: string

type: "rate\_limit\_error"

BetaGatewayTimeoutError = object {message, type}

message: string

type: "timeout\_error"

BetaAPIError = object {message, type}

message: string

type: "api\_error"

BetaOverloadedError = object {message, type}

message: string

type: "overloaded\_error"

request\_id: string

type: "error"

type: "errored"

BetaMessageBatchExpiredResult = object {type}

type: "expired"

BetaMessageBatchIndividualResponse = object {custom\_id, result}

This is a single line in the response `.jsonl` file and does not represent the response as a whole.

custom\_id: string

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

result: [BetaMessageBatchResult](https://platform.claude.com/docs/en/api/beta#beta_message_batch_result)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

BetaMessageBatchSucceededResult = object {message, type}

message: [BetaMessage](https://platform.claude.com/docs/en/api/beta#beta_message) { id, container, content, 7 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](https://platform.claude.com/docs/en/api/beta#beta_container) { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

skills: array of [BetaSkill](https://platform.claude.com/docs/en/api/beta#beta_skill) { skill\_id, type, version }

Skills loaded in the container

skill\_id: string

Skill ID

type: "anthropic"or"custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

content: array of [BetaContentBlock](https://platform.claude.com/docs/en/api/beta#beta_content_block)

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```
[{"type": "text", "text": "Hi, I'm Claude."}]
```

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```
[\
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},\
  {"role": "assistant", "content": "The best answer is ("}\
]
```

Then the response `content` might be:

```
[{"type": "text", "text": "B)"}]
```

Accepts one of the following:

BetaTextBlock = object {citations, text, type}

citations: array of [BetaTextCitation](https://platform.claude.com/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

BetaThinkingBlock = object {signature, thinking, type}

signature: string

thinking: string

type: "thinking"

BetaRedactedThinkingBlock = object {data, type}

data: string

type: "redacted\_thinking"

BetaToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: string

type: "tool\_use"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaServerToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: "web\_search"or"web\_fetch"or"code\_execution"or4 more

Accepts one of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaWebSearchToolResultBlock = object {content, tool\_use\_id, type, caller}

content: [BetaWebSearchToolResultBlockContent](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError = object {error\_code, type}

error\_code: [BetaWebSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

UnionMember1 = array of [BetaWebSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_web_search_result_block) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaWebFetchToolResultBlock = object {content, tool\_use\_id, type, caller}

content: [BetaWebFetchToolResultErrorBlock](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error\_code, type } or[BetaWebFetchBlock](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_block) { content, retrieved\_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock = object {error\_code, type}

error\_code: [BetaWebFetchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

BetaWebFetchBlock = object {content, retrieved\_at, type, url}

content: [BetaDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](https://platform.claude.com/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](https://platform.claude.com/docs/en/api/beta#beta_base64_pdf_source) { data, media\_type, type } or[BetaPlainTextSource](https://platform.claude.com/docs/en/api/beta#beta_plain_text_source) { data, media\_type, type }

Accepts one of the following:

BetaBase64PDFSource = object {data, media\_type, type}

data: string

media\_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object {data, media\_type, type}

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaCodeExecutionToolResultBlockContent](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

BetaCodeExecutionToolResultError = object {error\_code, type}

error\_code: [BetaCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

BetaCodeExecutionResultBlock = object {content, return\_code, stderr, 2 more}

content: array of [BetaCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

BetaEncryptedCodeExecutionResultBlock = object {content, encrypted\_stdout, return\_code, 2 more}

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

BetaBashCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaBashCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error\_code, type } or[BetaBashCodeExecutionResultBlock](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return\_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError = object {error\_code, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

BetaBashCodeExecutionResultBlock = object {content, return\_code, stderr, 2 more}

content: array of [BetaBashCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_output_block) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

BetaTextEditorCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaTextEditorCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error\_code, error\_message, type } or[BetaTextEditorCodeExecutionViewResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file\_type, num\_lines, 3 more } or[BetaTextEditorCodeExecutionCreateResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is\_file\_update, type } or[BetaTextEditorCodeExecutionStrReplaceResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new\_lines, new\_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError = object {error\_code, error\_message, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

BetaTextEditorCodeExecutionViewResultBlock = object {content, file\_type, num\_lines, 3 more}

content: string

file\_type: "text"or"image"or"pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

BetaTextEditorCodeExecutionCreateResultBlock = object {is\_file\_update, type}

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock = object {lines, new\_lines, new\_start, 3 more}

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

BetaToolSearchToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaToolSearchToolResultError](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_result_error) { error\_code, error\_message, type } or[BetaToolSearchToolSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool\_references, type }

Accepts one of the following:

BetaToolSearchToolResultError = object {error\_code, error\_message, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or"execution\_time\_exceeded"

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

BetaToolSearchToolSearchResultBlock = object {tool\_references, type}

tool\_references: array of [BetaToolReferenceBlock](https://platform.claude.com/docs/en/api/beta#beta_tool_reference_block) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

BetaMCPToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

BetaMCPToolResultBlock = object {content, is\_error, tool\_use\_id, type}

content: stringorarray of [BetaTextBlock](https://platform.claude.com/docs/en/api/beta#beta_text_block) { citations, text, type }

Accepts one of the following:

UnionMember0 = string

BetaMCPToolResultBlockContent = array of [BetaTextBlock](https://platform.claude.com/docs/en/api/beta#beta_text_block) { citations, text, type }

citations: array of [BetaTextCitation](https://platform.claude.com/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"

BetaContainerUploadBlock = object {file\_id, type}

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

BetaCompactionBlock = object {content, type}

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

context\_management: [BetaContextManagementResponse](https://platform.claude.com/docs/en/api/beta#beta_context_management_response) { applied\_edits }

Context management response.

Information about context management strategies applied during the request.

applied\_edits: array of [BetaClearToolUses20250919EditResponse](https://platform.claude.com/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared\_input\_tokens, cleared\_tool\_uses, type } or[BetaClearThinking20251015EditResponse](https://platform.claude.com/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared\_input\_tokens, cleared\_thinking\_turns, type }

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse = object {cleared\_input\_tokens, cleared\_tool\_uses, type}

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

BetaClearThinking20251015EditResponse = object {cleared\_input\_tokens, cleared\_thinking\_turns, type}

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.

model: [Model](https://platform.claude.com/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = "claude-opus-4-6"or"claude-sonnet-4-6"or"claude-haiku-4-5"or12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

"claude-opus-4-0"

Powerful model for complex tasks

"claude-opus-4-20250514"

Powerful model for complex tasks

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-3-haiku-20240307"

Fast and cost-effective model

UnionMember1 = string

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_reason: [BetaStopReason](https://platform.claude.com/docs/en/api/beta#beta_stop_reason)

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

Accepts one of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: [BetaUsage](https://platform.claude.com/docs/en/api/beta#beta_usage) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

inference\_geo: string

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.

iterations: [BetaIterationsUsage](https://platform.claude.com/docs/en/api/beta#beta_iterations_usage) { ,  }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage = object {cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more}

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

BetaCompactionIterationUsage = object {cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more}

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output\_tokens: number

The number of output tokens which were used.

server\_tool\_use: [BetaServerToolUsage](https://platform.claude.com/docs/en/api/beta#beta_server_tool_usage) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

service\_tier: "standard"or"priority"or"batch"

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

speed: "standard"or"fast"

The inference speed mode used for this request.

Accepts one of the following:

"standard"

"fast"

type: "succeeded"

BetaMessageBatchErroredResult = object {error, type}

error: [BetaErrorResponse](https://platform.claude.com/docs/en/api/beta#beta_error_response) { error, request\_id, type }

error: [BetaError](https://platform.claude.com/docs/en/api/beta#beta_error)

Accepts one of the following:

BetaInvalidRequestError = object {message, type}

message: string

type: "invalid\_request\_error"

BetaAuthenticationError = object {message, type}

message: string

type: "authentication\_error"

BetaBillingError = object {message, type}

message: string

type: "billing\_error"

BetaPermissionError = object {message, type}

message: string

type: "permission\_error"

BetaNotFoundError = object {message, type}

message: string

type: "not\_found\_error"

BetaRateLimitError = object {message, type}

message: string

type: "rate\_limit\_error"

BetaGatewayTimeoutError = object {message, type}

message: string

type: "timeout\_error"

BetaAPIError = object {message, type}

message: string

type: "api\_error"

BetaOverloadedError = object {message, type}

message: string

type: "overloaded\_error"

request\_id: string

type: "error"

type: "errored"

BetaMessageBatchCanceledResult = object {type}

type: "canceled"

BetaMessageBatchExpiredResult = object {type}

type: "expired"

BetaMessageBatchRequestCounts = object {canceled, errored, expired, 2 more}

canceled: number

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: number

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: number

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: number

Number of requests in the Message Batch that are processing.

succeeded: number

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

BetaMessageBatchResult = [BetaMessageBatchSucceededResult](https://platform.claude.com/docs/en/api/beta#beta_message_batch_succeeded_result) { message, type } or[BetaMessageBatchErroredResult](https://platform.claude.com/docs/en/api/beta#beta_message_batch_errored_result) { error, type } or[BetaMessageBatchCanceledResult](https://platform.claude.com/docs/en/api/beta#beta_message_batch_canceled_result) { type } or[BetaMessageBatchExpiredResult](https://platform.claude.com/docs/en/api/beta#beta_message_batch_expired_result) { type }

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

BetaMessageBatchSucceededResult = object {message, type}

message: [BetaMessage](https://platform.claude.com/docs/en/api/beta#beta_message) { id, container, content, 7 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](https://platform.claude.com/docs/en/api/beta#beta_container) { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

skills: array of [BetaSkill](https://platform.claude.com/docs/en/api/beta#beta_skill) { skill\_id, type, version }

Skills loaded in the container

skill\_id: string

Skill ID

type: "anthropic"or"custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

content: array of [BetaContentBlock](https://platform.claude.com/docs/en/api/beta#beta_content_block)

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```
[{"type": "text", "text": "Hi, I'm Claude."}]
```

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```
[\
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},\
  {"role": "assistant", "content": "The best answer is ("}\
]
```

Then the response `content` might be:

```
[{"type": "text", "text": "B)"}]
```

Accepts one of the following:

BetaTextBlock = object {citations, text, type}

citations: array of [BetaTextCitation](https://platform.claude.com/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

BetaThinkingBlock = object {signature, thinking, type}

signature: string

thinking: string

type: "thinking"

BetaRedactedThinkingBlock = object {data, type}

data: string

type: "redacted\_thinking"

BetaToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: string

type: "tool\_use"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaServerToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: "web\_search"or"web\_fetch"or"code\_execution"or4 more

Accepts one of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaWebSearchToolResultBlock = object {content, tool\_use\_id, type, caller}

content: [BetaWebSearchToolResultBlockContent](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError = object {error\_code, type}

error\_code: [BetaWebSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

UnionMember1 = array of [BetaWebSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_web_search_result_block) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaWebFetchToolResultBlock = object {content, tool\_use\_id, type, caller}

content: [BetaWebFetchToolResultErrorBlock](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error\_code, type } or[BetaWebFetchBlock](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_block) { content, retrieved\_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock = object {error\_code, type}

error\_code: [BetaWebFetchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

BetaWebFetchBlock = object {content, retrieved\_at, type, url}

content: [BetaDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](https://platform.claude.com/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](https://platform.claude.com/docs/en/api/beta#beta_base64_pdf_source) { data, media\_type, type } or[BetaPlainTextSource](https://platform.claude.com/docs/en/api/beta#beta_plain_text_source) { data, media\_type, type }

Accepts one of the following:

BetaBase64PDFSource = object {data, media\_type, type}

data: string

media\_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object {data, media\_type, type}

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaCodeExecutionToolResultBlockContent](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

BetaCodeExecutionToolResultError = object {error\_code, type}

error\_code: [BetaCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

BetaCodeExecutionResultBlock = object {content, return\_code, stderr, 2 more}

content: array of [BetaCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

BetaEncryptedCodeExecutionResultBlock = object {content, encrypted\_stdout, return\_code, 2 more}

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

BetaBashCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaBashCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error\_code, type } or[BetaBashCodeExecutionResultBlock](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return\_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError = object {error\_code, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

BetaBashCodeExecutionResultBlock = object {content, return\_code, stderr, 2 more}

content: array of [BetaBashCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_output_block) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

BetaTextEditorCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaTextEditorCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error\_code, error\_message, type } or[BetaTextEditorCodeExecutionViewResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file\_type, num\_lines, 3 more } or[BetaTextEditorCodeExecutionCreateResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is\_file\_update, type } or[BetaTextEditorCodeExecutionStrReplaceResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new\_lines, new\_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError = object {error\_code, error\_message, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

BetaTextEditorCodeExecutionViewResultBlock = object {content, file\_type, num\_lines, 3 more}

content: string

file\_type: "text"or"image"or"pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

BetaTextEditorCodeExecutionCreateResultBlock = object {is\_file\_update, type}

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock = object {lines, new\_lines, new\_start, 3 more}

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

BetaToolSearchToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaToolSearchToolResultError](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_result_error) { error\_code, error\_message, type } or[BetaToolSearchToolSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool\_references, type }

Accepts one of the following:

BetaToolSearchToolResultError = object {error\_code, error\_message, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or"execution\_time\_exceeded"

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

BetaToolSearchToolSearchResultBlock = object {tool\_references, type}

tool\_references: array of [BetaToolReferenceBlock](https://platform.claude.com/docs/en/api/beta#beta_tool_reference_block) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

BetaMCPToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

BetaMCPToolResultBlock = object {content, is\_error, tool\_use\_id, type}

content: stringorarray of [BetaTextBlock](https://platform.claude.com/docs/en/api/beta#beta_text_block) { citations, text, type }

Accepts one of the following:

UnionMember0 = string

BetaMCPToolResultBlockContent = array of [BetaTextBlock](https://platform.claude.com/docs/en/api/beta#beta_text_block) { citations, text, type }

citations: array of [BetaTextCitation](https://platform.claude.com/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"

BetaContainerUploadBlock = object {file\_id, type}

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

BetaCompactionBlock = object {content, type}

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

context\_management: [BetaContextManagementResponse](https://platform.claude.com/docs/en/api/beta#beta_context_management_response) { applied\_edits }

Context management response.

Information about context management strategies applied during the request.

applied\_edits: array of [BetaClearToolUses20250919EditResponse](https://platform.claude.com/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared\_input\_tokens, cleared\_tool\_uses, type } or[BetaClearThinking20251015EditResponse](https://platform.claude.com/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared\_input\_tokens, cleared\_thinking\_turns, type }

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse = object {cleared\_input\_tokens, cleared\_tool\_uses, type}

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

BetaClearThinking20251015EditResponse = object {cleared\_input\_tokens, cleared\_thinking\_turns, type}

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.

model: [Model](https://platform.claude.com/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = "claude-opus-4-6"or"claude-sonnet-4-6"or"claude-haiku-4-5"or12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

"claude-opus-4-0"

Powerful model for complex tasks

"claude-opus-4-20250514"

Powerful model for complex tasks

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-3-haiku-20240307"

Fast and cost-effective model

UnionMember1 = string

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_reason: [BetaStopReason](https://platform.claude.com/docs/en/api/beta#beta_stop_reason)

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

Accepts one of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: [BetaUsage](https://platform.claude.com/docs/en/api/beta#beta_usage) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

inference\_geo: string

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.

iterations: [BetaIterationsUsage](https://platform.claude.com/docs/en/api/beta#beta_iterations_usage) { ,  }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage = object {cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more}

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

BetaCompactionIterationUsage = object {cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more}

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output\_tokens: number

The number of output tokens which were used.

server\_tool\_use: [BetaServerToolUsage](https://platform.claude.com/docs/en/api/beta#beta_server_tool_usage) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

service\_tier: "standard"or"priority"or"batch"

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

speed: "standard"or"fast"

The inference speed mode used for this request.

Accepts one of the following:

"standard"

"fast"

type: "succeeded"

BetaMessageBatchErroredResult = object {error, type}

error: [BetaErrorResponse](https://platform.claude.com/docs/en/api/beta#beta_error_response) { error, request\_id, type }

error: [BetaError](https://platform.claude.com/docs/en/api/beta#beta_error)

Accepts one of the following:

BetaInvalidRequestError = object {message, type}

message: string

type: "invalid\_request\_error"

BetaAuthenticationError = object {message, type}

message: string

type: "authentication\_error"

BetaBillingError = object {message, type}

message: string

type: "billing\_error"

BetaPermissionError = object {message, type}

message: string

type: "permission\_error"

BetaNotFoundError = object {message, type}

message: string

type: "not\_found\_error"

BetaRateLimitError = object {message, type}

message: string

type: "rate\_limit\_error"

BetaGatewayTimeoutError = object {message, type}

message: string

type: "timeout\_error"

BetaAPIError = object {message, type}

message: string

type: "api\_error"

BetaOverloadedError = object {message, type}

message: string

type: "overloaded\_error"

request\_id: string

type: "error"

type: "errored"

BetaMessageBatchCanceledResult = object {type}

type: "canceled"

BetaMessageBatchExpiredResult = object {type}

type: "expired"

BetaMessageBatchSucceededResult = object {message, type}

message: [BetaMessage](https://platform.claude.com/docs/en/api/beta#beta_message) { id, container, content, 7 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](https://platform.claude.com/docs/en/api/beta#beta_container) { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

skills: array of [BetaSkill](https://platform.claude.com/docs/en/api/beta#beta_skill) { skill\_id, type, version }

Skills loaded in the container

skill\_id: string

Skill ID

type: "anthropic"or"custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

content: array of [BetaContentBlock](https://platform.claude.com/docs/en/api/beta#beta_content_block)

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```
[{"type": "text", "text": "Hi, I'm Claude."}]
```

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```
[\
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},\
  {"role": "assistant", "content": "The best answer is ("}\
]
```

Then the response `content` might be:

```
[{"type": "text", "text": "B)"}]
```

Accepts one of the following:

BetaTextBlock = object {citations, text, type}

citations: array of [BetaTextCitation](https://platform.claude.com/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

BetaThinkingBlock = object {signature, thinking, type}

signature: string

thinking: string

type: "thinking"

BetaRedactedThinkingBlock = object {data, type}

data: string

type: "redacted\_thinking"

BetaToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: string

type: "tool\_use"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaServerToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: "web\_search"or"web\_fetch"or"code\_execution"or4 more

Accepts one of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaWebSearchToolResultBlock = object {content, tool\_use\_id, type, caller}

content: [BetaWebSearchToolResultBlockContent](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError = object {error\_code, type}

error\_code: [BetaWebSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

UnionMember1 = array of [BetaWebSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_web_search_result_block) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaWebFetchToolResultBlock = object {content, tool\_use\_id, type, caller}

content: [BetaWebFetchToolResultErrorBlock](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error\_code, type } or[BetaWebFetchBlock](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_block) { content, retrieved\_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock = object {error\_code, type}

error\_code: [BetaWebFetchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

BetaWebFetchBlock = object {content, retrieved\_at, type, url}

content: [BetaDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](https://platform.claude.com/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](https://platform.claude.com/docs/en/api/beta#beta_base64_pdf_source) { data, media\_type, type } or[BetaPlainTextSource](https://platform.claude.com/docs/en/api/beta#beta_plain_text_source) { data, media\_type, type }

Accepts one of the following:

BetaBase64PDFSource = object {data, media\_type, type}

data: string

media\_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object {data, media\_type, type}

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type } or[BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool\_id, type } or[BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object {type}

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object {tool\_id, type}

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

BetaServerToolCaller20260120 = object {tool\_id, type}

tool\_id: string

type: "code\_execution\_20260120"

BetaCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaCodeExecutionToolResultBlockContent](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

BetaCodeExecutionToolResultError = object {error\_code, type}

error\_code: [BetaCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

BetaCodeExecutionResultBlock = object {content, return\_code, stderr, 2 more}

content: array of [BetaCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

BetaEncryptedCodeExecutionResultBlock = object {content, encrypted\_stdout, return\_code, 2 more}

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

BetaBashCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaBashCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error\_code, type } or[BetaBashCodeExecutionResultBlock](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return\_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError = object {error\_code, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

BetaBashCodeExecutionResultBlock = object {content, return\_code, stderr, 2 more}

content: array of [BetaBashCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_output_block) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

BetaTextEditorCodeExecutionToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaTextEditorCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error\_code, error\_message, type } or[BetaTextEditorCodeExecutionViewResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file\_type, num\_lines, 3 more } or[BetaTextEditorCodeExecutionCreateResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is\_file\_update, type } or[BetaTextEditorCodeExecutionStrReplaceResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new\_lines, new\_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError = object {error\_code, error\_message, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or2 more

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

BetaTextEditorCodeExecutionViewResultBlock = object {content, file\_type, num\_lines, 3 more}

content: string

file\_type: "text"or"image"or"pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

BetaTextEditorCodeExecutionCreateResultBlock = object {is\_file\_update, type}

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock = object {lines, new\_lines, new\_start, 3 more}

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

BetaToolSearchToolResultBlock = object {content, tool\_use\_id, type}

content: [BetaToolSearchToolResultError](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_result_error) { error\_code, error\_message, type } or[BetaToolSearchToolSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool\_references, type }

Accepts one of the following:

BetaToolSearchToolResultError = object {error\_code, error\_message, type}

error\_code: "invalid\_tool\_input"or"unavailable"or"too\_many\_requests"or"execution\_time\_exceeded"

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

BetaToolSearchToolSearchResultBlock = object {tool\_references, type}

tool\_references: array of [BetaToolReferenceBlock](https://platform.claude.com/docs/en/api/beta#beta_tool_reference_block) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

BetaMCPToolUseBlock = object {id, input, name, 2 more}

id: string

input: map\[unknown\]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

BetaMCPToolResultBlock = object {content, is\_error, tool\_use\_id, type}

content: stringorarray of [BetaTextBlock](https://platform.claude.com/docs/en/api/beta#beta_text_block) { citations, text, type }

Accepts one of the following:

UnionMember0 = string

BetaMCPToolResultBlockContent = array of [BetaTextBlock](https://platform.claude.com/docs/en/api/beta#beta_text_block) { citations, text, type }

citations: array of [BetaTextCitation](https://platform.claude.com/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

BetaCitationPageLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

BetaCitationContentBlockLocation = object {cited\_text, document\_index, document\_title, 4 more}

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

BetaCitationsWebSearchResultLocation = object {cited\_text, encrypted\_index, title, 2 more}

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

BetaCitationSearchResultLocation = object {cited\_text, end\_block\_index, search\_result\_index, 4 more}

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"

BetaContainerUploadBlock = object {file\_id, type}

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

BetaCompactionBlock = object {content, type}

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

context\_management: [BetaContextManagementResponse](https://platform.claude.com/docs/en/api/beta#beta_context_management_response) { applied\_edits }

Context management response.

Information about context management strategies applied during the request.

applied\_edits: array of [BetaClearToolUses20250919EditResponse](https://platform.claude.com/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared\_input\_tokens, cleared\_tool\_uses, type } or[BetaClearThinking20251015EditResponse](https://platform.claude.com/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared\_input\_tokens, cleared\_thinking\_turns, type }

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse = object {cleared\_input\_tokens, cleared\_tool\_uses, type}

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

BetaClearThinking20251015EditResponse = object {cleared\_input\_tokens, cleared\_thinking\_turns, type}

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.

model: [Model](https://platform.claude.com/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = "claude-opus-4-6"or"claude-sonnet-4-6"or"claude-haiku-4-5"or12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

"claude-opus-4-0"

Powerful model for complex tasks

"claude-opus-4-20250514"

Powerful model for complex tasks

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-3-haiku-20240307"

Fast and cost-effective model

UnionMember1 = string

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_reason: [BetaStopReason](https://platform.claude.com/docs/en/api/beta#beta_stop_reason)

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

Accepts one of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: [BetaUsage](https://platform.claude.com/docs/en/api/beta#beta_usage) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

inference\_geo: string

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.

iterations: [BetaIterationsUsage](https://platform.claude.com/docs/en/api/beta#beta_iterations_usage) { ,  }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage = object {cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more}

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

BetaCompactionIterationUsage = object {cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more}

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output\_tokens: number

The number of output tokens which were used.

server\_tool\_use: [BetaServerToolUsage](https://platform.claude.com/docs/en/api/beta#beta_server_tool_usage) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

service\_tier: "standard"or"priority"or"batch"

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

speed: "standard"or"fast"

The inference speed mode used for this request.

Accepts one of the following:

"standard"

"fast"

type: "succeeded"

#### BetaFiles

##### [Upload File](https://platform.claude.com/docs/en/api/beta/files/upload)

POST/v1/files

##### [List Files](https://platform.claude.com/docs/en/api/beta/files/list)

GET/v1/files

##### [Download File](https://platform.claude.com/docs/en/api/beta/files/download)

GET/v1/files/{file\_id}/content

##### [Get File Metadata](https://platform.claude.com/docs/en/api/beta/files/retrieve_metadata)

GET/v1/files/{file\_id}

##### [Delete File](https://platform.claude.com/docs/en/api/beta/files/delete)

DELETE/v1/files/{file\_id}

##### ModelsExpand Collapse

DeletedFile = object {id, type}

id: string

ID of the deleted file.

type: optional "file\_deleted"

Deleted object type.

For file deletion, this is always `"file_deleted"`.

FileMetadata = object {id, created\_at, filename, 4 more}

id: string

Unique object identifier.

The format and length of IDs may change over time.

created\_at: string

RFC 3339 datetime string representing when the file was created.

filename: string

Original filename of the uploaded file.

mime\_type: string

MIME type of the file.

size\_bytes: number

Size of the file in bytes.

type: "file"

Object type.

For files, this is always `"file"`.

downloadable: optional boolean

Whether the file can be downloaded.

#### BetaSkills

##### [Create Skill](https://platform.claude.com/docs/en/api/beta/skills/create)

POST/v1/skills

##### [List Skills](https://platform.claude.com/docs/en/api/beta/skills/list)

GET/v1/skills

##### [Get Skill](https://platform.claude.com/docs/en/api/beta/skills/retrieve)

GET/v1/skills/{skill\_id}

##### [Delete Skill](https://platform.claude.com/docs/en/api/beta/skills/delete)

DELETE/v1/skills/{skill\_id}

#### BetaSkillsVersions

##### [Create Skill Version](https://platform.claude.com/docs/en/api/beta/skills/versions/create)

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](https://platform.claude.com/docs/en/api/beta/skills/versions/list)

GET/v1/skills/{skill\_id}/versions

##### [Get Skill Version](https://platform.claude.com/docs/en/api/beta/skills/versions/retrieve)

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](https://platform.claude.com/docs/en/api/beta/skills/versions/delete)

DELETE/v1/skills/{skill\_id}/versions/{version}

a.claude.ai

# a.claude.ai is blocked

**a.claude.ai** refused to connect.

ERR\_BLOCKED\_BY\_RESPONSE

**a.claude.ai** refused to connect.

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)