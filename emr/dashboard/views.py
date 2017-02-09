from flask import Blueprint
from flask import render_template
from flask_login import login_required

dashboard_blueprint = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@dashboard_blueprint.route('')
@login_required
def index():
    return render_template('dashboard/index.html')

