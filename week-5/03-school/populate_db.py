from models import session, Student, Course, Enroll

session.add(Student(name='rahul', place='albd', age=23))
session.add(Student(name='cmd', place='albd', age=24))
session.add(Student(name='vidu', place='hbh', age=21))
session.add(Course(name='mad1', credits=10))
session.add(Course(name='dbms', credits=10))

session.add(Enroll(student_id=2, course_id=2, term='T1', year=2024))
session.add(Enroll(student_id=2, course_id=2, term='T3', year=2024))
session.add(Enroll(student_id=1, course_id=1, term='T2', year=2024))
session.commit()
