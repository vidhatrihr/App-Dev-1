class Student:
  _idx = 1

  def __init__(self, name, place, age):
    self.id = Student._idx
    Student._idx += 1

    self.name = name
    self.place = place
    self.age = age

  def __repr__(self):
    return f'<Student {self.name}>'


class Course:
  _idx = 1

  def __init__(self, name, credits):
    self.id = Course._idx
    Course._idx += 1

    self.name = name
    self.credits = credits

  def __repr__(self):
    return f'<Course {self.name}>'


class Enroll:
  _idx = 1

  def __init__(self, student_id, course_id, term, year):
    self.id = Enroll._idx
    Enroll._idx += 1

    self.student_id = student_id
    self.course_id = course_id
    self.term = term
    self.year = year

  def __repr__(self):
    return f'<Enroll {self.student_id} {self.course_id}>'


students = {}
courses = {}
enrolls = {}


def add_student(student):
  students[student.id] = student


def add_course(course):
  courses[course.id] = course


def add_enroll(enroll):
  enrolls[enroll.id] = enroll


# Demo data
add_student(Student('vidu', 'hbh', 21))
add_student(Student('rahul', 'albd', 23))
add_course(Course('maths1', 10))
add_course(Course('stats', 20))
add_enroll(Enroll(student_id=1, course_id=1, term='T3', year=2023))
add_enroll(Enroll(student_id=2, course_id=2, term='T2', year=2023))
