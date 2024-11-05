from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Student(db.Model):
  __tablename__ = 'student'

  student_id = Column(Integer, primary_key=True, autoincrement=True)
  roll_number = Column(String, unique=True, nullable=False)
  first_name = Column(String, nullable=False)
  last_name = Column(String)

  enrolls = relationship('Enroll', back_populates='student', cascade='all, delete')

  def __repr__(self):
    return f'<Student {self.first_name}>'


class Course(db.Model):
  __tablename__ = 'course'

  course_id = Column(Integer, primary_key=True, autoincrement=True)
  course_code = Column(String, nullable=False, unique=True)
  course_name = Column(String, nullable=False)
  course_description = Column(String)

  enrolls = relationship('Enroll', back_populates='course', cascade='all, delete')

  def __repr__(self):
    return f'<Course {self.course_code}>'


class Enroll(db.Model):
  __tablename__ = 'enrollments'

  enrollment_id = Column(Integer, primary_key=True, autoincrement=True)
  estudent_id = Column(Integer, ForeignKey('student.student_id'), nullable=False)
  ecourse_id = Column(Integer, ForeignKey('course.course_id'), nullable=False)

  student = relationship('Student', back_populates='enrolls')
  course = relationship('Course', back_populates='enrolls')

  def __repr__(self):
    return f'<Enroll {self.estudent_id} {self.ecourse_id}>'
