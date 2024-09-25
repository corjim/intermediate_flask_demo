from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def connect_db(app):
    with app.app_context():
        db.app = app 
        db.init_app(app)



#   MODELS GO BELOW


class Department(db.Model):
    '''Department Modle'''

    __tablename__ = 'departments'

    dept_code = db.Column(db.Text, primary_key=True)
    dept_name = db.Column(db.Text, nullable=False, unique=True)
    phone = db.Column(db.Integer, unique=False)

    associates = db.relationship('Employee')

    def __repr__(self):
        """show info about post"""
        p = self 
        return f'<Dept_code ={p.dept_code}, name = {p.dept_name}, phone = {p.phone}'



class Employee(db.Model):
    '''Employee Model'''

    __tablename__ = 'employees'

    def __repr__(self):
        """show info about post"""
        p = self 
        return f'<Employee name = {p.name}, state = {p.state}, phone = {p.dept_code}'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True) #nullable=False means its required

    state = db.Column(db.Text, nullable=False, default="AR")
    dept_code = db.Column(db.Text, db.ForeignKey('departments.dept_code'))

    # dept = db.relationship('Department', backref='employees')

    # assignments = db.relationship("EmployeeProject", backref='employee')                                       

    projects = db.relationship('Projects', secondary='employes_projects', backref='employees')


# Employee.dept.dept_name  // 'Marketing' // relates the feature of the other table to the other one.


class Project(db.Model):

    __tablename__ = 'projects'

    proj_code = db.Column(db.Text, primary_key=True)
    proj_name = db.Column(db.Text, nullable=False, unique=True)

    assignments = db.relationship('EmployeeProject', backref='project')


class Project(db.Model):

    __tablename__ = 'projects'

    proj_code = db.Column(db.Text, primary_key=True)
    proj_name = db.Column(db.Text, nullable=False, unique=True)

    assignments = db.relationship('EmployeeProject', backref='project')


class EmployeeProject(db.Model):

    __tablename__ = 'employees_projects'

    emp_id = db.Column(db.Integer, db.ForeignKey('employees.id'), primary_key=True)
    proj_code = db.Column(db.Text, db.ForeignKey('projects.proj_code'), primary_key=True)
    role = db.Column(db.Text, nullable=True)
