[Skip to main content](https://cursor.com/docs/context/mcp-extension-api#main-content)

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

Get Started

# MCP Extension API Reference

The Cursor Extension API provides programmatic access to register and manage MCP servers without modifying `mcp.json` files directly. This is particularly useful for enterprise environments, onboarding tools, or MDM systems that need to dynamically configure MCP servers.

## [Overview](https://cursor.com/docs/context/mcp-extension-api\#overview)

The MCP Extension API allows you to:

- Register MCP servers programmatically
- Support both HTTP/SSE and stdio transport methods
- Use the same configuration schema as `mcp.json`
- Manage server registration dynamically

This API is useful for organizations that need to:

- Deploy MCP configurations programmatically
- Integrate MCP setup into onboarding workflows
- Manage MCP servers through enterprise tools
- Avoid manual `mcp.json` modifications

## [API Reference](https://cursor.com/docs/context/mcp-extension-api\#api-reference)

### [`vscode.cursor.mcp.registerServer`](https://cursor.com/docs/context/mcp-extension-api\#vscodecursormcpregisterserver)

Registers an MCP server that Cursor can communicate with.

**Signature:**

```
vscode.cursor.mcp.registerServer(config: ExtMCPServerConfig): void
```

**Parameters:**

- `config: ExtMCPServerConfig` \- The server configuration object

### [`vscode.cursor.mcp.unregisterServer`](https://cursor.com/docs/context/mcp-extension-api\#vscodecursormcpunregisterserver)

Unregisters a previously registered MCP server.

**Signature:**

```
vscode.cursor.mcp.unregisterServer(serverName: string): void
```

**Parameters:**

- `serverName: string` \- The name of the server to unregister

## [Type Definitions](https://cursor.com/docs/context/mcp-extension-api\#type-definitions)

Use these TypeScript definitions for type checking:

```
declare module "vscode" {
  export namespace cursor {
    export namespace mcp {
      export interface StdioServerConfig {
        name: string;
        server: {
          command: string;
          args: string[];
          env: Record<string, string>;
        };
      }

      export interface RemoteServerConfig {
        name: string;
        server: {
          url: string;
          /**
           * Optional HTTP headers to include with every request to this server (e.g. for authentication).
           * The keys are header names and the values are header values.
           */
          headers?: Record<string, string>;
        };
      }

      export type ExtMCPServerConfig = StdioServerConfig | RemoteServerConfig;

      /**
       * Register an MCP server that the Cursor extension can communicate with.
       *
       * The server can be exposed either over HTTP(S) (SSE/streamable HTTP) **or** as a local
       * stdio process.
       */
      export const registerServer: (config: ExtMCPServerConfig) => void;
      export const unregisterServer: (serverName: string) => void;
    }
  }
}
```

## [Configuration Types](https://cursor.com/docs/context/mcp-extension-api\#configuration-types)

### [HTTP/SSE Server Configuration](https://cursor.com/docs/context/mcp-extension-api\#httpsse-server-configuration)

For servers running on HTTP or Server-Sent Events:

```
interface RemoteServerConfig {
  name: string;
  server: {
    url: string;
    headers?: Record<string, string>;
  };
}
```

**Properties:**

- `name`: Unique identifier for the server
- `server.url`: The HTTP endpoint URL
- `server.headers` (optional): HTTP headers for authentication or other purposes

### [Stdio Server Configuration](https://cursor.com/docs/context/mcp-extension-api\#stdio-server-configuration)

For local servers that communicate via standard input/output:

```
interface StdioServerConfig {
  name: string;
  server: {
    command: string;
    args: string[];
    env: Record<string, string>;
  };
}
```

**Properties:**

- `name`: Unique identifier for the server
- `server.command`: The executable command
- `server.args`: Command line arguments
- `server.env`: Environment variables

## [Examples](https://cursor.com/docs/context/mcp-extension-api\#examples)

### [HTTP/SSE Server](https://cursor.com/docs/context/mcp-extension-api\#httpsse-server)

Register a remote MCP server with authentication:

```
vscode.cursor.mcp.registerServer({
  name: "my-remote-server",
  server: {
    url: "https://api.example.com/mcp",
    headers: {
      Authorization: "Bearer your-token-here",
      "X-API-Key": "your-api-key",
    },
  },
});
```

### [Stdio Server](https://cursor.com/docs/context/mcp-extension-api\#stdio-server)

Register a local MCP server:

```
vscode.cursor.mcp.registerServer({
  name: "my-local-server",
  server: {
    command: "python",
    args: ["-m", "my_mcp_server"],
    env: {
      API_KEY: "your-api-key",
      DEBUG: "true",
    },
  },
});
```

### [Node.js Server](https://cursor.com/docs/context/mcp-extension-api\#nodejs-server)

Register a Node.js-based MCP server:

```
vscode.cursor.mcp.registerServer({
  name: "nodejs-server",
  server: {
    command: "npx",
    args: ["-y", "@company/mcp-server"],
    env: {
      NODE_ENV: "production",
      CONFIG_PATH: "/path/to/config",
    },
  },
});
```

## [Managing Servers](https://cursor.com/docs/context/mcp-extension-api\#managing-servers)

### [Unregister a Server](https://cursor.com/docs/context/mcp-extension-api\#unregister-a-server)

```
// Unregister a previously registered server
vscode.cursor.mcp.unregisterServer("my-remote-server");
```

### [Conditional Registration](https://cursor.com/docs/context/mcp-extension-api\#conditional-registration)

```
// Only register if not already registered
if (!isServerRegistered("my-server")) {
  vscode.cursor.mcp.registerServer({
    name: "my-server",
    server: {
      url: "https://api.example.com/mcp",
    },
  });
}
```

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