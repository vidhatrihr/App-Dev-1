from models import session, Course, Student, Enroll


session.add(Course(course_code='CSE01', course_name='MAD 1', course_description='...'))
session.add(Course(course_code='CSE02', course_name='DBMS', course_description='...'))
session.add(Course(course_code='CSE03', course_name='PDSA', course_description='...'))
session.add(Course(course_code='BST13', course_name='BDM', course_description='...'))

session.add(Student(roll_number='1', first_name='Harikesh', last_name='Shukla'))

session.add(Enroll(estudent_id=1, ecourse_id=1))
session.add(Enroll(estudent_id=1, ecourse_id=3))

session.commit()
print('populate db done')
