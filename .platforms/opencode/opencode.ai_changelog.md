[![OpenCode](data:image/svg+xml,%3csvg%20width='234'%20height='42'%20viewBox='0%200%20234%2042'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M18%2030H6V18H18V30Z'%20fill='%23CFCECD'/%3e%3cpath%20d='M18%2012H6V30H18V12ZM24%2036H0V6H24V36Z'%20fill='%23656363'/%3e%3cpath%20d='M48%2030H36V18H48V30Z'%20fill='%23CFCECD'/%3e%3cpath%20d='M36%2030H48V12H36V30ZM54%2036H36V42H30V6H54V36Z'%20fill='%23656363'/%3e%3cpath%20d='M84%2024V30H66V24H84Z'%20fill='%23CFCECD'/%3e%3cpath%20d='M84%2024H66V30H84V36H60V6H84V24ZM66%2018H78V12H66V18Z'%20fill='%23656363'/%3e%3cpath%20d='M108%2036H96V18H108V36Z'%20fill='%23CFCECD'/%3e%3cpath%20d='M108%2012H96V36H90V6H108V12ZM114%2036H108V12H114V36Z'%20fill='%23656363'/%3e%3cpath%20d='M144%2030H126V18H144V30Z'%20fill='%23CFCECD'/%3e%3cpath%20d='M144%2012H126V30H144V36H120V6H144V12Z'%20fill='%23211E1E'/%3e%3cpath%20d='M168%2030H156V18H168V30Z'%20fill='%23CFCECD'/%3e%3cpath%20d='M168%2012H156V30H168V12ZM174%2036H150V6H174V36Z'%20fill='%23211E1E'/%3e%3cpath%20d='M198%2030H186V18H198V30Z'%20fill='%23CFCECD'/%3e%3cpath%20d='M198%2012H186V30H198V12ZM204%2036H180V6H198V0H204V36Z'%20fill='%23211E1E'/%3e%3cpath%20d='M234%2024V30H216V24H234Z'%20fill='%23CFCECD'/%3e%3cpath%20d='M216%2012V18H228V12H216ZM234%2024H216V30H234V36H210V6H234V24Z'%20fill='%23211E1E'/%3e%3c/svg%3e)![OpenCode](data:image/svg+xml,%3csvg%20width='234'%20height='42'%20viewBox='0%200%20234%2042'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M18%2030H6V18H18V30Z'%20fill='%234B4646'/%3e%3cpath%20d='M18%2012H6V30H18V12ZM24%2036H0V6H24V36Z'%20fill='%23B7B1B1'/%3e%3cpath%20d='M48%2030H36V18H48V30Z'%20fill='%234B4646'/%3e%3cpath%20d='M36%2030H48V12H36V30ZM54%2036H36V42H30V6H54V36Z'%20fill='%23B7B1B1'/%3e%3cpath%20d='M84%2024V30H66V24H84Z'%20fill='%234B4646'/%3e%3cpath%20d='M84%2024H66V30H84V36H60V6H84V24ZM66%2018H78V12H66V18Z'%20fill='%23B7B1B1'/%3e%3cpath%20d='M108%2036H96V18H108V36Z'%20fill='%234B4646'/%3e%3cpath%20d='M108%2012H96V36H90V6H108V12ZM114%2036H108V12H114V36Z'%20fill='%23B7B1B1'/%3e%3cpath%20d='M144%2030H126V18H144V30Z'%20fill='%234B4646'/%3e%3cpath%20d='M144%2012H126V30H144V36H120V6H144V12Z'%20fill='%23F1ECEC'/%3e%3cpath%20d='M168%2030H156V18H168V30Z'%20fill='%234B4646'/%3e%3cpath%20d='M168%2012H156V30H168V12ZM174%2036H150V6H174V36Z'%20fill='%23F1ECEC'/%3e%3cpath%20d='M198%2030H186V18H198V30Z'%20fill='%234B4646'/%3e%3cpath%20d='M198%2012H186V30H198V12ZM204%2036H180V6H198V0H204V36Z'%20fill='%23F1ECEC'/%3e%3cpath%20d='M234%2024V30H216V24H234Z'%20fill='%234B4646'/%3e%3cpath%20d='M216%2012V18H228V12H216ZM234%2024H216V30H234V36H210V6H234V24Z'%20fill='%23F1ECEC'/%3e%3c/svg%3e)](https://opencode.ai/)

# Changelog

New updates and improvements to OpenCode

### Core

- Canonicalize current working directory after changing directories in TUI
- Fix broken MCP toggling in TUI [(@natewill)](https://github.com/natewill)
- Update database path test to verify correct channel-based filename
- Allow beta channel to share database with stable channel
- Add OPENCODE\_SKIP\_MIGRATIONS flag to bypass database migrations

### TUI

- Guard TUI exit to prevent premature termination
- Avoid TTY corruption from double cleanup [(@tobwen)](https://github.com/tobwen)

### Desktop

- Fix sidebar background color when collapsed
- Suppress hover when opening project menu or right-clicking to prevent flickering
- Trim retained desktop terminal buffers
- Messages not loading reliably
- Prune and evict stale app session caches
- Restore new-session logo on dev so users recognize OpenCode immediately
- Revert new session logo on dev branch to ship UI change with auto-accept-permissions feature
- Add OpenCode logo to new session screen for immediate app identification
- Revert prompt control docking in TUI
- Dock auto-accept after thinking and move Add file to bottom-left
- Balance titlebar columns so center content doesn't get squeezed by long side content
- Center empty states vertically in session view and improve review panel messaging for projects without version control
- Review panel transition fixed in app

### Core

- Preserve original line endings in edit tool [(@ranqn)](https://github.com/ranqn)
- Fix Git path resolution for modified files across Git Bash, MSYS2, and Cygwin on Windows
- Fix PTY session handle leak [(@kikuchan)](https://github.com/kikuchan)
- Sanitize preview database filenames
- Log stack trace when schema validation fails
- I need to see the actual commit diff to understand what was fixed and provide an accurate changelog entry.
- Add project git init API
- Update Drizzle and channel database handling
- Speed up share loads
- Enable auto-accept keybind regardless of permission config [(@luisfelipesena)](https://github.com/luisfelipesena)

### TUI

- Fix broken /export toggling in TUI [(@natewill)](https://github.com/natewill)

### Desktop

- Guard session-header current() against undefined when options is empty [(@cyberprophet)](https://github.com/cyberprophet)
- Preserve file tree tab on reopen and fix e2e test regressions [(@neriousy)](https://github.com/neriousy)
- Remove close button from project hover popover
- New session uses agent model/variant
- Model sticks to session after being changed
- Based on the commit message "fix(app): all panels transition", here's the changelog entry:
- Can't scroll files in app
- Fix maximum width on timeline component
- Align session empty states in TUI
- Add interactive timeline visualization feature
- Share workspace slug wait helper across e2e specs
- Abort sessions and wait for idle before e2e cleanup
- Show skill issue when snapshotting is off in desktop app
- Fix portal positioning for sidebar menus and tooltips by removing conditional mount logic
- Add end-to-end tests for app (part 67) [(@neriousy)](https://github.com/neriousy)
- Add sidebar reveal animation, hover peek overlay, and weaker dividers to app
- Better review and file tree empty states
- Enable Safari autocorrect in normal mode, disable in shell mode [(@alexandrereyes)](https://github.com/alexandrereyes)
- Revert stale read error fix in app
- Add English to locale matchers [(@KirillTregubov)](https://github.com/KirillTregubov)

### Core

- Stop leaking fsmonitor daemons that caused 60GB+ of committed memory after running tests
- Replace Bun.which with npm which in OpenCode

### TUI

- Restore Bun stdin reads for prompt input

### Core

- Add GPT-5.4 to Codex allowed models list [(@msadiks)](https://github.com/msadiks)
- Replace Bun.stderr and Bun.color with Node.js equivalents
- Replace Bun.connect with net.createConnection for better compatibility
- Use SHA1 for hash instead of unsupported xxHash3-XXH64
- Replace Bun.hash with Hash.fast using xxhash3-xxh64
- Replace Bun.write with Filesystem.write in config files
- Replace Bun.write/file with Filesystem utilities in snapshot
- Replace Bun.sleep with Node.js timers for better compatibility

### TUI

- Use node:stream/consumers for stdin reading
- Replace Bun.stdin.text with Node.js stream reading for better compatibility

### Desktop

- Fix stale show in app [(@neriousy)](https://github.com/neriousy)
- Remove keyboard shortcut tooltips from new session and new workspace buttons in the sidebar
- Load tab when opening file

### Core

- Handle SIGHUP signal and kill process gracefully

### TUI

- Add onClick handler to InlineTool and Task components
- Add options to auth login command to skip interactive questions [(@dbpolito)](https://github.com/dbpolito)
- Don't let Dax touch the UI

### Desktop

- Fork Ghostty for web-based terminal implementation
- Show errors for stale keyed components
- Fixed locale error in app
- Resolve stale read error in app
- Improve provider settings consistency in app
- Preserve question dock state across session switches [(@ualtinok)](https://github.com/ualtinok)
- Fix icon jiggle in app
- Open search with Mod+F even when editor is not focused
- Improve error handling and translation in desktop server error formatting [(@OpeOginni)](https://github.com/OpeOginni)
- Improve agent selection logic to correctly pass configured models and variants [(@OpeOginni)](https://github.com/OpeOginni)
- Remove unnecessary macOS entitlements
- Add desktop deep link support for creating new sessions
- Prefer using useLocation hook instead of window.location in app

### SDK

- Update SDK package.json

### Core

- Rework workspace integration and adaptor interface
- Clarify output capture guidance in bash tool documentation

### TUI

- Show scrollbar by default
- Prevent orphaned opencode subprocesses on shutdown
- Validate agent when running with attach flag [(@alberti42)](https://github.com/alberti42)

### Desktop

- Remove blur from todos in app
- Delay dock animation on session load
- Remove diff lines from sessions in sidebar
- Loading session should be scrolled to the bottom
- Close terminal tabs properly

### Core

- Normalize trailing slashes in auth login URLs [(@elithrar)](https://github.com/elithrar)
- Upgrade OpenTUI to v0.1.86 and enable markdown rendering by default
- Avoid Gemini combiner schema sibling injection
- Forward metadata options to Cloudflare AI Gateway provider [(@ryanskidmore)](https://github.com/ryanskidmore)
- Clone part data in Bus event to preserve token values [(@ryanskidmore)](https://github.com/ryanskidmore)
- Recover from 413 Request Entity Too Large errors via automatic compaction [(@bentrd)](https://github.com/bentrd)
- Show human-readable message for HTML error responses [(@rianvdm)](https://github.com/rianvdm)
- Kill orphaned MCP child processes and expose OPENCODE\_PID on shutdown [(@ryanwyler)](https://github.com/ryanwyler)
- Add workspace\_id to session table
- Add WorkspaceContext to core
- Basic implementation of remote workspace support
- Change keybindings to navigate between child sessions
- Fixed test issues
- Fixed terminal rendering and interaction issues in the application

### TUI

- Replace curved arrow with straight arrow for better terminal compatibility
- Show pending tool call count in TUI instead of generic 'Running...' message
- Use arrow indicator for active tool execution in TUI
- Disable session navigation commands when no parent session [(@jerome-benoit)](https://github.com/jerome-benoit)
- Fixed project ID conflict and updated handling for same session ID [(@noamzbr)](https://github.com/noamzbr)
- Improve task tool display with subagent keybind hints and spinner animations
- Add Go provider list command

### Desktop

- Defer diff rendering
- Fixed timeline performance jank in the application
- Tighten up header elements in the app
- Stabilize project close navigation
- Add comprehensive animation system with multiple easing functions and transition utilities
- Default auto-respond to false
- Refactor app to use SolidJS
- Move session review bottom padding to UI layer
- Fix latest.json finalizer in desktop application
- Revert Polish Turkish translations
- Use correct download link in finalize-latest-json script
- Faster session switching via windowed rendering and staged timeline
- Add compact UI to the app [(@neriousy)](https://github.com/neriousy)
- Polish Turkish translations [(@vaur94)](https://github.com/vaur94)
- Fallback to synthetic icon for unknown provider IDs [(@rexdotsh)](https://github.com/rexdotsh)
- Fixed scroll issues in the app
- Synchronize internationalization translations
- Add Warp to the open menu
- Add latest.json finalizer script for desktop builds
- Auto-accept permissions in app
- Add Turkish locale support for app and UI packages [(@vaur94)](https://github.com/vaur94)
- Add recent projects section to command palette [(@neriousy)](https://github.com/neriousy)
- Move desktop open\_path functionality to Rust
- Allow providing username and password when connecting to remote server
- Fixed permission indicator in app
- Add permission notifications to app
- Show keybind on context tab close button
- Better diff and code comments in app
- Deduplicate file tree scroll state management
- Align review changes select height
- Mute inactive file tab icons
- Set max-width on session when review is closed but file tree is open
- Add border to file tree on scroll
- Fix session tab alignment in compact view to prevent vertical overflow
- New tabs styling in the app
- Auto-accept all permissions mode
- Enhance project tile interaction with suppress hover functionality [(@OpeOginni)](https://github.com/OpeOginni)
- Simplify review layout
- Restore shell path environment for desktop sidecar
- Open app in PowerShell instead of Command Prompt on Windows [(@neriousy)](https://github.com/neriousy)

### SDK

- Add zen mode feature

### Core

- Fix most segfaults on Windows with Bun v1.3.10 stable
- Split TUI and server configuration

### Desktop

- Remove interactive shell flag from sidecar spawn to prevent hang on macOS [(@kilhyeonjun)](https://github.com/kilhyeonjun)
- Fixed permissions and questions handling from child sessions in the app
- Fixed keyboard navigation for previous/next message [(@neriousy)](https://github.com/neriousy)
- Correct Copilot provider description in i18n files [(@Oleksii-Pavliuk)](https://github.com/Oleksii-Pavliuk)

### Core

- Add message delete endpoint [(@shantur)](https://github.com/shantur)

### TUI

- Consume stdout concurrently with process exit in auth login [(@Ayushlm10)](https://github.com/Ayushlm10)

### Core

- Synchronize changes
- Temporarily disable plan enter tool to prevent unintended mode switches during task execution
- Migrate Bun.spawn to Process utility with timeout and cleanup
- Disable Bun config cache in CI
- Await git ID cache write in project module
- Import custom tools via file URL

### TUI

- Add Go SDK code generation script
- Show LSP errors for apply\_patch tool

### Desktop

- Enhance Windows app resolution and UI loading states [(@neriousy)](https://github.com/neriousy)
- Update desktop README for accuracy

### Core

- Add workspace-serve command (experimental)
- ACP both live and load share synthetic pending status preceding actual data [(@noamzbr)](https://github.com/noamzbr)
- Replace structuredClone with spread operator for process.env in tests
- Add 50ms tolerance for NTFS mtime precision in Windows FileTime assertions
- Replace Unix-only test assumptions with cross-platform alternatives
- Use path.sep in discovery test for cross-platform path matching
- Normalize backslash paths in config rel() and file ignore on Windows
- Fix plugin resolution with createRequire fallback on Windows
- Harden preload cleanup against Windows EBUSY errors
- Normalize git excludesFile path for Windows in tests
- Stream bash output and add synthetic pending events to ACP [(@noamzbr)](https://github.com/noamzbr)
- Add git flags for snapshot operations and fix tests for cross-platform on Windows
- Handle CRLF line endings in markdown frontmatter parsing on Windows
- Use path.join for cross-platform glob test assertions
- Upgrade to Bun 1.3.10 canary and force baseline builds always
- Normalize paths at permission boundaries on Windows
- Windows path support and canonicalization [(@edemaine)](https://github.com/edemaine)
- Upgrade OpenTUI to v0.1.81
- Change detection on Windows, especially Cygwin [(@edemaine)](https://github.com/edemaine)
- Cache platform binary in postinstall for faster startup
- Revert caching platform binary in postinstall for faster startup
- Cache platform binary in postinstall for faster startup
- Publish desktop beta releases to a separate repository
- Add experimental endpoint to list all sessions
- Fixed terminal issues in the app
- Respect info exclude in snapshot staging
- Missing plugin dependencies cause TUI to black screen [(@elithrar)](https://github.com/elithrar)

### TUI

- Support variant parameter in GitHub Actions and OpenCode GitHub run command [(@elithrar)](https://github.com/elithrar)

### Desktop

- Ignore stale part deltas in the application
- Fix bug where lines remain highlighted after canceling a comment [(@neriousy)](https://github.com/neriousy)
- Replace error handling with serverErrorMessage utility and add ConfigInvalidError checks [(@OpeOginni)](https://github.com/OpeOginni)
- Preserve native path separators in file path helpers
- Remove file tree tooltips
- Update createOpenReviewFile test to match new call order
- Wait for loadFile to complete before opening file tab
- Windows E2E test failures due to IPv6 networking issues resolved
- Correct inverted chevron direction in todo list [(@kevinWangSheng)](https://github.com/kevinWangSheng)
- Feed customization options
- Add beta icon to desktop application
- E2E test updated to current version
- Remove double-border in share button
- Better sound effect disabling UX
- Add custom scroll view to app
- Show and hide reasoning summaries in the app
- Stay pinned with auto-scroll on todos, questions, and permissions
- Bring back -i flag in sidecar arguments for desktop
- Large text pasted into prompt input no longer causes main thread to lock

### SDK

- Scripts using Turbo commands would not run on Windows

### Desktop

- Don't spawn sidecar if default is localhost server

### SDK

- Build SDK to dist/ instead of dist/src

### Core

- Add missing id, sessionID, and messageID to MCP tool attachments [(@NatChung)](https://github.com/NatChung)
- Remove unnecessary deep clones from session loop and LLM stream
- Remove User-Agent header assertion from LLM test to fix failing test

### TUI

- Use structuredClone instead of remeda's clone for better performance and native support [(@mhart)](https://github.com/mhart)

### Desktop

- Restore settings header mask

### Core

- Support adaptive thinking for Claude Sonnet 4.6 [(@tctev)](https://github.com/tctev)

### TUI

- Add custom tool and MCP call responses that are visible and collapsible [(@yanosh-k)](https://github.com/yanosh-k)

### Desktop

- Black screen on launch with sidecar server fixed
- Clear todos on abort

### Core

- Fixed terminal rendering and interaction issues in the application
- Normalize file status paths relative to instance directory [(@shantur)](https://github.com/shantur)
- Migrate from Bun.Glob to npm glob package
- Bump AI SDK packages for Google, Google Vertex, Anthropic, Bedrock, and provider utils
- Add support for medium reasoning with Gemini 3.1
- Remove use of Bun.file
- Text files misclassified as binary
- Fetch default server at top level in desktop application
- Terminal rework in the app
- Bake in the AWS and Google authentication packages
- Token substitution in OPENCODE\_CONFIG\_CONTENT now works correctly [(@ariane-emory)](https://github.com/ariane-emory)
- Revert migration from Bun.file() to Filesystem module
- Migrate project.ts from Bun.file() to Filesystem/stat modules
- Migrate read tool from Bun.file() to Filesystem module
- Migrate write tool from Bun.file() to Filesystem module
- Migrate Edit tool from Bun.file() to Filesystem module
- Migrate remaining tool files from Bun.file() to Filesystem/stat modules
- Migrate storage.ts from Bun.file()/Bun.write() to Filesystem module
- Migrate src/storage/json-migration.ts from Bun.file() to Filesystem module
- Migrate MCP auth module from Bun file APIs to Filesystem module
- Migrate storage database from Bun.file() to statSync for file existence checks
- Migrate session prompt module from Bun.file() to Filesystem/stat modules
- Fix crash in \`opencode run\` and show errored tool calls in output
- Migrate skill discovery to use Filesystem module instead of Bun file APIs
- Migrate session instruction handling from Bun.file() to Filesystem module
- Migrate provider.ts from Bun.file() to Filesystem module
- Migrate shell.ts from Bun.file() to statSync for improved file system operations
- Migrate log utility from Bun.file() to Node.js fs module for better compatibility
- Migrate models.ts from Bun.file()/Bun.write() to Filesystem module
- Use HashiCorp releases API for installing terraform-ls [(@edubxb)](https://github.com/edubxb)
- Migrate LSP server from Bun.file()/Bun.write() to Filesystem module
- Migrate session command from Bun.file() to statSync for improved file system operations
- Migrate agent.ts from Bun.file() to Filesystem module
- Migrate auth module from Bun.file()/Bun.write() to Filesystem module
- Pass sessionID and callID to shell.env hook input [(@tesdal)](https://github.com/tesdal)
- Fix terminal cross-talk issue in the application
- Update SST version
- Migrate src/global/index.ts from Bun.file() to Filesystem module
- Emit PROMPT\_TOO\_LARGE error when GitHub context overflows [(@elithrar)](https://github.com/elithrar)
- Migrate src/bun/index.ts from Bun.file()/Bun.write() to Filesystem module
- Migrate config/markdown.ts from Bun.file() to Filesystem module
- Migrate file/index.ts from Bun.file() to Filesystem module
- Migrate format/formatter.ts from Bun.file() to Filesystem module
- Allow readJson to be called without explicit type parameter
- Migrate file/ripgrep.ts from Bun APIs to Filesystem module
- Migrate index.ts from Bun.file() to Filesystem module
- Add Julia language server support [(@zarly)](https://github.com/zarly)
- Bump GitLab AI provider to 3.6.0 to add Sonnet 4.6 support [(@vglafirov)](https://github.com/vglafirov)
- Add centralized filesystem module for Bun.file migration
- Fix Clojure syntax highlighting [(@finalfantasia)](https://github.com/finalfantasia)
- Ensure explore subagent prompts for external directory permission instead of auto-denying
- Don't autoload kilo
- Add Kilo as a native provider [(@Nomadcxx)](https://github.com/Nomadcxx)
- Simplify redundant ternary in updateMessage [(@yikayiyo)](https://github.com/yikayiyo)
- Ensure Read tool uses fs/promises for all file system operations
- Make read tool more memory efficient
- Surface plugin auth providers in the login picker [(@anoldguy)](https://github.com/anoldguy)
- Invalidate OAuth credentials when OAuth provider indicates they are invalid [(@GreenStage)](https://github.com/GreenStage)
- Don't fetch models.dev on completion [(@gigamonster256)](https://github.com/gigamonster256)
- Recover state after SSE reconnect and harden SSE streams
- Keep message part order stable when files resolve asynchronously
- Drop IDs from attachments in tools and assign them in prompt.ts instead

### TUI

- Improve GitHub action branch detection and handle 422 errors [(@elithrar)](https://github.com/elithrar)
- Ensure onExit callback fires after terminal output is written
- Migrate TUI thread module from Bun.file() to Filesystem module
- Migrate agent command from Bun.file()/Bun.write() to Filesystem module
- Migrate import command from Bun.file() to Filesystem module
- Update pasteImage to only increment count when the previous attachment is an image [(@OpeOginni)](https://github.com/OpeOginni)
- Migrate editor.ts from Bun.file()/Bun.write() to Filesystem module
- Migrate clipboard.ts from Bun.file() to Filesystem module
- Migrate CLI run command from Bun.file() to Filesystem/stat modules
- Session list --max-count parameter now correctly limits the number of sessions displayed [(@mharris717)](https://github.com/mharris717)
- Exit cleanly without hanging after session ends
- Style scrollbox for permission and sidebar [(@akronb)](https://github.com/akronb)
- Increase button heights and improve permission prompt layout alignment
- Display new session banner with logo and project details in TUI

### Desktop

- Update Japanese translations for WSL integration [(@taroj1205)](https://github.com/taroj1205)
- Made localhost URLs work correctly in isLocal function
- Navigate to last session when navigating to a project
- Fix typecheck errors in app
- Deduplicate allServers list in app
- Adjust session turn horizontal padding
- Tighten prompt dock padding in app
- Fixed sidecar spawning a window on Windows
- Delay prompt mode toggle tooltip
- Shorten prompt mode toggle tooltips in the app
- Reduce review panel padding
- Tweak search button style in UI
- Expanded color state on titlebar buttons
- Tweak hover and active styles for title bar buttons
- Share button now has a border
- Adjust file tree background color
- Handle sidecar key in projectsKey for desktop projects
- Fixed desktop app incorrectly identifying local servers
- Refactor server management backend
- Use group-hover for file tree icon color swap at all nesting levels
- Simplify mode toggle icon styling in TUI
- Clean up desktop implementation
- Temporarily disable WSL support in desktop application
- Use radio group in prompt input
- Simplify prompt mode toggle icon colors via CSS and tighten message timeline padding in TUI
- Fix prompt input quirks in app
- Terminal disconnect and resync functionality fixed
- Replicate tauri-plugin-shell logic in desktop application
- Improve modified file visibility and button spacing in TUI
- Show monochrome file icons by default in tree view, revealing colors on hover to reduce visual clutter
- Fix share button text styling to use consistent 12px regular font weight
- Add warning icon to permission requests for better visibility
- Extract dock prompt shell component
- UI no longer flashes when switching tabs [(@neriousy)](https://github.com/neriousy)
- Avoid sidecar health-check timeout on shell startup in desktop app [(@ysm-dev)](https://github.com/ysm-dev)
- Increase prompt mode toggle height for better clickability
- Add more end-to-end tests for desktop application [(@neriousy)](https://github.com/neriousy)
- Update magnifying-glass icon in UI
- Tighten titlebar action padding
- Refine titlebar search and open padding
- Center titlebar search and soften keybind styling
- Align titlebar search text size
- Match titlebar active background to hover
- Use weak borders in titlebar actions
- Reduce titlebar right padding
- Keep file tree toggle visible
- Adjust icon button spacing in UI
- Session timeline and turn handling reworked in app
- Keep Escape handling local to prompt input on macOS desktop [(@itskritix)](https://github.com/itskritix)
- Hide server CLI window on Windows

### SDK

- Fix nested exports transformation in SDK publish script

### Core

- Add dfmt formatter support for D language files [(@burner)](https://github.com/burner)
- Bump GitLab provider and auth plugin for mid-session token refresh [(@vglafirov)](https://github.com/vglafirov)
- Remove unnecessary per-message title LLM calls [(@rmk40)](https://github.com/rmk40)
- Prioritize user-defined variables over environment variables in Google Vertex AI configuration
- Add OpenAI-compatible endpoint support for Google Vertex provider [(@leehack)](https://github.com/leehack)
- Add Venice support for temperature, topP, topK, and smallOption parameters [(@dpuyosa)](https://github.com/dpuyosa)
- Add cljfmt formatter support for Clojure files [(@finalfantasia)](https://github.com/finalfantasia)

### TUI

- Make use of server directory path for file references in prompts [(@OpeOginni)](https://github.com/OpeOginni)
- Add database migration command to convert JSON storage to SQLite
- Add --continue and --fork flags to attach command
- Fixed inaccurate tips in TUI [(@imanolmzd-svg)](https://github.com/imanolmzd-svg)

### Desktop

- Normalize Linux Wayland/X11 backend and decoration policy [(@bnema)](https://github.com/bnema)
- Use process-wrap library instead of manual job object handling in desktop [(@Brendonovich)](https://github.com/Brendonovich)

### Core

- Ensure SQLite migration logs to stderr instead of stdout

### Desktop

- Fixed issue viewing new files opened from the file tree [(@shanebishop1)](https://github.com/shanebishop1)
- Only navigate prompt history at input boundaries [(@nexxeln)](https://github.com/nexxeln)
- Add keyboard shortcut Shift+Tab to the application [(@neriousy)](https://github.com/neriousy)
- Focus window after update and relaunch [(@zerone0x)](https://github.com/zerone0x)
- Add GeistMono Nerd Font to available mono font options [(@brandon-julio-t)](https://github.com/brandon-julio-t)

### Core

- Add db command for database inspection and querying
- Derive all IDs from file paths during JSON migration

### Desktop

- Clear notifications action
- Fixed stack overflow issue in file tree component

### Core

- Ensure Anthropic models on OpenRouter also have variant support
- Add WAL checkpoint on database open
- Ensure Vercel variants pass Amazon models under Bedrock key

©2026 [Anomaly](https://anoma.ly/)[Brand](https://opencode.ai/brand)[Privacy](https://opencode.ai/legal/privacy-policy)[Terms](https://opencode.ai/legal/terms-of-service)

English