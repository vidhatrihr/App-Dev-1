from flask import Blueprint, render_template, request, redirect
from flask_login import current_user, login_user, logout_user
from models import *

bp = Blueprint('default', __name__)


def check_if_liked(post):
  like = Like.query.filter_by(
      post_id=post.id,
      user_id=current_user.id,
  ).first()
  if like:
    return True
  return False


def count_likes(post):
  return len(post.likes)


@bp.route('/')
def index():
  if current_user.is_authenticated:
    posts = Post.query.all()
    return render_template('index.html', posts=posts, check_if_liked=check_if_liked, count_likes=count_likes)
  else:
    return redirect('/login')


@bp.route('/create-post', methods=['POST'])
def create_post():
  db.session.add(Post(
      user_id=current_user.id,
      body=request.form.get('post')
  ))
  db.session.commit()
  return redirect('/')


@bp.route('/unlike/<int:post_id>')
def unlike(post_id):
  like = Like.query.filter_by(
      post_id=post_id,
      user_id=current_user.id
  ).first()
  db.session.delete(like)
  db.session.commit()
  return redirect('/')


@bp.route('/like/<int:post_id>')
def like(post_id):
  db.session.add(Like(
      post_id=post_id,
      user_id=current_user.id
  ))
  db.session.commit()
  return redirect('/')


@bp.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    return render_template('login.html')

  elif request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()
    if user and user.password == password:
      login_user(user)
      return redirect('/')
    else:
      return render_template('login.html', error=True)


@bp.route('/logout')
def logout():
  logout_user()
  return redirect('/login')
