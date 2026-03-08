[Skip to main content](https://code.claude.com/docs/en/network-config#content-area)

[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/light.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=d535f2e20f53cd911acc59ad1b64b2e0)![dark logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/dark.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=28e49a2ffe69101f4aae9bfa70b393d0)](https://code.claude.com/docs)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Deployment

Enterprise network configuration

[Getting started](https://code.claude.com/docs/en/overview) [Build with Claude Code](https://code.claude.com/docs/en/sub-agents) [Deployment](https://code.claude.com/docs/en/third-party-integrations) [Administration](https://code.claude.com/docs/en/setup) [Configuration](https://code.claude.com/docs/en/settings) [Reference](https://code.claude.com/docs/en/cli-reference) [Resources](https://code.claude.com/docs/en/legal-and-compliance)

On this page

- [Proxy configuration](https://code.claude.com/docs/en/network-config#proxy-configuration)
- [Environment variables](https://code.claude.com/docs/en/network-config#environment-variables)
- [Basic authentication](https://code.claude.com/docs/en/network-config#basic-authentication)
- [Custom CA certificates](https://code.claude.com/docs/en/network-config#custom-ca-certificates)
- [mTLS authentication](https://code.claude.com/docs/en/network-config#mtls-authentication)
- [Network access requirements](https://code.claude.com/docs/en/network-config#network-access-requirements)
- [Additional resources](https://code.claude.com/docs/en/network-config#additional-resources)

Claude Code supports various enterprise network and security configurations through environment variables. This includes routing traffic through corporate proxy servers, trusting custom Certificate Authorities (CA), and authenticating with mutual Transport Layer Security (mTLS) certificates for enhanced security.

All environment variables shown on this page can also be configured in [`settings.json`](https://code.claude.com/docs/en/settings).

## [​](https://code.claude.com/docs/en/network-config\#proxy-configuration)  Proxy configuration

### [​](https://code.claude.com/docs/en/network-config\#environment-variables)  Environment variables

Claude Code respects standard proxy environment variables:

Report incorrect code

Copy

Ask AI

```
# HTTPS proxy (recommended)
export HTTPS_PROXY=https://proxy.example.com:8080

# HTTP proxy (if HTTPS not available)
export HTTP_PROXY=http://proxy.example.com:8080

# Bypass proxy for specific requests - space-separated format
export NO_PROXY="localhost 192.168.1.1 example.com .example.com"
# Bypass proxy for specific requests - comma-separated format
export NO_PROXY="localhost,192.168.1.1,example.com,.example.com"
# Bypass proxy for all requests
export NO_PROXY="*"
```

Claude Code does not support SOCKS proxies.

### [​](https://code.claude.com/docs/en/network-config\#basic-authentication)  Basic authentication

If your proxy requires basic authentication, include credentials in the proxy URL:

Report incorrect code

Copy

Ask AI

```
export HTTPS_PROXY=http://username:password@proxy.example.com:8080
```

Avoid hardcoding passwords in scripts. Use environment variables or secure credential storage instead.

For proxies requiring advanced authentication (NTLM, Kerberos, etc.), consider using an LLM Gateway service that supports your authentication method.

## [​](https://code.claude.com/docs/en/network-config\#custom-ca-certificates)  Custom CA certificates

If your enterprise environment uses custom CAs for HTTPS connections (whether through a proxy or direct API access), configure Claude Code to trust them:

Report incorrect code

Copy

Ask AI

```
export NODE_EXTRA_CA_CERTS=/path/to/ca-cert.pem
```

## [​](https://code.claude.com/docs/en/network-config\#mtls-authentication)  mTLS authentication

For enterprise environments requiring client certificate authentication:

Report incorrect code

Copy

Ask AI

```
# Client certificate for authentication
export CLAUDE_CODE_CLIENT_CERT=/path/to/client-cert.pem

# Client private key
export CLAUDE_CODE_CLIENT_KEY=/path/to/client-key.pem

# Optional: Passphrase for encrypted private key
export CLAUDE_CODE_CLIENT_KEY_PASSPHRASE="your-passphrase"
```

## [​](https://code.claude.com/docs/en/network-config\#network-access-requirements)  Network access requirements

Claude Code requires access to the following URLs:

- `api.anthropic.com`: Claude API endpoints
- `claude.ai`: authentication for claude.ai accounts
- `platform.claude.com`: authentication for Anthropic Console accounts

Ensure these URLs are allowlisted in your proxy configuration and firewall rules. This is especially important when using Claude Code in containerized or restricted network environments.

## [​](https://code.claude.com/docs/en/network-config\#additional-resources)  Additional resources

- [Claude Code settings](https://code.claude.com/docs/en/settings)
- [Environment variables reference](https://code.claude.com/docs/en/settings#environment-variables)
- [Troubleshooting guide](https://code.claude.com/docs/en/troubleshooting)

Was this page helpful?

YesNo

[Microsoft Foundry](https://code.claude.com/docs/en/microsoft-foundry) [LLM gateway](https://code.claude.com/docs/en/llm-gateway)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.