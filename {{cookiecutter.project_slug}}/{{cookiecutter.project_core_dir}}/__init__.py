from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_security import Security
from {{cookiecutter.project_core_dir}}.config import DefaultConfig

admin = Admin(name='{{cookiecutter.project_name}} Admin', template_mode='bootstrap3')
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
security = Security()


def create_app(cfg_file=''):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(DefaultConfig)
    app.config.from_pyfile(cfg_file, silent=True)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db=db)

    from {{cookiecutter.project_core_dir}}.models import user_datastore
    security.init_app(app, datastore=user_datastore)

    from {{cookiecutter.project_core_dir}}.client_module import site
    app.register_blueprint(site)

    from {{cookiecutter.project_core_dir}}.admin_module import get_views
    admin.init_app(app)
    admin.add_views(*get_views())

    return app
