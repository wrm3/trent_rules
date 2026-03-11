[Skip to main content](https://code.claude.com/docs/en/interactive-mode#content-area)

[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/light.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=d535f2e20f53cd911acc59ad1b64b2e0)![dark logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/dark.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=28e49a2ffe69101f4aae9bfa70b393d0)](https://code.claude.com/docs)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Reference

Interactive mode

[Getting started](https://code.claude.com/docs/en/overview) [Build with Claude Code](https://code.claude.com/docs/en/sub-agents) [Deployment](https://code.claude.com/docs/en/third-party-integrations) [Administration](https://code.claude.com/docs/en/setup) [Configuration](https://code.claude.com/docs/en/settings) [Reference](https://code.claude.com/docs/en/cli-reference) [Resources](https://code.claude.com/docs/en/legal-and-compliance)

On this page

- [Keyboard shortcuts](https://code.claude.com/docs/en/interactive-mode#keyboard-shortcuts)
- [General controls](https://code.claude.com/docs/en/interactive-mode#general-controls)
- [Text editing](https://code.claude.com/docs/en/interactive-mode#text-editing)
- [Theme and display](https://code.claude.com/docs/en/interactive-mode#theme-and-display)
- [Multiline input](https://code.claude.com/docs/en/interactive-mode#multiline-input)
- [Quick commands](https://code.claude.com/docs/en/interactive-mode#quick-commands)
- [Built-in commands](https://code.claude.com/docs/en/interactive-mode#built-in-commands)
- [MCP prompts](https://code.claude.com/docs/en/interactive-mode#mcp-prompts)
- [Vim editor mode](https://code.claude.com/docs/en/interactive-mode#vim-editor-mode)
- [Mode switching](https://code.claude.com/docs/en/interactive-mode#mode-switching)
- [Navigation (NORMAL mode)](https://code.claude.com/docs/en/interactive-mode#navigation-normal-mode)
- [Editing (NORMAL mode)](https://code.claude.com/docs/en/interactive-mode#editing-normal-mode)
- [Text objects (NORMAL mode)](https://code.claude.com/docs/en/interactive-mode#text-objects-normal-mode)
- [Command history](https://code.claude.com/docs/en/interactive-mode#command-history)
- [Reverse search with Ctrl+R](https://code.claude.com/docs/en/interactive-mode#reverse-search-with-ctrl%2Br)
- [Background bash commands](https://code.claude.com/docs/en/interactive-mode#background-bash-commands)
- [How backgrounding works](https://code.claude.com/docs/en/interactive-mode#how-backgrounding-works)
- [Bash mode with ! prefix](https://code.claude.com/docs/en/interactive-mode#bash-mode-with-prefix)
- [Prompt suggestions](https://code.claude.com/docs/en/interactive-mode#prompt-suggestions)
- [Task list](https://code.claude.com/docs/en/interactive-mode#task-list)
- [PR review status](https://code.claude.com/docs/en/interactive-mode#pr-review-status)
- [See also](https://code.claude.com/docs/en/interactive-mode#see-also)

## [​](https://code.claude.com/docs/en/interactive-mode\#keyboard-shortcuts)  Keyboard shortcuts

Keyboard shortcuts may vary by platform and terminal. Press `?` to see available shortcuts for your environment.**macOS users**: Option/Alt key shortcuts (`Alt+B`, `Alt+F`, `Alt+Y`, `Alt+M`, `Alt+P`) require configuring Option as Meta in your terminal:

- **iTerm2**: settings → Profiles → Keys → set Left/Right Option key to “Esc+”
- **Terminal.app**: settings → Profiles → Keyboard → check “Use Option as Meta Key”
- **VS Code**: settings → Profiles → Keys → set Left/Right Option key to “Esc+”

See [Terminal configuration](https://code.claude.com/docs/en/terminal-config) for details.

### [​](https://code.claude.com/docs/en/interactive-mode\#general-controls)  General controls

| Shortcut | Description | Context |
| --- | --- | --- |
| `Ctrl+C` | Cancel current input or generation | Standard interrupt |
| `Ctrl+F` | Kill all background agents. Press twice within 3 seconds to confirm | Background agent control |
| `Ctrl+D` | Exit Claude Code session | EOF signal |
| `Ctrl+G` | Open in default text editor | Edit your prompt or custom response in your default text editor |
| `Ctrl+L` | Clear terminal screen | Keeps conversation history |
| `Ctrl+O` | Toggle verbose output | Shows detailed tool usage and execution |
| `Ctrl+R` | Reverse search command history | Search through previous commands interactively |
| `Ctrl+V` or `Cmd+V` (iTerm2) or `Alt+V` (Windows) | Paste image from clipboard | Pastes an image or path to an image file |
| `Ctrl+B` | Background running tasks | Backgrounds bash commands and agents. Tmux users press twice |
| `Ctrl+T` | Toggle task list | Show or hide the [task list](https://code.claude.com/docs/en/interactive-mode#task-list) in the terminal status area |
| `Left/Right arrows` | Cycle through dialog tabs | Navigate between tabs in permission dialogs and menus |
| `Up/Down arrows` | Navigate command history | Recall previous inputs |
| `Esc` \+ `Esc` | Rewind or summarize | Restore code and/or conversation to a previous point, or summarize from a selected message |
| `Shift+Tab` or `Alt+M` (some configurations) | Toggle permission modes | Switch between Auto-Accept Mode, Plan Mode, and normal mode. |
| `Option+P` (macOS) or `Alt+P` (Windows/Linux) | Switch model | Switch models without clearing your prompt |
| `Option+T` (macOS) or `Alt+T` (Windows/Linux) | Toggle extended thinking | Enable or disable extended thinking mode. Run `/terminal-setup` first to enable this shortcut |

### [​](https://code.claude.com/docs/en/interactive-mode\#text-editing)  Text editing

| Shortcut | Description | Context |
| --- | --- | --- |
| `Ctrl+K` | Delete to end of line | Stores deleted text for pasting |
| `Ctrl+U` | Delete entire line | Stores deleted text for pasting |
| `Ctrl+Y` | Paste deleted text | Paste text deleted with `Ctrl+K` or `Ctrl+U` |
| `Alt+Y` (after `Ctrl+Y`) | Cycle paste history | After pasting, cycle through previously deleted text. Requires [Option as Meta](https://code.claude.com/docs/en/interactive-mode#keyboard-shortcuts) on macOS |
| `Alt+B` | Move cursor back one word | Word navigation. Requires [Option as Meta](https://code.claude.com/docs/en/interactive-mode#keyboard-shortcuts) on macOS |
| `Alt+F` | Move cursor forward one word | Word navigation. Requires [Option as Meta](https://code.claude.com/docs/en/interactive-mode#keyboard-shortcuts) on macOS |

### [​](https://code.claude.com/docs/en/interactive-mode\#theme-and-display)  Theme and display

| Shortcut | Description | Context |
| --- | --- | --- |
| `Ctrl+T` | Toggle syntax highlighting for code blocks | Only works inside the `/theme` picker menu. Controls whether code in Claude’s responses uses syntax coloring |

Syntax highlighting is only available in the native build of Claude Code.

### [​](https://code.claude.com/docs/en/interactive-mode\#multiline-input)  Multiline input

| Method | Shortcut | Context |
| --- | --- | --- |
| Quick escape | `\` \+ `Enter` | Works in all terminals |
| macOS default | `Option+Enter` | Default on macOS |
| Shift+Enter | `Shift+Enter` | Works out of the box in iTerm2, WezTerm, Ghostty, Kitty |
| Control sequence | `Ctrl+J` | Line feed character for multiline |
| Paste mode | Paste directly | For code blocks, logs |

Shift+Enter works without configuration in iTerm2, WezTerm, Ghostty, and Kitty. For other terminals (VS Code, Alacritty, Zed, Warp), run `/terminal-setup` to install the binding.

### [​](https://code.claude.com/docs/en/interactive-mode\#quick-commands)  Quick commands

| Shortcut | Description | Notes |
| --- | --- | --- |
| `/` at start | Command or skill | See [built-in commands](https://code.claude.com/docs/en/interactive-mode#built-in-commands) and [skills](https://code.claude.com/docs/en/skills) |
| `!` at start | Bash mode | Run commands directly and add execution output to the session |
| `@` | File path mention | Trigger file path autocomplete |

## [​](https://code.claude.com/docs/en/interactive-mode\#built-in-commands)  Built-in commands

Type `/` in Claude Code to see all available commands, or type `/` followed by any letters to filter. Not all commands are visible to every user. Some depend on your platform, plan, or environment. For example, `/desktop` only appears on macOS and Windows, `/upgrade` and `/privacy-settings` are only available on Pro and Max plans, and `/terminal-setup` is hidden when your terminal natively supports its keybindings.Claude Code also ships with [bundled skills](https://code.claude.com/docs/en/skills#bundled-skills) like `/simplify`, `/batch`, and `/debug` that appear alongside built-in commands when you type `/`. To create your own commands, see [skills](https://code.claude.com/docs/en/skills).In the table below, `<arg>` indicates a required argument and `[arg]` indicates an optional one.

| Command | Purpose |
| --- | --- |
| `/add-dir <path>` | Add a new working directory to the current session |
| `/agents` | Manage [agent](https://code.claude.com/docs/en/sub-agents) configurations |
| `/chrome` | Configure [Claude in Chrome](https://code.claude.com/docs/en/chrome) settings |
| `/clear` | Clear conversation history and free up context. Aliases: `/reset`, `/new` |
| `/compact [instructions]` | Compact conversation with optional focus instructions |
| `/config` | Open the [Settings](https://code.claude.com/docs/en/settings) interface (Config tab). Alias: `/settings` |
| `/context` | Visualize current context usage as a colored grid |
| `/copy` | Copy the last assistant response to clipboard. When code blocks are present, shows an interactive picker to select individual blocks or the full response |
| `/cost` | Show token usage statistics. See [cost tracking guide](https://code.claude.com/docs/en/costs#using-the-cost-command) for subscription-specific details |
| `/desktop` | Continue the current session in the Claude Code Desktop app. macOS and Windows only. Alias: `/app` |
| `/diff` | Open an interactive diff viewer showing uncommitted changes and per-turn diffs. Use left/right arrows to switch between the current git diff and individual Claude turns, and up/down to browse files |
| `/doctor` | Diagnose and verify your Claude Code installation and settings |
| `/exit` | Exit the CLI. Alias: `/quit` |
| `/export [filename]` | Export the current conversation as plain text. With a filename, writes directly to that file. Without, opens a dialog to copy to clipboard or save to a file |
| `/extra-usage` | Configure extra usage to keep working when rate limits are hit |
| `/fast [on|off]` | Toggle [fast mode](https://code.claude.com/docs/en/fast-mode) on or off |
| `/feedback [report]` | Submit feedback about Claude Code. Alias: `/bug` |
| `/fork [name]` | Create a fork of the current conversation at this point |
| `/help` | Show help and available commands |
| `/hooks` | Manage [hook](https://code.claude.com/docs/en/hooks) configurations for tool events |
| `/ide` | Manage IDE integrations and show status |
| `/init` | Initialize project with `CLAUDE.md` guide |
| `/insights` | Generate a report analyzing your Claude Code sessions, including project areas, interaction patterns, and friction points |
| `/install-github-app` | Set up the [Claude GitHub Actions](https://code.claude.com/docs/en/github-actions) app for a repository. Walks you through selecting a repo and configuring the integration |
| `/install-slack-app` | Install the Claude Slack app. Opens a browser to complete the OAuth flow |
| `/keybindings` | Open or create your keybindings configuration file |
| `/login` | Sign in to your Anthropic account |
| `/logout` | Sign out from your Anthropic account |
| `/mcp` | Manage MCP server connections and OAuth authentication |
| `/memory` | Edit `CLAUDE.md` memory files, enable or disable [auto-memory](https://code.claude.com/docs/en/memory#auto-memory), and view auto-memory entries |
| `/mobile` | Show QR code to download the Claude mobile app. Aliases: `/ios`, `/android` |
| `/model [model]` | Select or change the AI model. For models that support it, use left/right arrows to [adjust effort level](https://code.claude.com/docs/en/model-config#adjust-effort-level). The change takes effect immediately without waiting for the current response to finish |
| `/output-style [style]` | Switch between [output styles](https://code.claude.com/docs/en/output-styles). **Default** is standard behavior, **Explanatory** adds educational insights about implementation choices and codebase patterns, and **Learning** pauses to ask you to write small code pieces for hands-on practice. You can also [create custom output styles](https://code.claude.com/docs/en/output-styles#create-a-custom-output-style) |
| `/passes` | Share a free week of Claude Code with friends. Only visible if your account is eligible |
| `/permissions` | View or update [permissions](https://code.claude.com/docs/en/permissions#manage-permissions). Alias: `/allowed-tools` |
| `/plan` | Enter plan mode directly from the prompt |
| `/plugin` | Manage Claude Code [plugins](https://code.claude.com/docs/en/plugins) |
| `/pr-comments [PR]` | Fetch and display comments from a GitHub pull request. Automatically detects the PR for the current branch, or pass a PR URL or number. Requires the `gh` CLI |
| `/privacy-settings` | View and update your privacy settings. Only available for Pro and Max plan subscribers |
| `/release-notes` | View the full changelog, with the most recent version closest to your prompt |
| `/reload-plugins` | Reload all active [plugins](https://code.claude.com/docs/en/plugins) to apply pending changes without restarting. Reports what was loaded and notes any changes that require a restart |
| `/remote-control` | Make this session available for [remote control](https://code.claude.com/docs/en/remote-control) from claude.ai. Alias: `/rc` |
| `/remote-env` | Configure the default remote environment for [teleport sessions](https://code.claude.com/docs/en/claude-code-on-the-web#teleport-a-web-session-to-your-terminal) |
| `/rename [name]` | Rename the current session. Without a name, auto-generates one from conversation history |
| `/resume [session]` | Resume a conversation by ID or name, or open the session picker. Alias: `/continue` |
| `/review` | Review a pull request for code quality, correctness, security, and test coverage. Pass a PR number, or omit to list open PRs. Requires the `gh` CLI |
| `/rewind` | Rewind the conversation and/or code to a previous point, or summarize from a selected message. See [checkpointing](https://code.claude.com/docs/en/checkpointing). Alias: `/checkpoint` |
| `/sandbox` | Toggle [sandbox mode](https://code.claude.com/docs/en/sandboxing). Available on supported platforms only |
| `/security-review` | Analyze pending changes on the current branch for security vulnerabilities. Reviews the git diff and identifies risks like injection, auth issues, and data exposure |
| `/skills` | List available [skills](https://code.claude.com/docs/en/skills) |
| `/stats` | Visualize daily usage, session history, streaks, and model preferences |
| `/status` | Open the Settings interface (Status tab) showing version, model, account, and connectivity |
| `/statusline` | Configure Claude Code’s [status line](https://code.claude.com/docs/en/statusline). Describe what you want, or run without arguments to auto-configure from your shell prompt |
| `/stickers` | Order Claude Code stickers |
| `/tasks` | List and manage background tasks |
| `/terminal-setup` | Configure terminal keybindings for Shift+Enter and other shortcuts. Only visible in terminals that need it, like VS Code, Alacritty, or Warp |
| `/theme` | Change the color theme. Includes light and dark variants, colorblind-accessible (daltonized) themes, and ANSI themes that use your terminal’s color palette |
| `/upgrade` | Open the upgrade page to switch to a higher plan tier |
| `/usage` | Show plan usage limits and rate limit status |
| `/vim` | Toggle between Vim and Normal editing modes |

### [​](https://code.claude.com/docs/en/interactive-mode\#mcp-prompts)  MCP prompts

MCP servers can expose prompts that appear as commands. These use the format `/mcp__<server>__<prompt>` and are dynamically discovered from connected servers. See [MCP prompts](https://code.claude.com/docs/en/mcp#use-mcp-prompts-as-commands) for details.

## [​](https://code.claude.com/docs/en/interactive-mode\#vim-editor-mode)  Vim editor mode

Enable vim-style editing with `/vim` command or configure permanently via `/config`.

### [​](https://code.claude.com/docs/en/interactive-mode\#mode-switching)  Mode switching

| Command | Action | From mode |
| --- | --- | --- |
| `Esc` | Enter NORMAL mode | INSERT |
| `i` | Insert before cursor | NORMAL |
| `I` | Insert at beginning of line | NORMAL |
| `a` | Insert after cursor | NORMAL |
| `A` | Insert at end of line | NORMAL |
| `o` | Open line below | NORMAL |
| `O` | Open line above | NORMAL |

### [​](https://code.claude.com/docs/en/interactive-mode\#navigation-normal-mode)  Navigation (NORMAL mode)

| Command | Action |
| --- | --- |
| `h`/`j`/`k`/`l` | Move left/down/up/right |
| `w` | Next word |
| `e` | End of word |
| `b` | Previous word |
| `0` | Beginning of line |
| `$` | End of line |
| `^` | First non-blank character |
| `gg` | Beginning of input |
| `G` | End of input |
| `f{char}` | Jump to next occurrence of character |
| `F{char}` | Jump to previous occurrence of character |
| `t{char}` | Jump to just before next occurrence of character |
| `T{char}` | Jump to just after previous occurrence of character |
| `;` | Repeat last f/F/t/T motion |
| `,` | Repeat last f/F/t/T motion in reverse |

In vim normal mode, if the cursor is at the beginning or end of input and cannot move further, the arrow keys navigate command history instead.

### [​](https://code.claude.com/docs/en/interactive-mode\#editing-normal-mode)  Editing (NORMAL mode)

| Command | Action |
| --- | --- |
| `x` | Delete character |
| `dd` | Delete line |
| `D` | Delete to end of line |
| `dw`/`de`/`db` | Delete word/to end/back |
| `cc` | Change line |
| `C` | Change to end of line |
| `cw`/`ce`/`cb` | Change word/to end/back |
| `yy`/`Y` | Yank (copy) line |
| `yw`/`ye`/`yb` | Yank word/to end/back |
| `p` | Paste after cursor |
| `P` | Paste before cursor |
| `>>` | Indent line |
| `<<` | Dedent line |
| `J` | Join lines |
| `.` | Repeat last change |

### [​](https://code.claude.com/docs/en/interactive-mode\#text-objects-normal-mode)  Text objects (NORMAL mode)

Text objects work with operators like `d`, `c`, and `y`:

| Command | Action |
| --- | --- |
| `iw`/`aw` | Inner/around word |
| `iW`/`aW` | Inner/around WORD (whitespace-delimited) |
| `i"`/`a"` | Inner/around double quotes |
| `i'`/`a'` | Inner/around single quotes |
| `i(`/`a(` | Inner/around parentheses |
| `i[`/`a[` | Inner/around brackets |\
| `i{`/`a{` | Inner/around braces |\
\
## [​](https://code.claude.com/docs/en/interactive-mode\#command-history)  Command history\
\
Claude Code maintains command history for the current session:\
\
- Input history is stored per working directory\
- Input history resets when you run `/clear` to start a new session. The previous session’s conversation is preserved and can be resumed.\
- Use Up/Down arrows to navigate (see keyboard shortcuts above)\
- **Note**: history expansion (`!`) is disabled by default\
\
### [​](https://code.claude.com/docs/en/interactive-mode\#reverse-search-with-ctrl+r)  Reverse search with Ctrl+R\
\
Press `Ctrl+R` to interactively search through your command history:\
\
1. **Start search**: press `Ctrl+R` to activate reverse history search\
2. **Type query**: enter text to search for in previous commands. The search term is highlighted in matching results\
3. **Navigate matches**: press `Ctrl+R` again to cycle through older matches\
4. **Accept match**:\
\
   - Press `Tab` or `Esc` to accept the current match and continue editing\
   - Press `Enter` to accept and execute the command immediately\
5. **Cancel search**:\
\
   - Press `Ctrl+C` to cancel and restore your original input\
   - Press `Backspace` on empty search to cancel\
\
The search displays matching commands with the search term highlighted, so you can find and reuse previous inputs.\
\
## [​](https://code.claude.com/docs/en/interactive-mode\#background-bash-commands)  Background bash commands\
\
Claude Code supports running bash commands in the background, allowing you to continue working while long-running processes execute.\
\
### [​](https://code.claude.com/docs/en/interactive-mode\#how-backgrounding-works)  How backgrounding works\
\
When Claude Code runs a command in the background, it runs the command asynchronously and immediately returns a background task ID. Claude Code can respond to new prompts while the command continues executing in the background.To run commands in the background, you can either:\
\
- Prompt Claude Code to run a command in the background\
- Press Ctrl+B to move a regular Bash tool invocation to the background. (Tmux users must press Ctrl+B twice due to tmux’s prefix key.)\
\
**Key features:**\
\
- Output is buffered and Claude can retrieve it using the TaskOutput tool\
- Background tasks have unique IDs for tracking and output retrieval\
- Background tasks are automatically cleaned up when Claude Code exits\
\
To disable all background task functionality, set the `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` environment variable to `1`. See [Environment variables](https://code.claude.com/docs/en/settings#environment-variables) for details.**Common backgrounded commands:**\
\
- Build tools (webpack, vite, make)\
- Package managers (npm, yarn, pnpm)\
- Test runners (jest, pytest)\
- Development servers\
- Long-running processes (docker, terraform)\
\
### [​](https://code.claude.com/docs/en/interactive-mode\#bash-mode-with-prefix)  Bash mode with `!` prefix\
\
Run bash commands directly without going through Claude by prefixing your input with `!`:\
\
Report incorrect code\
\
Copy\
\
Ask AI\
\
```\
! npm test\
! git status\
! ls -la\
```\
\
Bash mode:\
\
- Adds the command and its output to the conversation context\
- Shows real-time progress and output\
- Supports the same `Ctrl+B` backgrounding for long-running commands\
- Does not require Claude to interpret or approve the command\
- Supports history-based autocomplete: type a partial command and press **Tab** to complete from previous `!` commands in the current project\
- Exit with `Escape`, `Backspace`, or `Ctrl+U` on an empty prompt\
\
This is useful for quick shell operations while maintaining conversation context.\
\
## [​](https://code.claude.com/docs/en/interactive-mode\#prompt-suggestions)  Prompt suggestions\
\
When you first open a session, a grayed-out example command appears in the prompt input to help you get started. Claude Code picks this from your project’s git history, so it reflects files you’ve been working on recently.After Claude responds, suggestions continue to appear based on your conversation history, such as a follow-up step from a multi-part request or a natural continuation of your workflow.\
\
- Press **Tab** to accept the suggestion, or press **Enter** to accept and submit\
- Start typing to dismiss it\
\
The suggestion runs as a background request that reuses the parent conversation’s prompt cache, so the additional cost is minimal. Claude Code skips suggestion generation when the cache is cold to avoid unnecessary cost.Suggestions are automatically skipped after the first turn of a conversation, in non-interactive mode, and in plan mode.To disable prompt suggestions entirely, set the environment variable or toggle the setting in `/config`:\
\
Report incorrect code\
\
Copy\
\
Ask AI\
\
```\
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false\
```\
\
## [​](https://code.claude.com/docs/en/interactive-mode\#task-list)  Task list\
\
When working on complex, multi-step work, Claude creates a task list to track progress. Tasks appear in the status area of your terminal with indicators showing what’s pending, in progress, or complete.\
\
- Press `Ctrl+T` to toggle the task list view. The display shows up to 10 tasks at a time\
- To see all tasks or clear them, ask Claude directly: “show me all tasks” or “clear all tasks”\
- Tasks persist across context compactions, helping Claude stay organized on larger projects\
- To share a task list across sessions, set `CLAUDE_CODE_TASK_LIST_ID` to use a named directory in `~/.claude/tasks/`: `CLAUDE_CODE_TASK_LIST_ID=my-project claude`\
- To revert to the previous TODO list, set `CLAUDE_CODE_ENABLE_TASKS=false`.\
\
## [​](https://code.claude.com/docs/en/interactive-mode\#pr-review-status)  PR review status\
\
When working on a branch with an open pull request, Claude Code displays a clickable PR link in the footer (for example, “PR #446”). The link has a colored underline indicating the review state:\
\
- Green: approved\
- Yellow: pending review\
- Red: changes requested\
- Gray: draft\
- Purple: merged\
\
`Cmd+click` (Mac) or `Ctrl+click` (Windows/Linux) the link to open the pull request in your browser. The status updates automatically every 60 seconds.\
\
PR status requires the `gh` CLI to be installed and authenticated (`gh auth login`).\
\
## [​](https://code.claude.com/docs/en/interactive-mode\#see-also)  See also\
\
- [Skills](https://code.claude.com/docs/en/skills) \- Custom prompts and workflows\
- [Checkpointing](https://code.claude.com/docs/en/checkpointing) \- Rewind Claude’s edits and restore previous states\
- [CLI reference](https://code.claude.com/docs/en/cli-reference) \- Command-line flags and options\
- [Settings](https://code.claude.com/docs/en/settings) \- Configuration options\
- [Memory management](https://code.claude.com/docs/en/memory) \- Managing CLAUDE.md files\
\
Was this page helpful?\
\
YesNo\
\
[CLI reference](https://code.claude.com/docs/en/cli-reference) [Checkpointing](https://code.claude.com/docs/en/checkpointing)\
\
Ctrl+I\
\
Assistant\
\
Responses are generated using AI and may contain mistakes.