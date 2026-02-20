---
description: "Integration points, template maintenance, and platform architecture reference"
activation: "always_on"
---

## Integration Points

### Task System Integration
- Automatically record metrics during task lifecycle events
- Track effort estimation accuracy for continuous improvement
- Monitor task pipeline health and bottlenecks

### File System Integration
- Use FILE_REGISTRY.md to understand current system structure
- Map file organization to component architecture
- Identify component boundaries from directory structure

### Tool System Integration
- Reference MCP_TOOLS_INVENTORY.md for available tools
- Use tool combinations for comprehensive workflows
- Validate tool selection against task requirements

## Template Maintenance and Platform Architecture

### Platform Architecture Reference

When maintaining this template or adding new features, **ALWAYS** consult the `.trent/` folder for platform-specific requirements and compatibility considerations.

**Key Documentation:**
- `.trent/PLATFORM_COMPARISON.md` - Cross-platform comparison table
- `.trent/CURSOR.md` - Cursor specific architecture
- `.trent/PLATFORM_ARCHITECTURE.md` - Overview and maintenance schedule

### When to Reference Platform Architecture

**ALWAYS check `.trent/` platform documentation before:**
1. Adding new rules or commands
2. Modifying task file formats or naming conventions
3. Creating new instructions or documentation
4. Updating file organization structure
5. Making changes that affect cross-IDE compatibility

### Critical Platform Differences

**File Formats (IMPORTANT):**
- Cursor: Uses `.mdc` for rules files (Markdown Cursor) - UNIQUE to Cursor
- Other platforms: Use `.md` files
- Task files: Use `.md` with YAML frontmatter (cross-platform compatible)

**Platform-Specific Features:**
- Cursor: Now Has Skills and SubAgents (no equivalent in Cursor)
- Cursor: Uses `.mdc` rule format (other platforms can't read these)
- Commands: Cursor uses `@command`, not `/command`

**Universal Features (work everywhere):**
- `.trent/` task management system
- YAML frontmatter in task files
- Markdown documentation
- Standard file organization
- Task status indicators ([ ], [�], [�], [✅])

### Periodic Verification

**Quarterly Review (Every 3 Months):**
- [ ] Check Cursor official documentation for updates
- [ ] Check other platform documentation for new features
- [ ] Test template on multiple platforms
- [ ] Update `.trent/` platform documentation
- [ ] Update PLATFORM_COMPARISON.md if differences found
- [ ] Document any breaking changes

### Adding Features Cross-Platform

When adding features to this template, ensure compatibility:

1. **Test on multiple platforms**: Test thoroughly
2. **Document compatibility**: Update `.trent/CURSOR.md` and other platform docs
3. **Provide fallbacks**: For features that don't work on all platforms
4. **Update comparison table**: Add new features to PLATFORM_COMPARISON.md
5. **Migration guides**: Update if file structure or format changes

### Template Maintenance Workflow

When maintaining this template:

1. **Check platform docs** in `.trent/`
2. **Identify compatibility requirements** from PLATFORM_COMPARISON.md
3. **Make Cursor-specific changes** in `.cursor/rules/*.mdc` files
4. **Update platform documentation** in `.trent/CURSOR.md`
5. **Update comparison table** if new differences emerge

### File Format Rules for Cursor

**Cursor Rules (.mdc files):**
- MUST use `.mdc` extension (not `.md`)
- Located in `.cursor/rules/` directory
- Can be in subdirectories (e.g., `.cursor/rules/trent/`)
- Include YAML frontmatter with `description`, `globs`, `alwaysApply`

**Cursor Commands:**
- Located in `.cursor/rules/*/commands/` directories
- Use `@command` prefix (not `/command`)
- Can reference rules and other commands

### Resources

- **Platform Comparison**: `.trent/PLATFORM_COMPARISON.md`
- **Cursor Architecture**: `.trent/CURSOR.md`
- **Official Cursor Docs**: https://docs.cursor.com
- **Platform Architecture Overview**: `.trent/PLATFORM_ARCHITECTURE.md`

---

*This consolidated rule provides all essential trent functionality in a single, efficient rule optimized for daily coding work.*