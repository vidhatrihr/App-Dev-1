from flask import Flask, session

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'


@app.route('/')
def greet():
  if 'name' in session:
    return f'Hello {session['name']}!!'
  return 'Hello guest'


@app.route('/know-me/<my_name>')
def know_me(my_name):
  session['name'] = my_name
  return f'Hello {my_name} now I know u!!'


app.run(debug=True)
