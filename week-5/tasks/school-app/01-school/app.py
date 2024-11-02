from flask import Flask, request, render_template, redirect
from models import *

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html', students=students, courses=courses, enrolls=enrolls)


@app.route('/add/student', methods=['GET', 'POST'])
def add_student_route():
  if request.method == 'POST':
    name = request.form['name']
    place = request.form['place']
    age = int(request.form['age'])
    student = Student(name, place, age)
    add_student(student)
    return redirect('/')
  elif request.method == 'GET':
    return render_template('add-student.html')


@app.route('/add/course', methods=['GET', 'POST'])
def add_course_route():
  if request.method == 'POST':
    name = request.form['name']
    credits = int(request.form['credits'])
    course = Course(name, credits)
    add_course(course)
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
    enroll = Enroll(student_id, course_id, term, year)
    add_enroll(enroll)
    return redirect('/')
  elif request.method == 'GET':
    return render_template('add-enroll.html')


if __name__ == "__main__":
  app.run(debug=True)
