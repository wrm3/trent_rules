# Platform Architecture Overview

**trent** - Cursor IDE Development System

This document provides an overview of platform-specific considerations for maintaining and extending the trent system.

## Supported Platform

- **Cursor IDE** - Primary platform with full feature support

## Platform-Specific Documentation

- **PLATFORM_COMPARISON.md** - Feature details and capabilities
- **CURSOR.md** - Cursor-specific architecture and features

## Maintenance Schedule

**Quarterly Review** (Every 3 Months):
- [ ] Check official Cursor documentation for updates
- [ ] Test template functionality
- [ ] Update platform-specific documentation
- [ ] Document any breaking changes

## Quick Reference

### File Formats
- **Rules**: `.mdc` files (Markdown Cursor) - Required for Cursor
- **Task Files**: `.md` with YAML frontmatter

### Commands
- **Cursor**: `@trent-*` (e.g., `@trent-task-new`)

### Skills & Agents
- **Cursor**: ✅ Full Skills and SubAgents support (2026+)

## When to Update This Documentation

Update platform architecture docs when:
1. Adding new platform-specific features
2. Discovering platform compatibility issues
3. Official Cursor documentation changes
4. Breaking changes in Cursor APIs

## Resources

- **Official Cursor Docs**: https://docs.cursor.com
- **Last Updated**: 2026-01-29
