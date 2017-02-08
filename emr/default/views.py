from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from flask import redirect
from flask import url_for

from flask_login import login_user
from flask_login import logout_user

from emr.extensions import login_manager
from .forms import LoginForm
from emr.models.user import User


default_blueprint = Blueprint('default', __name__, url_prefix='/')


@login_manager.user_loader
def load_user(id):
    return User.query.filter(User.id == id, User.active == 1).first()


@default_blueprint.route('', methods=['GET', 'POST', ])
def index():
    """ Welcome page
    """

    form = LoginForm(request.form)

    if request.method == 'POST':
        if not form.validate_on_submit():
            flash(form.errors)
            return redirect(url_for('default.index'))
        user = User.query.filter_by(
            username=form.username.data, password=form.password.data).first()
        if user and user.active:
            user.authenticated = True
            login_user(user)
            return redirect(url_for('dashboard.index'))
        else:
            form.username.errors.append('System cannot identify your login credentials.')
            flash(form.errors)
            return redirect(url_for('default.index'))

    return render_template('default.html', form=form)


@default_blueprint.route('logout')
def logout():
    """ logout user
    """
    logout_user()
    return redirect(url_for('default.index'))
