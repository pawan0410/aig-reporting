from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_assets import Environment, Bundle
from flask_migrate import Migrate


login_manager = LoginManager()
db = SQLAlchemy()
mail = Mail()
assets = Environment()
migrate = Migrate()


# Assets configuration
assets.register(
    'js_all',
    Bundle(
        'bower_components/jquery/dist/jquery.min.js',
        'bower_components/bootstrap/dist/js/bootstrap.min.js',
        filters='jsmin',
        output='packed.js'
    )
)

assets.register(
    'css_all',
    Bundle(
        'bower_components/bootstrap/dist/css/bootstrap.min.css',
        'flatui/css/uikit.min.css',
        'css/custom.css'
    )
)
