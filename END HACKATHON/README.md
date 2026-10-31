# Workforce Management System (WFMS)
### Complete College DBMS Project — Python Flask, SQLite Relational Database, REST API & Modern Web UI

> **Smarter Scheduling. Better Workforce Management.**

---

## 1. Project Overview
The **Workforce Management System (WFMS)** is a full-stack, enterprise-grade web application developed as a comprehensive College Database Management Systems (DBMS) project. It bridges database theory with practical application by implementing relational modeling (up to 3NF), declarative foreign key constraints, atomic transactions, session-based role authentication, constraint-validated shift rostering, employee availability tracking, and administrative leave workflows.

The system features separate **Admin** and **Employee** consoles, live **Chart.js** data visualizations powered directly by backend SQL queries, and a modern, responsive user interface styled with an enterprise palette.

---

## 2. Project Objectives
- Implement a fully normalized relational database (SQLite via SQLAlchemy ORM).
- Enforce business logic integrity: prevent duplicate shift bookings, detect cross-midnight interval overlaps, honor employee unavailabilities, and enforce approved leave exclusions.
- Provide secure session-based authentication with role-based access control (RBAC) and Werkzeug password hashing.
- Provide an intuitive, responsive user experience for both management and workforce personnel.
- Satisfy all academic DBMS Course Outcomes (CO1 through CO6) with verifiable SQL operations and automated tests.

---

## 3. Key Features

### Administrator Console
- **Executive Dashboard**: 6 real-time KPI stat cards and 4 interactive Chart.js visualizations (Department Headcount, Shift Distribution, Leave Statuses, Weekly Schedule Volume).
- **Staff Directory Management**: Add, view, edit, and deactivate employees; filter by branch/department; issue secure temporary passwords.
- **Department & Branch Management**: Maintain organizational branches with live headcount counts and cascade protection.
- **Roster & Shift Models**: Configure working windows with automatic cross-midnight (overnight) detection.
- **Shift Scheduling**: Interactive assignment form with auto-populating employee metadata and comprehensive constraint validation (duplicate checks, overlap checks, leave checks, availability checks).
- **Weekly & Daily Roster Views**: Calendar-style matrix with distinctive color coding for Morning, Evening, and Night shifts.
- **Leave Applications Queue**: Review time-off requests with automated schedule conflict alerts and one-click conflict resolution.
- **Availability Monitoring**: Inspect employee availability declarations prior to roster generation.
- **Reports & Analytics**: Comprehensive metric rollup with printable reports.

### Employee Portal
- **Personalized Workspace**: Real-time summary of upcoming shifts, weekly roster load, and leave statuses.
- **Weekly Shift Calendar**: View assigned shifts with date, day of week, timings, branch, and status.
- **Leave Application**: Apply for leave for a specific shift and date with mandatory justification.
- **Leave Application Tracking**: Monitor status (Pending: Yellow, Approved: Green, Rejected: Red) and view administrator remarks.
- **Availability Declaration**: Register Available or Unavailable dates and optional time windows.
- **Account Security**: Change account password with current credential verification; submit admin-assisted password recovery requests.

---

## 4. Technology Stack
- **Backend**: Python 3.10+ / 3.14, Flask 3.x
- **Database / ORM**: SQLite (`instance/workforce.db`), Flask-SQLAlchemy 3.x, SQLAlchemy 2.x
- **Security & Hashing**: Werkzeug (`generate_password_hash`, `check_password_hash`), Flask Signed Session Cookies
- **Frontend**: Semantic HTML5, Vanilla CSS3 (Custom Design System), Bootstrap 5 (Grid & Modals), Font Awesome 6
- **Data Visualizations**: Chart.js 4.x
- **Automated Testing**: pytest 8.x / 9.x

---

## 5. Directory Structure
```
WorkforceManagementSystem/
│
├── app.py                     # Main application factory & database seeder
├── config.py                  # Configuration profiles (Development & Testing)
├── requirements.txt           # Python package dependencies
├── README.md                  # Comprehensive documentation
├── .gitignore                 # Version control exclusions
│
├── instance/
│   └── workforce.db           # SQLite database (auto-generated on first launch)
│
├── models/                    # Normalized SQLAlchemy ORM Models
│   ├── __init__.py
│   ├── admin.py               # Administrator credentials
│   ├── department.py          # Operational branches
│   ├── employee.py            # Employee profiles
│   ├── shift.py               # Shift templates & overnight flags
│   ├── schedule.py            # Shift assignments & unique constraints
│   ├── availability.py        # Date-based worker availability
│   ├── leave_request.py       # Time-off requests & review states
│   ├── audit_log.py           # Administrative action audit trail
│   └── password_reset.py      # Assisted recovery requests
│
├── routes/                    # Modular Blueprint Controllers
│   ├── __init__.py
│   ├── auth_routes.py         # Login, logout, session guards, password change
│   ├── employee_routes.py     # Employee CRUD, status toggling, reset requests
│   ├── department_routes.py   # Department endpoints & deletion guards
│   ├── shift_routes.py        # Shift endpoints & status toggling
│   ├── schedule_routes.py     # Roster assignment & weekly/daily feeds
│   ├── availability_routes.py # Availability submission & filtering
│   ├── leave_routes.py        # Leave submission & approval workflow
│   └── analytics_routes.py    # Chart.js telemetry & KPI aggregates
│
├── services/                  # Business Logic & Validation Layer
│   ├── __init__.py
│   ├── scheduling_service.py  # Conflict & overlap validation across midnight
│   ├── leave_service.py       # Leave review & schedule auto-resolution
│   └── analytics_service.py   # Database query aggregation
│
├── templates/                 # Jinja2 HTML5 Responsive Templates
│   ├── base.html              # Master layout with sidebar & topbar
│   ├── index.html             # Dual login portal
│   ├── admin_login.html       # Administrator login console
│   ├── employee_login.html    # Staff ID login console
│   ├── admin_dashboard.html   # KPI cards & 4 Chart.js charts
│   ├── employees.html         # Staff management & modals
│   ├── departments.html       # Branch cards & master table
│   ├── shifts.html            # Shift roster templates
│   ├── scheduling.html        # Interactive scheduling console
│   ├── availability.html      # Admin availability inspection
│   ├── leave_requests.html    # Admin leave approval queue
│   ├── reports.html           # Printable executive telemetry
│   ├── password_reset.html    # Assisted recovery workflow
│   ├── employee_dashboard.html# Personalized worker workspace
│   ├── my_shifts.html         # Weekly personal shift roster
│   ├── leave_application.html # Leave application form
│   ├── my_leave_requests.html # Employee leave history & remarks
│   ├── my_availability.html   # Employee availability declaration
│   └── change_password.html   # Self-service password change
│
├── static/                    # Frontend Assets
│   ├── css/
│   │   ├── style.css          # Design system tokens & enterprise theme
│   │   ├── dashboard.css      # Sidebar, topbar, cards, and weekly matrix
│   │   └── responsive.css     # Mobile & tablet viewports
│   └── js/
│       ├── main.js            # Toast notifications, API helper, modal controls
│       ├── scheduling.js      # Employee auto-lookup, date navigation, assignment
│       └── analytics.js       # Live Chart.js data fetchers
│
├── tests/                     # Automated Pytest Suite (29 Unit & Integration Tests)
│   ├── __init__.py
│   ├── conftest.py            # Isolated in-memory test database fixture
│   ├── test_auth.py           # Authentication & session security tests
│   ├── test_employees.py      # Employee CRUD & duplicate rejection tests
│   ├── test_scheduling.py     # Conflict, duplicate, & leave guard tests
│   ├── test_leave_requests.py # Leave review & auto-unassign tests
│   └── test_analytics.py      # KPI & chart telemetry tests
│
└── docs/                      # Course Outcome Documentation
    ├── er_diagram.md          # Conceptual ER diagram & entity dictionary (CO1)
    ├── database_design.md     # Relational schema, 3NF, & 8 SQL proofs (CO1, CO2)
    ├── api_documentation.md   # REST API endpoint reference (CO3, CO4)
    └── project_demonstration.md# 14-step academic evaluation walkthrough (CO6)
```

---

## 6. Quick Start & Installation Instructions

Follow these standard steps in Windows PowerShell or Command Prompt:

### Step 1: Open Project Directory
```powershell
cd "$HOME\Desktop\WorkforceManagementSystem"
```

### Step 2: Create and Activate Virtual Environment
```powershell
python -m venv venv
.\venv\Scripts\activate
```

### Step 3: Install Required Dependencies
```powershell
python -m pip install -r requirements.txt
```

### Step 4: Run the Application
```powershell
python app.py
```

The database (`instance/workforce.db`) is **automatically initialized and seeded** on the first launch. You do **not** need to manually create tables or run SQL scripts.

Open your browser to:
```
http://127.0.0.1:5000
```

---

## 7. Demo Credentials

### Administrator Account
- **Portal**: Click **Admin Login** on the home page or navigate to `/admin/login`
- **Username**: `admin`
- **Password**: `123`

### Pre-Seeded Sample Employee Accounts
All demonstration employees belong to valid departments and have initial password: `emp123`.

| Employee ID | Name | Department | Designation | Password |
| :--- | :--- | :--- | :--- | :--- |
| `EMP001` | Sarah Jenkins | Hospitality | Front Desk Lead | `emp123` |
| `EMP002` | David Chen | Technical Support | Senior Systems Engineer | `emp123` |
| `EMP003` | Priya Sharma | Human Resource | HR Specialist | `emp123` |
| `EMP004` | Marcus Vance | Marketing | Campaign Strategist | `emp123` |
| `EMP005` | Elena Rostova | Management | Operations Supervisor | `emp123` |
| `EMP006` | Alex Turner | Technical Support | Network Analyst | `emp123` |

*Note: The administrator can create additional employees with custom IDs and initial passwords at any time.*

---

## 8. Core Workflows Walkthrough

### 1. Adding a New Employee
1. Log in as `admin` (`123`).
2. Go to **Employees** (`/admin/employees`) and click **Add Employee**.
3. Enter Employee ID (e.g. `EMP007`), Name, select a Branch, enter Designation, and an initial password (e.g. `emp123`).
4. Click **Create Employee**. The employee can immediately log in with these credentials.

### 2. Assigning Shifts (Roster Generation)
1. Go to **Shift Scheduling** (`/admin/scheduling`).
2. Select an employee from the dropdown. Notice their Full Name, Branch, and Designation **auto-populate**.
3. Choose a shift (Morning, Evening, or Night) and a date.
4. Click **Assign Shift**.
5. The system validates:
   - Worker active status
   - Shift active status
   - Duplicate booking prevention
   - Cross-midnight time overlaps
   - Worker availability declarations
   - Approved leave exclusions
6. The assignment immediately renders in the **Weekly Matrix**.

### 3. Leave Application & Approval
1. Log in as an employee (e.g. `EMP001` / `emp123`).
2. Navigate to **Leave Application** (`/employee/leave-application`).
3. Select date, shift, enter reason, and click **Submit Application**.
4. Log out and sign in as `admin`.
5. Navigate to **Leave Requests** (`/admin/leave-requests`).
6. Click **Approve**. If the employee is currently scheduled for that shift, the system alerts the administrator and can automatically unassign the conflicting shift upon approval.

---

## 9. Running Automated Tests

A comprehensive suite of 29 tests executes against an isolated database fixture:

```powershell
# Activate venv if not already active
.\venv\Scripts\activate

# Run pytest
python -m pytest -v
```

All 29 tests validate:
- Admin and Employee authentication, credential checks, and route protection
- Employee creation, duplicate prevention, and profile updates
- Shift scheduling, duplicate prevention, overlap prevention, and leave collision detection
- Leave submissions, duplicate prevention, review decisions, and conflict auto-unassign
- Analytics endpoints and database aggregation

---

## 10. DBMS Course Outcome (CO) Mapping

| Course Outcome | Academic Competency | Project Implementation & Proof Location |
| :--- | :--- | :--- |
| **CO1** | Problem Understanding & Database Design | Relational schema in 3NF, ER diagram in Mermaid, entities, relationships, foreign keys, and constraints. Documented in [`docs/er_diagram.md`](docs/er_diagram.md) and [`docs/database_design.md`](docs/database_design.md). |
| **CO2** | Database Implementation & Operations | SQLite implementation with 8 core SQL queries (Joins, Aggregates, Group By, Subqueries, Cross-Midnight Conflict detection). Documented in [`docs/database_design.md`](docs/database_design.md). |
| **CO3** | Backend & REST API Development | Flask Blueprints, JSON endpoints, error handling, input validation, and role-based access control. Documented in [`docs/api_documentation.md`](docs/api_documentation.md). |
| **CO4** | Integration & Separation of Concerns | Clean architectural separation: Frontend (HTML/CSS/JS), Service Layer (`services/`), Data Layer (`models/`), and REST Controllers (`routes/`). |
| **CO5** | Problem Solving & Constraint Optimization | Availability-aware scheduling, cross-midnight interval overlap resolution, and leave conflict auto-unassign in `SchedulingService`. |
| **CO6** | Evaluation, Testing & Industry Demonstration | Automated test suite (29 tests passing), step-by-step 14-step demonstration script in [`docs/project_demonstration.md`](docs/project_demonstration.md). |

---

## 11. Troubleshooting Common Issues

1. **Port 5000 Already in Use**:
   If another application is using port 5000, specify an alternate port in `app.py`:
   ```python
   app.run(host='127.0.0.1', port=5050, debug=True)
   ```
2. **Database Locked / Access Denied**:
   Ensure no background Python processes or SQLite viewers are holding a write lock on `instance/workforce.db`.
3. **Execution Policy Restriction in PowerShell**:
   If `.\venv\Scripts\activate` gives a script execution error, run:
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   ```

---

## 12. Limitations & Future Enhancements
- **Current Scope**: Optimized for single-server or local college evaluation using SQLite and Flask development server.
- **Future Enhancements**:
  - Integration with corporate email or SMS gateways (e.g. SendGrid / Twilio) for automated schedule notifications.
  - Integration with PostgreSQL or MySQL for high-concurrency production deployments.
  - Biometric or RFID clock-in integration for automated attendance verification against assigned rosters.
  - Multi-tenant capability for managing multiple corporate organizations within a unified database.

---
*Created for College DBMS Examination and Demonstration.*
