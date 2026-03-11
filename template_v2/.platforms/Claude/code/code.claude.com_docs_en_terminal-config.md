[Skip to main content](https://code.claude.com/docs/en/terminal-config#content-area)

[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/light.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=d535f2e20f53cd911acc59ad1b64b2e0)![dark logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/dark.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=28e49a2ffe69101f4aae9bfa70b393d0)](https://code.claude.com/docs)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Configuration

Optimize your terminal setup

[Getting started](https://code.claude.com/docs/en/overview) [Build with Claude Code](https://code.claude.com/docs/en/sub-agents) [Deployment](https://code.claude.com/docs/en/third-party-integrations) [Administration](https://code.claude.com/docs/en/setup) [Configuration](https://code.claude.com/docs/en/settings) [Reference](https://code.claude.com/docs/en/cli-reference) [Resources](https://code.claude.com/docs/en/legal-and-compliance)

On this page

- [Themes and appearance](https://code.claude.com/docs/en/terminal-config#themes-and-appearance)
- [Line breaks](https://code.claude.com/docs/en/terminal-config#line-breaks)
- [Notification setup](https://code.claude.com/docs/en/terminal-config#notification-setup)
- [Terminal notifications](https://code.claude.com/docs/en/terminal-config#terminal-notifications)
- [Notification hooks](https://code.claude.com/docs/en/terminal-config#notification-hooks)
- [Handling large inputs](https://code.claude.com/docs/en/terminal-config#handling-large-inputs)
- [Vim Mode](https://code.claude.com/docs/en/terminal-config#vim-mode)

### [​](https://code.claude.com/docs/en/terminal-config\#themes-and-appearance)  Themes and appearance

Claude cannot control the theme of your terminal. That’s handled by your terminal application. You can match Claude Code’s theme to your terminal any time via the `/config` command.For additional customization of the Claude Code interface itself, you can configure a [custom status line](https://code.claude.com/docs/en/statusline) to display contextual information like the current model, working directory, or git branch at the bottom of your terminal.

### [​](https://code.claude.com/docs/en/terminal-config\#line-breaks)  Line breaks

You have several options for entering line breaks into Claude Code:

- **Quick escape**: Type `\` followed by Enter to create a newline
- **Shift+Enter**: Works out of the box in iTerm2, WezTerm, Ghostty, and Kitty
- **Keyboard shortcut**: Set up a keybinding to insert a newline in other terminals

**Set up Shift+Enter for other terminals**Run `/terminal-setup` within Claude Code to automatically configure Shift+Enter for VS Code, Alacritty, Zed, and Warp.

The `/terminal-setup` command is only visible in terminals that require manual configuration. If you’re using iTerm2, WezTerm, Ghostty, or Kitty, you won’t see this command because Shift+Enter already works natively.

**Set up Option+Enter (VS Code, iTerm2 or macOS Terminal.app)****For Mac Terminal.app:**

1. Open Settings → Profiles → Keyboard
2. Check “Use Option as Meta Key”

**For iTerm2 and VS Code terminal:**

1. Open Settings → Profiles → Keys
2. Under General, set Left/Right Option key to “Esc+“

### [​](https://code.claude.com/docs/en/terminal-config\#notification-setup)  Notification setup

When Claude finishes working and is waiting for your input, it fires a notification event. You can surface this event as a desktop notification through your terminal or run custom logic with [notification hooks](https://code.claude.com/docs/en/hooks#notification).

#### [​](https://code.claude.com/docs/en/terminal-config\#terminal-notifications)  Terminal notifications

Kitty and Ghostty support desktop notifications without additional configuration. iTerm 2 requires setup:

1. Open iTerm 2 Settings → Profiles → Terminal
2. Enable “Notification Center Alerts”
3. Click “Filter Alerts” and check “Send escape sequence-generated alerts”

If notifications aren’t appearing, verify that your terminal app has notification permissions in your OS settings.Other terminals, including the default macOS Terminal, do not support native notifications. Use [notification hooks](https://code.claude.com/docs/en/hooks#notification) instead.

#### [​](https://code.claude.com/docs/en/terminal-config\#notification-hooks)  Notification hooks

To add custom behavior when notifications fire, such as playing a sound or sending a message, configure a [notification hook](https://code.claude.com/docs/en/hooks#notification). Hooks run alongside terminal notifications, not as a replacement.

### [​](https://code.claude.com/docs/en/terminal-config\#handling-large-inputs)  Handling large inputs

When working with extensive code or long instructions:

- **Avoid direct pasting**: Claude Code may struggle with very long pasted content
- **Use file-based workflows**: Write content to a file and ask Claude to read it
- **Be aware of VS Code limitations**: The VS Code terminal is particularly prone to truncating long pastes

### [​](https://code.claude.com/docs/en/terminal-config\#vim-mode)  Vim Mode

Claude Code supports a subset of Vim keybindings that can be enabled with `/vim` or configured via `/config`.The supported subset includes:

- Mode switching: `Esc` (to NORMAL), `i`/`I`, `a`/`A`, `o`/`O` (to INSERT)
- Navigation: `h`/`j`/`k`/`l`, `w`/`e`/`b`, `0`/`$`/`^`, `gg`/`G`, `f`/`F`/`t`/`T` with `;`/`,` repeat
- Editing: `x`, `dw`/`de`/`db`/`dd`/`D`, `cw`/`ce`/`cb`/`cc`/`C`, `.` (repeat)
- Yank/paste: `yy`/`Y`, `yw`/`ye`/`yb`, `p`/`P`
- Text objects: `iw`/`aw`, `iW`/`aW`, `i"`/`a"`, `i'`/`a'`, `i(`/`a(`, `i[`/`a[`, `i{`/`a{`\
- Indentation: `>>`/`<<`\
- Line operations: `J` (join lines)\
\
See [Interactive mode](https://code.claude.com/docs/en/interactive-mode#vim-editor-mode) for the complete reference.\
\
Was this page helpful?\
\
YesNo\
\
[Sandboxing](https://code.claude.com/docs/en/sandboxing) [Model configuration](https://code.claude.com/docs/en/model-config)\
\
Ctrl+I\
\
Assistant\
\
Responses are generated using AI and may contain mistakes.