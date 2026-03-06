# Claude Code CLI Quick Reference

Claude Code CLI (`claude` command) -- terminal AI coding. Docs: https://docs.anthropic.com/en/docs/claude-code

## Commands
```bash
claude                             # Interactive session
claude "prompt"                    # With initial prompt
claude -p "prompt"                 # Non-interactive (headless/CI)
claude -c                          # Continue last conversation
claude -r "session-id"             # Resume specific session
claude --model opus                # Choose model
claude mcp add|remove|list         # Manage MCP servers
```

## Permission Flags
- `--dangerously-skip-permissions` -- auto-approve ALL tools (requires `--allowedTools` or isolation)
- `--permission-mode plan|acceptEdits|bypassPermissions` -- permission level
- `--allowedTools "Bash(npm *)" "Read" "Edit"` -- pre-authorize specific tools
- `--disallowedTools "Bash(rm *)"` -- block specific tools

## Key Flags
- `--output-format text|json|stream-json` -- output format (with `-p`)
- `--append-system-prompt "..."` -- add instructions (preserves defaults)
- `--max-turns N` -- limit agentic turns
- `--max-budget-usd N` -- spending cap
- `-w name` -- start in isolated git worktree

## Multi-Agent
- `--agents '{"agents":[...]}'` -- define subagents via JSON
- File-based agents: `.claude/agents/*.md`
- Parallel via worktrees: `claude -w agent1 -p "task A"` & `claude -w agent2 -p "task B"`

## Agent SDK
- Python: `pip install claude-agent-sdk`
- TypeScript: `npm install @anthropic-ai/claude-agent-sdk`

## Windows Note
Use `;` not `&&` for chaining. Set UTF-8 encoding before running.
