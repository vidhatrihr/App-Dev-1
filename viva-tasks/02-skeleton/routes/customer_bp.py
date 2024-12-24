from flask import Blueprint, render_template
from flask_login import login_required, current_user


customer_bp = Blueprint('customer', __name__)


@customer_bp.route('/customer/home')
@login_required
def customer_home():
  if current_user.type != 'customer':
    return 'NOt permitted', 403
  return render_template('customer_home.html')
