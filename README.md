# trent

## Task Management System for Cursor IDE

**AI-powered task management that just works.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)](https://github.com/wrm3/trent)

> A streamlined task management system designed specifically for **Cursor IDE**, enabling developers to manage projects with AI assistance.

---

## 🎯 What is trent?

**trent** is a file-based task management system designed specifically for AI-powered coding environments. It provides:

- ✅ **Git-friendly** - Standard markdown files, easy merging
- ✅ **AI-native** - Built for natural language interaction
- ✅ **25+ Skills** - Database, DevOps, research, and more
- ✅ **18+ Agents** - Specialized agents for different roles

### How It Works

```
┌──────────────────────────────────────────────────────┐
│           .trent/ (Task Data)              │
│  ├── PLAN.md        (Product Requirements)          │
│  ├── TASKS.md       (Master task list)              │
│  ├── BUGS.md        (Bug tracking)                  │
│  └── tasks/         (Individual task files)         │
└──────────────────────────────────────────────────────┘
                           ▲
                           │
                    ┌──────▼──────┐
                    │   Cursor    │
                    │    IDE      │
                    │  .cursor/   │
                    │   rules/    │
                    │   skills/   │
                    │   agents/   │
                    └─────────────┘
```

---

## ⚡ Quick Start

1. Copy the `.cursor/` and `.trent/` folders to your project
2. Start using natural language: "Create a new task for implementing authentication"
3. Use commands: `@trent-setup`, `@trent-plan`, `@trent-task-new`

---

## 📁 Project Structure

```
.trent/              # Core task management (shared data)
├── PLAN.md                    # Product Requirements Document
├── TASKS.md                   # Master task checklist with status
├── BUGS.md                    # Bug tracking
├── PROJECT_CONTEXT.md         # Project mission and goals
├── SUBSYSTEMS.md              # Component registry
├── tasks/                     # Individual task files
└── templates/                 # Task/plan templates

.cursor/                       # Cursor IDE configuration
├── skills/                    # AI Skills for task management
│   ├── trent-task-management/
│   ├── trent-planning/
│   ├── trent-qa/
│   └── trent-code-reviewer/
├── agents/                    # Specialized agents
│   ├── backend-developer.md
│   ├── frontend-developer.md
│   ├── database-expert.md
│   └── ... (18+ more)
├── rules/                     # Rule files (.mdc)
└── commands/                  # Cursor commands
```

---

## 🚀 Features

### Task Management
- ✅ Create, update, and track tasks
- ✅ Task status management (Pending, In Progress, Completed)
- ✅ Priority levels (Critical, High, Medium, Low)
- ✅ Task dependencies and sub-tasks
- ✅ Automatic task expansion for complex work

### Project Planning
- ✅ Product Requirements Documents (PRD)
- ✅ Feature specifications
- ✅ User stories and acceptance criteria
- ✅ Project context and scope management

### Bug Tracking
- ✅ Centralized bug tracking
- ✅ Severity classification
- ✅ Bug-to-task relationships
- ✅ Resolution tracking

---

## 📦 What's Included

### Specialized Agents

| Agent | Description |
|-------|-------------|
| `backend-developer` | API design, server logic |
| `frontend-developer` | React, TypeScript, UI |
| `database-expert` | Schema design, queries |
| `devops-engineer` | CI/CD, infrastructure |
| `docker-specialist` | Containerization |
| `kubernetes-specialist` | K8s management |
| `security-auditor` | Security reviews |
| `code-reviewer` | Code quality |
| ... and 10+ more! |

### Unified Commands

| Command | Description |
|---------|-------------|
| `trent-setup` | Initialize trent system |
| `trent-plan` | Create PRD and project planning |
| `trent-workflow` | Task expansion, sprint planning |
| `trent-qa` | Quality assurance activation |
| `trent-status` | Project status overview |
| `trent-new-task` | Create a new task |
| `trent-update-task` | Update task status |
| `trent-report-bug` | Report/document a bug |
| `trent-fix-bug` | Fix a reported bug |
| `trent-review` | Comprehensive code review |
| `trent-git-commit` | Create well-structured commits |

**Usage:** `@trent-setup`, `@trent-task-new`, etc.

---

## 🤝 Team Collaboration

### Git Workflow

```bash
# Initial setup
git add .trent/ .cursor/
git commit -m "Add trent system"
git push

# Daily workflow
git pull                              # Get latest changes
# Work on tasks in Cursor
git add .trent/             # Stage task changes
git commit -m "Update tasks"
git push
```

---

## 📚 Documentation

- **[agents.md](agents.md)** - Complete agent and skill documentation
- **[docs/](docs/)** - Additional documentation

---

## 💡 Use Cases

### Solo Developer
Install in all projects. All planning stays consistent across projects.

### Small Team
Everyone uses Cursor with the same configuration. All work tracked in shared `.trent/` files.

---

## 🔧 Installation

### Prerequisites
- Git
- Cursor IDE

### Option 1: Copy to Existing Project

```bash
# Navigate to your project
cd my-existing-project

# Copy interfaces
cp -r /path/to/trent/.cursor .
cp -r /path/to/trent/.trent .

# Start using!
```

### Option 2: Use as Template

```bash
# Clone this repository
git clone https://github.com/wrm3/trent.git

# Copy to your project
cp -r trent/.cursor trent/.trent my-project/
```

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

## 🚀 Get Started Now

```bash
# Copy to your project
cp -r .cursor .trent your-project/

# Open in Cursor and start managing tasks!
```

**Questions?** Check the [documentation](docs/) or open an issue.

---

<div align="center">

**Made for developers who value simplicity and flexibility**

[Documentation](docs/) • [agents.md](agents.md)

</div>
