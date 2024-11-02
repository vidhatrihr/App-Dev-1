from flask import Flask, request, render_template, redirect
from models import session, Student, Course, Enroll

app = Flask(__name__)


@app.route('/')
def index():

  students = session.query(Student).all()
  courses = session.query(Course).all()
  enrolls = session.query(Enroll).all()
  return render_template('index.html', students=students, courses=courses, enrolls=enrolls)


@app.route('/add/student', methods=['GET', 'POST'])
def add_student_route():
  if request.method == 'POST':
    name = request.form['name']
    place = request.form['place']
    age = int(request.form['age'])
    session.add(Student(name=name, place=place, age=age))
    session.commit()
    return redirect('/')
  elif request.method == 'GET':
    return render_template('add-student.html')


@app.route('/add/course', methods=['GET', 'POST'])
def add_course_route():
  if request.method == 'POST':
    name = request.form['name']
    credits = int(request.form['credits'])
    session.add(Course(name=name, credits=credits))
    session.commit()
    return redirect('/')
  elif request.method == 'GET':
    return render_template('add-course.html')


@app.route('/add/enroll', methods=['GET', 'POST'])
def add_enroll_route():
  if request.method == 'POST':
    student_id = int(request.form['student_id'])
    course_id = int(request.form['course_id'])
    term = request.form['term']
    year = int(request.form['year'])
    session.add(Enroll(student_id=student_id, course_id=course_id, term=term, year=year))
    session.commit()
    return redirect('/')
  elif request.method == 'GET':
    return render_template('add-enroll.html')


if __name__ == "__main__":
  app.run(debug=True)
