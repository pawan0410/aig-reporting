"""
A Web Based Reporting Interface for Medstreaming EHR and EMR
"""

import locale
import logging
from logging.handlers import RotatingFileHandler
from werkzeug.contrib.fixers import ProxyFix

from flask import Flask

from emr.config import app_config
from emr.extensions import login_manager
from emr.extensions import db
from emr.extensions import mail
from emr.extensions import assets
from emr.extensions import migrate

from emr.default.views import default_blueprint


def emr_app(config_name):
    """ Application Factories
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    handler = RotatingFileHandler('emr.log')
    handler.setLevel(logging.INFO)

    app.logger.addHandler(handler)
    app.wsgi_app = ProxyFix(app.wsgi_app)

    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    assets.init_app(app)

    # Register blueprints
    app.register_blueprint(default_blueprint)
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    with app.app_context():
        db.create_all()
    return app
