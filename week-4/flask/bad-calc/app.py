from flask import Flask, request, render_template
from datetime import datetime


app = Flask(__name__)


@app.route('/')
def root():
  return f'Hello from root, datetime is {datetime.now()}'


@app.route('/greet')
def greet():
  return 'Good Morning somebody'


@app.route('/greet/<name>')
def greet_all(name):
  return f'Good Morning {name}'


# @app.route('/greet/rahul')
# def greet_rahul():
#   return 'good morning rahul'


# @app.route('/greet/vidu')
# def greet_vidu():
#   return 'good morning vidu'


@app.route('/add/<a>/<b>')
def add(a, b):
  return str(int(a)+int(b))


@app.route('/calc/<op>/<a>/<b>')
def calc(op, a, b):
  if op == 'add':
    result = int(a)+int(b)
  elif op == 'minus':
    result = int(a)-int(b)
  elif op == 'mult':
    result = int(a)*int(b)
  elif op == 'div':
    result = int(a)/int(b)
  elif op == 'power':
    result = int(a)**int(b)

  return render_template('calc.html', op=op, a=a, b=b, result=result)
  # if op == 'add':
  #   return f'<h1>Result = <span style="color:red">{int(a)+int(b)}</span></h1>'
  # elif op == 'minus':
  #   return f'<h1>Result = <span style="color:red">{int(a)-int(b)}</span></h1>'
  # elif op == 'mult':
  #   return f'<h1>Result = <span style="color:red">{int(a)*int(b)}</span></h1>'
  # elif op == 'div':
  #   return f'<h1>Result = <span style="color:red">{int(a)/int(b)}</span></h1>'
  # elif op == 'power':
  #   return f'<h1>Result = <span style="color:red">{int(a)**int(b)}</span></h1>'


@app.route('/quiz/1')
def quiz1():
  return '<h1>Quiz 1 is on <span style="color:green">27th Oct</span></h1>'


@app.route('/quiz/2')
def quiz2():
  return render_template('quiz2.html')


@app.route('/html-test')
def html():
  return render_template('test.html')


if __name__ == '__main__':
  app.run(debug=True)
