from flask import Blueprint, render_template
from models import *

root_bp = Blueprint('root', __name__)


@root_bp.route('/')
def index():
  # students = session.query(Student).all()
  students = Student.query.all()
  return render_template('index.html', students=students)
