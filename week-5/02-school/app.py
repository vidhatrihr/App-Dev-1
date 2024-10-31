from flask import Flask, request, render_template, redirect
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('test.db', check_same_thread=False)
cur = conn.cursor()


@app.route('/')
def index():
  cur.execute('select * from students')
  students = cur.fetchall()

  cur.execute('select * from courses')
  courses = cur.fetchall()

  cur.execute('select * from enrolls')
  enrolls = cur.fetchall()
  return render_template('index.html', students=students, courses=courses, enrolls=enrolls)


@app.route('/add/student', methods=['GET', 'POST'])
def add_student_route():
  if request.method == 'POST':
    name = request.form['name']
    place = request.form['place']
    age = int(request.form['age'])
    cur.execute("INSERT INTO students (name, place, age) VALUES (?,?,?)", (name, place, age))
    conn.commit()
    return redirect('/')
  elif request.method == 'GET':
    return render_template('add-student.html')


@app.route('/add/course', methods=['GET', 'POST'])
def add_course_route():
  if request.method == 'POST':
    name = request.form['name']
    credits = int(request.form['credits'])
    cur.execute('INSERT INTO courses (name, credits) VALUES (?,?)', (name, credits))
    conn.commit()
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
    cur.execute('INSERT INTO enrolls (student_id, course_id, term, year) VALUES (?,?,?,?)',
                (student_id, course_id, term, year))
    conn.commit()
    return redirect('/')
  elif request.method == 'GET':
    return render_template('add-enroll.html')


if __name__ == "__main__":
  app.run(debug=True)
