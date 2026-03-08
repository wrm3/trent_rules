[Skip to main content](https://cursor.com/docs/cli/acp#main-content)

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

CLI

# ACP

## [Overview](https://cursor.com/docs/cli/acp\#overview)

Cursor CLI supports **ACP (Agent Client Protocol)** for advanced integrations. You can run `agent acp` and connect a custom client over `stdio` using JSON-RPC.

Learn more in the official [Agent Client Protocol docs](https://agentclientprotocol.com/).

ACP is intended for building custom clients and integrations. For normal terminal
workflows, use the interactive CLI with `agent`.

## [Start ACP server](https://cursor.com/docs/cli/acp\#start-acp-server)

Start Cursor CLI in ACP mode:

```
agent acp
```

## [Transport and message format](https://cursor.com/docs/cli/acp\#transport-and-message-format)

- Transport: `stdio`
- Protocol envelope: JSON-RPC 2.0
- Framing: newline-delimited JSON (one message per line)
- Direction:
  - Client writes requests/notifications to `stdin`
  - Cursor CLI writes responses/notifications to `stdout`
  - Logs may be written to `stderr`

## [Request flow](https://cursor.com/docs/cli/acp\#request-flow)

Typical ACP session flow:

1. `initialize`
2. `authenticate` with `methodId: "cursor_login"`
3. `session/new` (or `session/load`)
4. `session/prompt`
5. Handle `session/update` notifications while the model streams output
6. Handle `session/request_permission` by returning a decision
7. Optionally send `session/cancel`

## [Authentication](https://cursor.com/docs/cli/acp\#authentication)

Cursor CLI advertises `cursor_login` as the ACP auth method. In practice, you can pre-authenticate before startup using existing CLI auth paths:

- `agent login`
- `--api-key` (or `CURSOR_API_KEY`)
- `--auth-token` (or `CURSOR_AUTH_TOKEN`)

You can also pass endpoint and TLS options from the root CLI command:

```
agent --api-key "$CURSOR_API_KEY" acp
agent -e https://api2.cursor.sh acp
agent -k acp
```

## [Sessions, modes, and permissions](https://cursor.com/docs/cli/acp\#sessions-modes-and-permissions)

### [Sessions](https://cursor.com/docs/cli/acp\#sessions)

- Create a session with `session/new`
- Resume an existing conversation with `session/load`

### [Modes](https://cursor.com/docs/cli/acp\#modes)

ACP sessions support the same core modes as CLI:

- `agent` (full tool access)
- `plan` (planning, read-only behavior)
- `ask` (Q&A/read-only behavior)

### [Permissions](https://cursor.com/docs/cli/acp\#permissions)

When tools need approval, Cursor sends `session/request_permission`. Clients should return one of:

- `allow-once`
- `allow-always`
- `reject-once`

If your client does not answer permission requests, tool execution can block.

## [Cursor extension methods](https://cursor.com/docs/cli/acp\#cursor-extension-methods)

Cursor also sends ACP extension methods for richer client UX:

| Method | Use |
| --- | --- |
| `cursor/ask_question` | Ask users multiple-choice questions |
| `cursor/create_plan` | Request explicit plan approval |
| `cursor/update_todos` | Notify client about todo state updates |
| `cursor/task` | Notify client about subagent task completion |
| `cursor/generate_image` | Notify client about generated image output |

Clients can implement these methods to match Cursor-native interaction behavior.

## [Minimal Node.js client](https://cursor.com/docs/cli/acp\#minimal-nodejs-client)

This example shows the minimum control flow for a custom ACP client:

```
import { spawn } from "node:child_process";
import readline from "node:readline";

const agent = spawn("agent", ["acp"], { stdio: ["pipe", "pipe", "inherit"] });

let nextId = 1;
const pending = new Map();

function send(method, params) {
  const id = nextId++;
  agent.stdin.write(JSON.stringify({ jsonrpc: "2.0", id, method, params }) + "\n");
  return new Promise((resolve, reject) => pending.set(id, { resolve, reject }));
}

function respond(id, result) {
  agent.stdin.write(JSON.stringify({ jsonrpc: "2.0", id, result }) + "\n");
}

const rl = readline.createInterface({ input: agent.stdout });
rl.on("line", line => {
  const msg = JSON.parse(line);

  if (msg.id && (msg.result || msg.error)) {
    const waiter = pending.get(msg.id);
    if (!waiter) return;
    pending.delete(msg.id);
    msg.error ? waiter.reject(msg.error) : waiter.resolve(msg.result);
    return;
  }

  if (msg.method === "session/update") {
    const update = msg.params?.update;
    if (update?.sessionUpdate === "agent_message_chunk" && update.content?.text) {
      process.stdout.write(update.content.text);
    }
    return;
  }

  if (msg.method === "session/request_permission") {
    respond(msg.id, { outcome: { outcome: "selected", optionId: "allow-once" } });
  }
});

const init = async () => {
  await send("initialize", {
    protocolVersion: 1,
    clientCapabilities: { fs: { readTextFile: false, writeTextFile: false }, terminal: false },
    clientInfo: { name: "acp-minimal-client", version: "0.1.0" }
  });

  await send("authenticate", { methodId: "cursor_login" });
  const { sessionId } = await send("session/new", { cwd: process.cwd(), mcpServers: [] });
  const result = await send("session/prompt", {
    sessionId,
    prompt: [{ type: "text", text: "Say hello in one sentence." }]
  });

  console.log(`\n\n[stopReason=${result.stopReason}]`);
};

init().finally(() => {
  agent.stdin.end();
  agent.kill();
});
```

## [IDE integrations](https://cursor.com/docs/cli/acp\#ide-integrations)

ACP enables Cursor's AI agent to work with editors beyond the Cursor desktop app. Build or use third-party integrations for your preferred development environment.

### [Example use cases](https://cursor.com/docs/cli/acp\#example-use-cases)

- **JetBrains IDEs** — Connect IntelliJ IDEA, WebStorm, PyCharm, or other JetBrains IDEs to Cursor's agent. See the [JetBrains integration guide](https://cursor.com/docs/integrations/jetbrains) for setup instructions.

- **Neovim (avante.nvim)** — Use [avante.nvim](https://github.com/yetone/avante.nvim) to connect Neovim to Cursor's agent through ACP. See [Neovim setup](https://cursor.com/docs/cli/acp#neovim-avantenvim) below.

- **Zed** — Integrate with Zed's modern editor by spawning `agent acp` and communicating over stdio. Zed extensions can implement the ACP client protocol to route AI requests to Cursor.

- **Custom editors** — Any editor with extension support can implement an ACP client. Spawn the agent process, send JSON-RPC messages over stdio, and handle responses in your editor's UI.


### [Neovim (avante.nvim)](https://cursor.com/docs/cli/acp\#neovim-avantenvim)

[avante.nvim](https://github.com/yetone/avante.nvim) is a Neovim plugin that provides an AI-powered coding assistant. It supports ACP, so you can connect it to Cursor's agent for agentic coding inside Neovim.

Add the following to your lazy.nvim plugin configuration (e.g., `~/.config/nvim/lua/plugins/avante.lua`):

```
return {
  {
    "yetone/avante.nvim",
    event = "VeryLazy",
    version = false,
    build = "make",
    opts = {
      provider = "cursor",
      mode = "agentic",
      acp_providers = {
        cursor = {
          command = os.getenv("HOME") .. "/.local/bin/agent",
          args = { "acp" },
          auth_method = "cursor_login",
          env = {
            HOME = os.getenv("HOME"),
            PATH = os.getenv("PATH"),
          },
        },
      },
    },
    dependencies = {
      "nvim-lua/plenary.nvim",
      "MunifTanjim/nui.nvim",
      "nvim-tree/nvim-web-devicons",
      {
        "MeanderingProgrammer/render-markdown.nvim",
        opts = {
          file_types = { "markdown", "Avante" },
        },
        ft = { "markdown", "Avante" },
      },
    },
  },
}
```

Key settings:

- **`provider`**: Set to `"cursor"` to route requests through Cursor's agent.
- **`mode`**: Set to `"agentic"` for full tool access (file edits, terminal commands). Use `"normal"` for chat-only mode.
- **`command`**: Points to the `agent` binary. The default install path is `~/.local/bin/agent`. Adjust if you installed it elsewhere.
- **`auth_method`**: Uses `"cursor_login"`. Run `agent login` in your terminal first to authenticate.

### [Building an integration](https://cursor.com/docs/cli/acp\#building-an-integration)

1. Spawn `agent acp` as a child process
2. Communicate over stdin/stdout using JSON-RPC
3. Handle `session/update` notifications to display streaming responses
4. Respond to `session/request_permission` when tools need approval
5. Optionally implement Cursor extension methods for richer UX

See the [minimal Node.js client](https://cursor.com/docs/cli/acp#minimal-nodejs-client) above for a working reference implementation.

## [Related](https://cursor.com/docs/cli/acp\#related)

[MCP in CLI\\
\\
Manage and use MCP servers from Cursor CLI](https://cursor.com/docs/cli/mcp) [MCP Overview\\
\\
Learn MCP transports, configuration, and server setup](https://cursor.com/docs/mcp)

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