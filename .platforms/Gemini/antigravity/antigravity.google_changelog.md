![Google Antigravity Blinking Cursor](https://antigravity.google/assets/image/antigravity-cursor.png)

G

o

o

g

l

e

A

n

t

i

g

r

a

v

i

t

y

C

h

a

n

g

e

l

o

g

[View docs](https://antigravity.google/docs)[Follow us on X](https://x.com/antigravity)

info

New versions are rolled out gradually and may take a few days to reach all users.

Version

Description

* * *

1.20.4

Mar 6, 2026

### Stability and UI improvements

Stability and UI improvements.

Improvements (3)

- Added support for reading rules from AGENTS.md in addition to GEMINI.md.
- Deprecated the Auto-continue setting, which is now enabled by default.
- Improved conversation load times, especially for long conversations.

Fixes (3)

- Fixed color contrast in Agent Manager terminals.
- Fixed an issue with cleaning up old SSH server instances.
- Fixed a bug in token accounting that could cause conversations to prematurely reach the maximum token limit.

Patches (1)

- Removed Command support.

1.19.6

Feb 26, 2026

### Account Remediation Pathway

Introduced a formal remediation process for accounts suspended due to Terms of Service violations. See our [official announcement](https://x.com/antigravity/status/2027435365275967591).

Improvements (1)

- Account remediation UI for suspended users.

Fixes (1)

Patches (1)

1.19.5

Feb 26, 2026

### Browser Fix

Stability and UI improvements.

Improvements (0)

Fixes (1)

- Fixed an issue from 1.19.4 that prevented the browser from launching.

Patches (0)

1.19.4

Feb 25, 2026

### Stability and UI Improvements

Stability and UI improvements.

Improvements (2)

- Allow users to include screenshots in feedback reports.
- Nano Banana Pro 2 availability.

Fixes (0)

Patches (0)

1.18.4

Feb 21, 2026

### Fix for Windows Auto-updater

Bug fixes and stability improvements.

Improvements (0)

Fixes (1)

- Fixed an issue where the Windows auto-updater fails to detect new releases. Please manually install the latest update if you are on version 1.16.5 or 1.18.3.

Patches (0)

1.18.3

Feb 19, 2026

### Settings, Artifacts, and Stability

New settings screens for models and terminal integration, artifact download support, and various stability and UI fixes across platforms.

Improvements (6)

- Gemini 3.1 Pro availability.
- Added Models screen to settings, providing more visibility into quota usage.
- Added a setting to enable or disable terminal integration.
- Support for downloading artifacts from the chat UI.
- Up/down arrow key navigation for input box history.
- Improved UI responsiveness for chat interactions, including creating conversations, sending messages, and reverting changes.

Fixes (3)

- Resolved an issue where external plugins could fail to load on macOS due to signing problems.
- Fixed certain artifact files not being recognized as artifacts and missing the 'Proceed' button in the chat UI on Windows.
- Fixed an issue where reverting could occasionally delete files edited by the agent.

Patches (0)

1.16.5

Feb 3, 2026

### Bug Fixes

Various bug fixes and performance improvements.

Improvements (1)

- Speed up population of @-mention search results in the Agent Manager

Fixes (0)

Patches (1)

- Renamed Secure Mode to strict mode

1.15.8

Jan 24, 2026

### Performance Improvements

Performance improvements for long conversations.

Improvements (0)

Fixes (0)

Patches (1)

- Fixes a bug with long conversations with the agent that caused performance issues.

1.15.6

Jan 23, 2026

### Terminal Sandboxing

MacOS users can now execute agent terminal commands within [a sandbox](https://antigravity.google/docs/sandbox-mode) to prevent damage to files outside the workspace.

Improvements (1)

- Terminal commands can now be executed within a sandbox for MacOS users.

Fixes (0)

Patches (0)

1.14.2

Jan 13, 2026

### Agent Skills

Introducing agent skills to Antigravity for enhanced customizability, alongside tab model updates and new conversation settings.

Improvements (3)

- Agent Skills now available in Antigravity
- Updated tab model architecture.
- New Settings to allow disabling conversation history and knowledge.

Fixes (2)

- Resolved transparency issues across various UI components.
- Corrected overactive jump-to-bottom and autoscroll behavior in the chat client.

Patches (0)

1.13.3

Dec 19, 2025

### Google Workspace Support

Higher, more frequently refreshed rate limits for Google Workspace AI Ultra for Business subscribers.

Improvements (1)

- Higher, more frequently refreshed rate limits for Google Workspace AI Ultra for Business subscribers.

Fixes (0)

Patches (0)

1.12.4

Dec 17, 2025

### Gemini 3 Flash

Support for Gemini 3 Flash in Antigravity.

Improvements (3)

- Support for Gemini 3 Flash.
- Native audio support for the agent.
- Performance improvements for Agent Manager and for long conversations in editor windows.

Fixes (0)

Patches (1)

- Switched default browser use model to Gemini 3 Flash.

1.11.17

Dec 8, 2025

### Secure Mode and Security Fixes

Adding the [secure mode](https://antigravity.google/docs/secure-mode) option, which enforces certain settings to prevent the agent from autonomously running targeted exploits and requires human review for all agent actions. Various security fixes.

Improvements (1)

- Secure mode option.

Fixes (1)

- Various security fixes.

Patches (0)

1.11.14

Dec 4, 2025

### Google One Support

Higher, more frequently refreshed rate limits for Google AI Pro and Ultra subscribers.

Improvements (1)

- Google One integration.

Fixes (0)

Patches (0)

1.11.9

Nov 26, 2025

### Stability and Bug Fixes

Bug fixes in the authentication flow.

Improvements (1)

- Added better error states for onboarding users during authentication flow.

Fixes (0)

Patches (0)

1.11.5

Nov 20, 2025

### Nano Banana Pro

With Nano Banana Pro, our agents have gotten even better at generating UI mockups, system diagrams, or relevant embeddable assets, all grounded in your existing codebase and knowledge.

Improvements (1)

- Nano Banana Pro (incrementally rolling out)

Fixes (1)

- Agent can now create scratch directories if no workspaces are open.

Patches (1)

- Fixed an issue with the telemetry settings toggle on the settings page.

1.11.3

Nov 18, 2025

### Launch Day Feedback

Fast hotfixes to address day one issues.

Improvements (0)

Fixes (1)

- Support for individuals with non-Latin alphabetic characters in their names.

Patches (1)

- Messaging to distinguish particular users hitting their user quota limit from all users hitting the global capacity limits.

1.11.2

Nov 18, 2025

### Google Antigravity

The original launch of Google Antigravity, with a fully-featured AI-powered IDE, new Agent Manager view, an integrated experience with Chrome, broad variety of rich Artifacts, user feedback flows, knowledge management, and much more. The vision for what development looks like in an agent-first paradigm.

Improvements (1)

- Google Antigravity

Fixes (0)

Patches (0)