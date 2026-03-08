[Skip to main content](https://cursor.com/docs/get-started/quickstart#main-content)

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

# Quickstart

This quickstart walks you through working with Cursor's Agent. By the end, you'll understand how to plan effectively, manage context, and iterate on code with AI.

[Download Cursor⤓](https://cursor.com/downloads)

### macOS

- macOS 10.15 (Catalina) and later
- Native installer (.dmg)
- Apple Silicon and Intel support

### Windows

- Windows 10 and later
- Native installer (.exe)

### Linux

**Debian/Ubuntu (recommended)**

```
# Add Cursor's GPG key
curl -fsSL https://downloads.cursor.com/keys/anysphere.asc | gpg --dearmor | sudo tee /etc/apt/keyrings/cursor.gpg > /dev/null

# Add the Cursor repository
echo "deb [arch=amd64,arm64 signed-by=/etc/apt/keyrings/cursor.gpg] https://downloads.cursor.com/aptrepo stable main" | sudo tee /etc/apt/sources.list.d/cursor.list > /dev/null

# Update and install
sudo apt update
sudo apt install cursor
```

**RHEL/Fedora**

```
# Add Cursor's repository
sudo tee /etc/yum.repos.d/cursor.repo << 'EOF'
[cursor]
name=Cursor
baseurl=https://downloads.cursor.com/yumrepo
enabled=1
gpgcheck=1
gpgkey=https://downloads.cursor.com/keys/anysphere.asc
EOF

# Install Cursor
sudo dnf install cursor
```

**AppImage (portable)**

Download the `.AppImage` file from [cursor.com/downloads](https://cursor.com/downloads), then:

```
chmod +x Cursor-*.AppImage
./Cursor-*.AppImage
```

The apt and yum packages are preferred over AppImage. They provide desktop icons, automatic updates, and CLI tools.

## [Start with Agent](https://cursor.com/docs/get-started/quickstart\#start-with-agent)

Open the Agent panel with `Cmd ICtrl I`. Agent can complete complex coding tasks independently: searching your codebase, editing files, and running terminal commands.

How does this project work?

[Cursor LogoTry in Cursor](cursor://anysphere.cursor-deeplink/prompt?text=How%20does%20this%20project%20work%3F)

Agent will explore the codebase, read relevant files, and explain the architecture. This is one of the fastest ways to understand unfamiliar code.

## [Plan before building](https://cursor.com/docs/get-started/quickstart\#plan-before-building)

The most impactful change you can make is planning before coding.

Press `Shift+Tab` in the agent input to toggle **Plan Mode**. Instead of immediately writing code, Agent will:

1. Research your codebase to find relevant files
2. Ask clarifying questions about your requirements
3. Create a detailed implementation plan
4. Wait for your approval before building

Click "Save to workspace" to store plans in `.cursor/plans/`. This creates documentation for your team and provides context for future work.

Try it: Ask Agent to "add a new feature" in Plan Mode. Review the plan, make adjustments, then click to build.

## [Let Agent find context](https://cursor.com/docs/get-started/quickstart\#let-agent-find-context)

You don't need to manually tag every file in your prompt.

Agent has powerful search tools and pulls context on demand. When you ask about "the authentication flow," Agent finds relevant files through search, even if your prompt doesn't contain the exact file names.

Keep it simple: if you know the exact file, tag it with `@`. If not, Agent will find it. Including irrelevant files can confuse Agent about what's important.

## [Write specific prompts](https://cursor.com/docs/get-started/quickstart\#write-specific-prompts)

Agent's success rate improves significantly with specific instructions. Compare:

| Vague | Specific |
| --- | --- |
| "add tests for auth.ts" | "Write a test case for auth.ts covering the logout edge case, using the patterns in `__tests__/` and avoiding mocks" |
| "fix the bug" | "The login form submits twice when clicking the button. Find the cause and fix it" |

Be explicit about what you want, reference existing patterns, and describe the expected outcome.

## [Know when to start fresh](https://cursor.com/docs/get-started/quickstart\#know-when-to-start-fresh)

Long conversations can cause Agent to lose focus. Start a new conversation when:

- You're moving to a different task or feature
- Agent seems confused or keeps making the same mistakes
- You've finished one logical unit of work

Continue the conversation when:

- You're iterating on the same feature
- Agent needs context from earlier in the discussion
- You're debugging something it just built

Use `@Past Chats` to reference previous work in new conversations rather than copy-pasting entire discussions.

## [Review and iterate](https://cursor.com/docs/get-started/quickstart\#review-and-iterate)

Watch Agent work. The diff view shows changes as they happen. If you see Agent heading in the wrong direction, click **Stop** or press `Cmd Shift BackspaceCtrl Shift Backspace` to cancel and redirect.

After Agent finishes, click **Review** → **Find Issues** to run a dedicated review pass that analyzes proposed edits and flags potential problems.

AI-generated code can look right while being subtly wrong. Read the diffs carefully. The faster an agent works, the more important your review process becomes.

## [Provide verifiable goals](https://cursor.com/docs/get-started/quickstart\#provide-verifiable-goals)

Agents perform best when they have clear targets to iterate against:

- **Use typed languages** so Agent gets immediate feedback from the type checker
- **Write tests** so Agent can run them and iterate until they pass
- **Configure linters** to catch style and quality issues automatically

Try this workflow: Ask Agent to write tests first, confirm they fail, then ask it to implement code that passes the tests.

## [Next steps](https://cursor.com/docs/get-started/quickstart\#next-steps)

[Agent Overview\\
\\
Learn about Agent's tools and capabilities](https://cursor.com/docs/agent/overview) [Rules\\
\\
Create persistent instructions for your project](https://cursor.com/docs/rules) [Models & Pricing\\
\\
Compare models and understand usage pools](https://cursor.com/docs/models-and-pricing) [AI Foundations\\
\\
Deep dive into how AI works](https://cursor.com/learn)

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