[Skip to main content](https://cursor.com/docs/agent/tools/terminal#main-content)

## Command Palette

Search for a command to run...

## Get Started

[Welcome](https://cursor.com/docs) [Quickstart](https://cursor.com/docs/get-started/quickstart)
Models & Pricing

## Agent

[Overview](https://cursor.com/docs/agent/overview) [Planning](https://cursor.com/docs/agent/plan-mode) [Prompting](https://cursor.com/docs/agent/prompting) [Debugging](https://cursor.com/docs/agent/debug-mode)
Tools

[Terminal](https://cursor.com/docs/agent/tools/terminal)

[Browser](https://cursor.com/docs/agent/tools/browser)

[Search](https://cursor.com/docs/agent/tools/search)

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

Agent

# Terminal

Agent runs shell commands directly in your terminal, with safe sandbox execution on macOS, Linux, and Windows.

## [Sandbox](https://cursor.com/docs/agent/tools/terminal\#sandbox)

By default, Agent runs terminal commands in a restricted environment that blocks unauthorized file access and network activity. Commands execute automatically while staying confined to your workspace.

For a deep dive into how sandboxing is implemented on each platform, see [Implementing a secure sandbox for local agents](https://cursor.com/blog/agent-sandboxing).

### [Platform requirements](https://cursor.com/docs/agent/tools/terminal\#platform-requirements)

### macOS

- Cursor v2.0 or later
- Works out of the box with no additional setup

### Windows

- [WSL2](https://learn.microsoft.com/en-us/windows/wsl/about) must be installed and configured
- The sandbox runs inside WSL2, applying the same restrictions as on Linux

### Linux

- **Kernel 6.2 or later** with Landlock v3 support (`CONFIG_SECURITY_LANDLOCK=y`)
- **Unprivileged user namespaces** enabled (most distributions enable this by default)

If your kernel doesn't meet these requirements, Agent falls back to asking for approval before running commands.

**AppArmor setup**

Some distributions restrict user namespaces through AppArmor. The Cursor desktop package ships with the required profile, so no extra setup is needed for local installations.

Remote environments and the standalone [CLI](https://cursor.com/docs/cli/overview) don't include this profile. If sandbox creation fails with a permissions error related to user namespaces, install the AppArmor package for your distribution:

Debian / Ubuntu:

```
curl -fsSL https://downloads.cursor.com/lab/enterprise/cursor-sandbox-apparmor_0.2.0_all.deb -o cursor-sandbox-apparmor.deb
sudo dpkg -i cursor-sandbox-apparmor.deb
```

RHEL / Fedora:

```
curl -fsSL https://downloads.cursor.com/lab/enterprise/cursor-sandbox-apparmor-0.2.0-1.noarch.rpm -o cursor-sandbox-apparmor.rpm
sudo rpm -i cursor-sandbox-apparmor.rpm
```

After installing, restart Cursor or your CLI session for the sandbox to work.

### [How the sandbox works](https://cursor.com/docs/agent/tools/terminal\#how-the-sandbox-works)

The sandbox prevents unauthorized access while allowing workspace operations:

| Access Type | Description |
| --- | --- |
| **File access** | Read access to the filesystem<br>Read and write access to workspace directories |
| **Network access** | Blocked by default. Configure with [`sandbox.json`](https://cursor.com/docs/reference/sandbox) or in settings. |
| **Temporary files** | Full access to `/tmp/` or equivalent system temp directories |

The `.cursor` configuration directory stays protected regardless of allowlist settings.

Some commands need full system access and bypass the sandbox. Agent will indicate when a command runs outside the sandbox and ask for your approval.

### [Allowlist](https://cursor.com/docs/agent/tools/terminal\#allowlist)

Commands on the allowlist skip sandbox restrictions and run immediately. You can add commands to the allowlist by choosing "Add to allowlist" when prompted after a sandboxed command fails.

When a sandboxed command fails due to restrictions, you can:

| Option | Description |
| --- | --- |
| **Skip** | Cancel the command and let Agent try something else |
| **Run** | Execute the command without sandbox restrictions |
| **Add to allowlist** | Run without restrictions and automatically approve it for future use |

#### [Default network allowlist](https://cursor.com/docs/agent/tools/terminal\#default-network-allowlist)

When network access is enabled, outbound connections are restricted to a curated set of domains. These cover common package registries, cloud providers, and language toolchains so most development workflows work without extra configuration.

### View default allowed domains

```
*.cloudflarestorage.com
*.docker.com
*.docker.io
*.googleapis.com
*.githubusercontent.com
*.gvt1.com
*.public.blob.vercel-storage.com
*.yarnpkg.com
alpinelinux.org
anaconda.com
apache.org
apt.llvm.org
archive.ubuntu.com
archlinux.org
awscli.amazonaws.com
azure.com
binaries.prisma.sh
bitbucket.org
centos.org
cloudflarestorage.com
cocoapods.org
codeload.github.com
cpan.org
crates.io
debian.org
dl.google.com
docker.com
docker.io
dot.net
dotnet.microsoft.com
eclipse.org
fedoraproject.org
files.pythonhosted.org
fonts.gstatic.com
gcr.io
ghcr.io
github.com
gitlab.com
golang.org
google.com
goproxy.io
gradle.org
haskell.org
hashicorp.com
hex.pm
index.crates.io
java.com
java.net
json-schema.org
json.schemastore.org
k8s.io
launchpad.net
maven.org
mcr.microsoft.com
metacpan.org
microsoft.com
mise.run
nodejs.org
npm.duckdb.org
npmjs.com
npmjs.org
nuget.org
oracle.com
packagecloud.io
packages.microsoft.com
packagist.org
pkg.go.dev
playwright.azureedge.net
ppa.launchpad.net
proxy.golang.org
pub.dev
public.blob.vercel-storage.com
public.ecr.aws
pypa.io
pypi.org
pypi.python.org
pythonhosted.org
quay.io
registry.npmjs.org
registry.yarnpkg.com
repo.maven.apache.org
ruby-lang.org
rubygems.org
rubyonrails.org
rustup.rs
rvm.io
security.ubuntu.com
sh.rustup.rs
sourceforge.net
spring.io
static.crates.io
static.rust-lang.org
sum.golang.org
swift.org
ubuntu.com
visualstudio.com
yarnpkg.com
ziglang.org
```

## [Sandbox configuration](https://cursor.com/docs/agent/tools/terminal\#sandbox-configuration)

Customize sandbox behavior with a `sandbox.json` file placed at `~/.cursor/sandbox.json` (per-user) or `<workspace>/.cursor/sandbox.json` (per-repo). Control network access, filesystem paths, build caches, and more.

See the [`sandbox.json` reference](https://cursor.com/docs/reference/sandbox) for the full schema, network pattern syntax, merge behavior, and protected paths.

## [Editor configuration](https://cursor.com/docs/agent/tools/terminal\#editor-configuration)

Configure how Agent runs terminal commands at **Settings > Cursor Settings > Agents > Auto-Run**.

### [Auto-run mode](https://cursor.com/docs/agent/tools/terminal\#auto-run-mode)

Choose how Agent runs tools like command execution, MCP, and file writes:

| Mode | Behavior |
| --- | --- |
| **Run in Sandbox** | Tools and commands auto-run in the sandbox where possible. Available on macOS, Linux, and Windows (via WSL2). |
| **Ask Every Time** | All tools and commands require user approval before running. |
| **Run Everything** | The agent runs all tools and commands automatically without asking for input. |

### [Auto-run network access](https://cursor.com/docs/agent/tools/terminal\#auto-run-network-access)

Choose how sandboxed commands access the network:

| Mode | Behavior |
| --- | --- |
| **sandbox.json Only** | Network is limited to domains in your `sandbox.json` allowlist. No Cursor defaults are added. |
| **sandbox.json + Defaults** | Your allowlist plus Cursor's built-in defaults (common package managers, etc.). This is the default. |
| **Allow All** | All network access is allowed in the sandbox, regardless of `sandbox.json`. |

### [Protection settings](https://cursor.com/docs/agent/tools/terminal\#protection-settings)

| Setting | Description |
| --- | --- |
| **Command Allowlist** | Commands that can run automatically outside of the sandbox. |
| **MCP Allowlist** | MCP tools that can run automatically outside of the sandbox. |
| **Browser Protection** | Prevent Agent from automatically running [Browser](https://cursor.com/docs/agent/tools/browser) tools. |
| **File-Deletion Protection** | Prevent Agent from deleting files automatically. |
| **Dotfile Protection** | Prevent Agent from modifying dot files like .gitignore automatically. |
| **External-File Protection** | Prevent Agent from creating or modifying files outside of the workspace automatically. |

## [Enterprise controls](https://cursor.com/docs/agent/tools/terminal\#enterprise-controls)

Only available for Enterprise subscriptions.

Enterprise admins can override editor configurations or change which settings are visible for end users. Navigate to **Settings > Auto-Run** in the [web dashboard](https://cursor.com/dashboard?tab=settings) to view and change these settings.

| Setting | Description |
| --- | --- |
| **Auto-Run Controls** | Enable controls for auto-run and sandbox mode. When disabled, commands auto-run in the sandbox where available, otherwise they ask for permission. |
| **Sandboxing Mode** | Control whether sandbox is available for end users. When enabled, commands auto-run in the sandbox even if they are not on the allowlist. |
| **Sandbox Networking** | Choose whether sandboxed commands have network access. |
| **Delete File Protection** | Prevent Agent from deleting files automatically. |
| **MCP Tool Protection** | Prevent Agent from automatically running MCP tools. |
| **Terminal Command Allowlist** | Commands that can run automatically without sandboxing. When sandbox is enabled, commands not on this list auto-run in sandbox mode. |
| **Enable Run Everything** | Give end users the ability to enable the "Run Everything" auto-run mode. |

## [Troubleshooting](https://cursor.com/docs/agent/tools/terminal\#troubleshooting)

Some shell themes (for example, Powerlevel9k/Powerlevel10k) can interfere with
the inline terminal output. If your command output looks truncated or
misformatted, disable the theme or switch to a simpler prompt when Agent runs.

### [Disable heavy prompts for Agent sessions](https://cursor.com/docs/agent/tools/terminal\#disable-heavy-prompts-for-agent-sessions)

Use the `CURSOR_AGENT` environment variable in your shell config to detect when
the Agent is running and skip initializing fancy prompts/themes.

```
# ~/.zshrc — disable Powerlevel10k when Cursor Agent runs
if [[ -n "$CURSOR_AGENT" ]]; then
  # Skip theme initialization for better compatibility
else
  [[ -r ~/.p10k.zsh ]] && source ~/.p10k.zsh
fi
```

```
# ~/.bashrc — fall back to a simple prompt in Agent sessions
if [[ -n "$CURSOR_AGENT" ]]; then
  PS1='\u@\h \W \$ '
fi
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