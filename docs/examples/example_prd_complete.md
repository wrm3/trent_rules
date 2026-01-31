# Example PRD: Task Management Web Application

**This is a complete, real-world example of a PRD created using the trent planning system.**

---

# PRD: Task Management Web Application

## 1. Product overview

### 1.1 Document title and version
- PRD: Task Management Web Application
- Version: 1.0

### 1.2 Product summary

A web-based task management application designed for small teams (2-10 users) to organize, track, and collaborate on projects. The application provides a simple, intuitive interface for creating tasks, assigning them to team members, tracking progress, and managing deadlines. Built with React frontend and Python Flask backend, using PostgreSQL for data persistence.

The application focuses on simplicity and ease of use, avoiding complex project management features in favor of core task tracking functionality that teams can adopt immediately without extensive training.

## 2. Goals

### 2.1 Business goals
- Provide a lightweight alternative to complex project management tools
- Enable small teams to track work without overhead
- Create a foundation for potential future feature expansion
- Maintain low maintenance burden

### 2.2 User goals
- Quickly create and organize tasks
- Assign tasks to team members
- Track task progress and completion
- Set and view deadlines
- Filter and search tasks
- View task history

### 2.3 Non-goals
- Complex project hierarchies (no sub-projects)
- Time tracking or billing features
- Gantt charts or advanced visualizations
- Mobile native apps (web-responsive only)
- Real-time collaboration (page refresh required)
- Integration with external tools (v1.0)

## 3. User personas

### 3.1 Key user types
- Team members (primary users)
- Team leads (task creators and assigners)
- Project managers (progress viewers)

### 3.2 Basic persona details
- **Team Member**: Individual contributor who creates and completes tasks assigned to them
- **Team Lead**: Creates tasks, assigns to team members, monitors progress
- **Project Manager**: Views overall project status, generates reports

### 3.3 Role-based access
- **Team Member**: Create own tasks, view assigned tasks, update task status
- **Team Lead**: All team member permissions + assign tasks, view all team tasks
- **Project Manager**: Read-only access to all tasks and reports

## 4. Phases

### 4.1 Project Phases
- **Phase 0: Setup & Infrastructure** (Task IDs: 1-99)
  - Project structure setup
  - Development environment configuration
  - Database schema design
  - Basic authentication system

- **Phase 1: Foundation** (Task IDs: 100-199)
  - User management system
  - Task data model implementation
  - Basic API endpoints
  - Database migrations

- **Phase 2: Core Development** (Task IDs: 200-299)
  - Task creation and editing UI
  - Task list display
  - Task assignment functionality
  - Status tracking

- **Phase 3: Enhancement** (Task IDs: 300-399)
  - Search and filtering
  - Deadline management
  - Basic reporting
  - UI polish

### 4.2 Phase References
- phase0-setup-infrastructure.md
- phase1-foundation.md
- phase2-core-development.md
- phase3-enhancement.md

## 5. User experience

### 5.1 Entry points & first-time user flow
- User navigates to application URL
- Login page (email/password)
- First-time users see welcome screen with quick tutorial
- After login, user sees dashboard with assigned tasks

### 5.2 Core experience
- **Dashboard**: Overview of assigned tasks, recent activity, upcoming deadlines
- **Task List**: Filterable list of all tasks (assigned, created, all)
- **Task Creation**: Simple form with title, description, assignee, due date
- **Task Detail**: View full task details, update status, add comments
- **Task Assignment**: Drag-and-drop or dropdown to assign tasks to team members

### 5.3 Advanced features & edge cases
- Bulk task operations (mark multiple complete)
- Task templates for recurring work
- Export tasks to CSV
- Task dependencies (blocking tasks)
- Task archiving for completed projects

### 5.4 UI/UX highlights
- Clean, minimal design inspired by Todoist and Asana
- Responsive layout for tablet use
- Keyboard shortcuts for power users
- Color-coded priority levels
- Drag-and-drop task reordering

## 6. Narrative

Sarah, a team lead, starts her day by opening the task management application. She quickly reviews her dashboard to see which tasks are due today and which team members need assignments. She creates three new tasks for the current sprint, assigns them to team members based on their expertise, and sets realistic deadlines. Throughout the day, team members update task statuses, and Sarah can see progress in real-time. At the end of the day, she reviews the completed tasks and plans tomorrow's work, feeling confident that nothing is falling through the cracks.

## 7. Success metrics

### 7.1 User-centric metrics
- Task completion rate (target: >80% of tasks completed on time)
- User adoption rate (target: 90% of team using within 2 weeks)
- Average tasks created per user per week (target: 5-10)
- User satisfaction score (target: 4.0/5.0)

### 7.2 Business metrics
- Time saved vs. previous method (target: 2 hours/week per user)
- Reduced missed deadlines (target: 30% reduction)
- Team productivity increase (target: 15% improvement)

### 7.3 Technical metrics
- Page load time (target: <2 seconds)
- API response time (target: <500ms for 95th percentile)
- Uptime (target: 99.5%)
- Error rate (target: <0.1%)

## 8. Technical considerations

### 8.1 Affected subsystems
- **Primary subsystems** (directly modified/extended):
  - **Frontend (React)**: Task UI components, state management, routing
  - **Backend (Flask)**: Task API endpoints, authentication, business logic
  - **Database (PostgreSQL)**: Task schema, user schema, relationships

- **Secondary subsystems** (indirectly affected):
  - **Authentication System**: User roles and permissions
  - **Email System**: Task assignment notifications (future)

### 8.2 Integration points
- User authentication service (existing)
- Email service for notifications (future)
- File storage for task attachments (future)

### 8.3 Data storage & privacy
- User data stored in PostgreSQL with encryption at rest
- Task data associated with user accounts
- No PII beyond email addresses
- GDPR-compliant data deletion on user request
- Regular backups (daily)

### 8.4 Scalability & performance
- Expected load: 10-50 concurrent users
- Database: PostgreSQL with connection pooling
- Frontend: React with code splitting for performance
- Caching: Redis for frequently accessed data (future)
- CDN: Static assets served via CDN

### 8.5 Potential challenges
- Real-time updates without WebSockets (page refresh required)
- Complex task dependencies may need graph database (future)
- Search performance with large task volumes
- Mobile responsiveness on small screens

## 9. Milestones & sequencing

### 9.1 Project estimate
- **Medium**: 6-8 weeks for full implementation
- Team: 2 developers (1 frontend, 1 backend)

### 9.2 Team size & composition
- Small Team: 2 people (1 Frontend Developer, 1 Backend Developer)
- Part-time Project Manager for requirements and testing

### 9.3 Suggested phases
- **Phase 0: Setup & Infrastructure** (1 week)
  - Key deliverables: Project structure, database schema, authentication
- **Phase 1: Foundation** (2 weeks)
  - Key deliverables: User management, task data model, basic API
- **Phase 2: Core Development** (3 weeks)
  - Key deliverables: Task UI, assignment, status tracking
- **Phase 3: Enhancement** (2 weeks)
  - Key deliverables: Search, filtering, reporting, polish

## 10. User stories

### 10.1 Create Task
- **ID**: US-001
- **Description**: As a team lead, I want to create a new task with title, description, and assignee so that I can delegate work to team members.
- **Acceptance Criteria**:
  - Task creation form has required fields (title, description, assignee)
  - Form validates required fields before submission
  - Created task appears in task list immediately
  - Task creator receives confirmation message

### 10.2 Assign Task
- **ID**: US-002
- **Description**: As a team lead, I want to assign tasks to team members so that work is distributed appropriately.
- **Acceptance Criteria**:
  - Task detail page shows assignee dropdown with team members
  - Assignee can be changed after task creation
  - Assigned user receives notification (email or in-app)
  - Task appears in assignee's task list

### 10.3 Update Task Status
- **ID**: US-003
- **Description**: As a team member, I want to update my task status so that others can see my progress.
- **Acceptance Criteria**:
  - Task detail page shows status dropdown (Pending, In Progress, Completed)
  - Status change is saved immediately
  - Status change is visible to all users with access
  - Completed tasks are moved to completed section

### 10.4 View Task List
- **ID**: US-004
- **Description**: As a user, I want to view a list of tasks so that I can see what needs to be done.
- **Acceptance Criteria**:
  - Task list shows all accessible tasks
  - Tasks can be filtered by status, assignee, or date
  - Tasks are sorted by due date (soonest first)
  - Task list updates when tasks are modified

### 10.5 Search Tasks
- **ID**: US-005
- **Description**: As a user, I want to search for tasks by keyword so that I can quickly find specific tasks.
- **Acceptance Criteria**:
  - Search box is available on task list page
  - Search matches task titles and descriptions
  - Search results highlight matching text
  - Search works across all accessible tasks

---

**This PRD was generated using the trent planning system and demonstrates the 10-section template in action.**
