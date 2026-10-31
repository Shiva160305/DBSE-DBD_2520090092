import os
from datetime import datetime, date, timedelta
from flask import Flask, render_template
from config import Config
from models import db, Admin, Department, Shift, Employee, Schedule, EmployeeAvailability, LeaveRequest, AuditLog
from routes import (
    auth_bp,
    employee_bp,
    department_bp,
    shift_bp,
    schedule_bp,
    availability_bp,
    leave_bp,
    analytics_bp
)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Ensure instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    # Initialize extensions
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(employee_bp)
    app.register_blueprint(department_bp)
    app.register_blueprint(shift_bp)
    app.register_blueprint(schedule_bp)
    app.register_blueprint(availability_bp)
    app.register_blueprint(leave_bp)
    app.register_blueprint(analytics_bp)

    # Global template context
    @app.context_processor
    def inject_global_vars():
        return {
            'now': datetime.utcnow(),
            'current_year': datetime.utcnow().year,
            'app_name': 'Workforce Management System'
        }

    # Error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('base.html', custom_content='<div class="text-center py-5"><h2>404 - Page Not Found</h2><p class="text-muted">The requested page could not be located.</p><a href="/" class="btn btn-primary mt-3">Return to Home</a></div>'), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template('base.html', custom_content='<div class="text-center py-5"><h2>500 - Server Error</h2><p class="text-muted">An unexpected server error occurred. Please contact the administrator.</p><a href="/" class="btn btn-primary mt-3">Return to Home</a></div>'), 500

    return app

def seed_database(app):
    """Seed initial administrator, departments, shifts, and sample demo data idempotently."""
    with app.app_context():
        db.create_all()

        # 1. Seed Administrator: admin / 123
        admin = Admin.query.filter_by(username='admin').first()
        if not admin:
            admin = Admin(username='admin')
            admin.set_password('123')
            db.session.add(admin)
            print('[SEED] Default administrator created (admin / 123)')

        # 2. Seed 5 Default Departments
        default_depts = [
            ('Hospitality', 'Guest relations, customer front-desk, and venue hospitality services.'),
            ('Technical Support', 'Infrastructure, IT support desk, hardware, and client systems engineering.'),
            ('Human Resource', 'Talent acquisition, employee welfare, payroll, and compliance operations.'),
            ('Marketing', 'Digital communications, brand strategy, content, and public outreach.'),
            ('Management', 'Executive oversight, strategic workforce planning, and organizational leadership.')
        ]
        dept_map = {}
        for d_name, d_desc in default_depts:
            dept = Department.query.filter_by(department_name=d_name).first()
            if not dept:
                dept = Department(department_name=d_name, description=d_desc)
                db.session.add(dept)
                db.session.flush()
                print(f'[SEED] Department created: {d_name}')
            dept_map[d_name] = dept

        # 3. Seed 3 Default Shifts
        default_shifts = [
            ('Morning Shift', '06:00', '14:00', 'Standard morning operations and opening roster.'),
            ('Evening Shift', '14:00', '22:00', 'Afternoon to evening peak operations and mid-day cover.'),
            ('Night Shift', '22:00', '06:00', 'Overnight graveyard operations spanning into the next morning.')
        ]
        shift_map = {}
        for s_name, s_start, s_end, s_desc in default_shifts:
            shift = Shift.query.filter_by(shift_name=s_name).first()
            if not shift:
                shift = Shift(shift_name=s_name, start_time=s_start, end_time=s_end, description=s_desc, active_status=True)
                db.session.add(shift)
                db.session.flush()
                print(f'[SEED] Shift created: {s_name} ({s_start}-{s_end})')
            shift_map[s_name] = shift

        # 4. Seed Demonstration Employees (only if employees table is empty)
        if Employee.query.count() == 0:
            sample_employees = [
                ('EMP001', 'Sarah Jenkins', 'sarah.jenkins@workforce.local', '555-0101', 'Hospitality', 'Front Desk Lead', 'emp123'),
                ('EMP002', 'David Chen', 'david.chen@workforce.local', '555-0102', 'Technical Support', 'Senior Systems Engineer', 'emp123'),
                ('EMP003', 'Priya Sharma', 'priya.sharma@workforce.local', '555-0103', 'Human Resource', 'HR Specialist', 'emp123'),
                ('EMP004', 'Marcus Vance', 'marcus.vance@workforce.local', '555-0104', 'Marketing', 'Campaign Strategist', 'emp123'),
                ('EMP005', 'Elena Rostova', 'elena.rostova@workforce.local', '555-0105', 'Management', 'Operations Supervisor', 'emp123'),
                ('EMP006', 'Alex Turner', 'alex.turner@workforce.local', '555-0106', 'Technical Support', 'Network Analyst', 'emp123'),
            ]
            emp_objs = {}
            for e_id, e_name, e_email, e_phone, d_name, e_desig, e_pw in sample_employees:
                emp = Employee(
                    employee_id=e_id,
                    name=e_name,
                    email=e_email,
                    phone=e_phone,
                    department_id=dept_map[d_name].department_id,
                    designation=e_desig,
                    employment_status='Active'
                )
                emp.set_password(e_pw)
                db.session.add(emp)
                emp_objs[e_id] = emp
            db.session.flush()
            print('[SEED] Sample employees created with default password: emp123')

            # 5. Seed Demonstration Schedules for the Current Week
            today = date.today()
            mon = today - timedelta(days=today.weekday())

            # Schedule sample assignments across the week
            sample_assignments = [
                ('EMP001', 'Morning Shift', mon),
                ('EMP001', 'Morning Shift', mon + timedelta(days=1)),
                ('EMP001', 'Morning Shift', mon + timedelta(days=2)),
                ('EMP002', 'Evening Shift', mon),
                ('EMP002', 'Evening Shift', mon + timedelta(days=1)),
                ('EMP002', 'Evening Shift', mon + timedelta(days=3)),
                ('EMP003', 'Morning Shift', mon),
                ('EMP003', 'Morning Shift', mon + timedelta(days=2)),
                ('EMP004', 'Evening Shift', mon + timedelta(days=1)),
                ('EMP004', 'Evening Shift', mon + timedelta(days=2)),
                ('EMP005', 'Morning Shift', mon),
                ('EMP005', 'Morning Shift', mon + timedelta(days=1)),
                ('EMP005', 'Morning Shift', mon + timedelta(days=3)),
                ('EMP006', 'Night Shift', mon),
                ('EMP006', 'Night Shift', mon + timedelta(days=2)),
            ]
            for e_id, s_name, s_date in sample_assignments:
                sched = Schedule(
                    employee_id=e_id,
                    shift_id=shift_map[s_name].shift_id,
                    shift_date=s_date,
                    assigned_by='admin'
                )
                db.session.add(sched)

            # 6. Seed Sample Availability
            avail1 = EmployeeAvailability(
                employee_id='EMP006',
                available_date=mon + timedelta(days=4), # Friday
                availability_status='Unavailable',
                notes='Personal medical appointment scheduled.'
            )
            avail2 = EmployeeAvailability(
                employee_id='EMP001',
                available_date=mon + timedelta(days=5), # Saturday
                availability_status='Available',
                notes='Available for emergency overtime.'
            )
            db.session.add(avail1)
            db.session.add(avail2)

            # 7. Seed Sample Leave Requests
            lr1 = LeaveRequest(
                employee_id='EMP001',
                requested_date=mon + timedelta(days=4),
                shift_id=shift_map['Morning Shift'].shift_id,
                reason='Family function attendance.',
                request_status='Pending'
            )
            lr2 = LeaveRequest(
                employee_id='EMP002',
                requested_date=mon + timedelta(days=5),
                shift_id=shift_map['Evening Shift'].shift_id,
                reason='Professional development workshop.',
                request_status='Approved',
                reviewed_by='admin',
                reviewed_at=datetime.utcnow() - timedelta(hours=5),
                admin_remarks='Approved. Cover arranged with Alex Turner.'
            )
            lr3 = LeaveRequest(
                employee_id='EMP004',
                requested_date=mon + timedelta(days=6),
                shift_id=shift_map['Evening Shift'].shift_id,
                reason='Short notice personal trip.',
                request_status='Rejected',
                reviewed_by='admin',
                reviewed_at=datetime.utcnow() - timedelta(hours=2),
                admin_remarks='Campaign launch weekend requires all marketing personnel.'
            )
            db.session.add(lr1)
            db.session.add(lr2)
            db.session.add(lr3)

            # 8. Seed Initial Audit Log
            log = AuditLog(
                action='SYSTEM_INITIALIZED',
                performed_by='system',
                details='Database initialized with departments, default shifts, and demonstration data.'
            )
            db.session.add(log)
            print('[SEED] Sample schedules, availability records, and leave requests populated.')

        db.session.commit()
        print('[OK] Database initialization and verification complete.')

app = create_app()

if __name__ == '__main__':
    seed_database(app)
    print('\n======================================================')
    print('  WORKFORCE MANAGEMENT SYSTEM (DBMS PROJECT)')
    print('  Local Development Server: http://127.0.0.1:5000')
    print('  Admin Login: admin / 123')
    print('  Sample Employee: EMP001 / emp123')
    print('======================================================\n')
    app.run(host='127.0.0.1', port=5000, debug=True)
