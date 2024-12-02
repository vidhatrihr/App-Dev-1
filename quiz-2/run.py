
# from flask import Flask, abort, url_for
# app = Flask(__name__)


# ===== 3 =====

# @app.route('/<uname>')
# def index(uname):
#   if uname[0].isdigit():
#     abort(400, 'Bad request')
#   return 'Good uname'


# app.run(debug=True)


# ======= 2 =======


# @app.route('/home')
# def index():
#   return 'Mad-1 Student Data'


# @app.route('/student/<student_name>/<int:student_id>')
# def profile(student_name, student_id):
#   return f'Student name:{student_name}, Student ID: {student_id}'


# with app.test_request_context():
#   print(url_for('profile', student_name='John', student_id=101))


# ======= 1 ======


# users = ["admin", "user_1", "user_2", "user_3"]


# @app.route('/home/<string:username>', methods=['POST'])
# def home(username):
#   if username in users:
#     return f'Hello {username}, Welcome!'
#   else:
#     abort(404)


# @app.errorhandler(404)
# def user_error_1(error):
#   return "What you r looking for is invalid"


# @app.errorhandler(405)
# def user_error_2(error):
#   return 'Pls check the web request.'


# app.run()
