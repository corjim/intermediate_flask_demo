from models import Department, Employee, db, Project, EmployeeProject
from app import app

# create all tables
db.drop_all()
db.create_all()

d1 = Department(dept_code='mktg',dept_name='Marketing', phone= 99393993)

d2 = Department(dept_code='IT',dept_name='Information Tech', phone= 20355993)

d3 = Department(dept_code='act',dept_name='Accounting', phone= 993938893)

d4 = Department(dept_code='lgl',dept_name='Legal', phone=2544551)

d5 = Department(dept_code='sm',dept_name='Social Media')

d6 = Department(dept_code='HR',dept_name='Human Resources', phone=2565555)




broda = Employee(name='Broda Bennerda', state='AL', dept_code='mktg')

Jon = Employee(name='John Bull', state='AK', dept_code='act')

Ron = Employee(name='Jake Ron', state='AR', dept_code='mktg')

Obi = Employee(name='Obi Bull', state='LA', dept_code='lgl')

Eze = Employee(name='Eze Henry', state='VA', dept_code='lgl')

Stev = Employee(name='Chike Steve', state='VA', dept_code='IT')

Ada = Employee(name='Ada Love', state='AR', dept_code='HR')

Fla = Employee(name='Fla Robin', state='AK', dept_code='sm')


db.session.add_all([d1,d2,d3,d4,d5,d6])

db.session.commit()

db.session.add(broda)
db.session.add(Jon)
db.session.add(Obi)
db.session.add(Ron)
db.session.add(Stev)
db.session.add(Eze)
db.session.add(Ada)
db.session.add(Fla)

db.session.commit()


pc = Project(proj_code='car', proj_name='Design Car',
             assignments=[EmployeeProject(emp_id=Ada.id, role='Chair'),
                          EmployeeProject(emp_id=Obi.id)])
ps = Project(proj_code='server', proj_name='Deploy Server',
             assignments=[EmployeeProject(emp_id=Ada.id),
                          EmployeeProject(emp_id=Eze.id, role='Auditor')])

db.session.add_all([ps, pc])
db.session.commit()


