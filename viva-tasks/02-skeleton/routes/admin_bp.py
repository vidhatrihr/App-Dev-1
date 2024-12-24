from flask import Blueprint, render_template
from flask_login import login_required, current_user

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/admin/home')
@login_required
def admin_home():
  if current_user.type != 'admin':
    return 'You are not permitted', 403
  return render_template('admin_home.html')
