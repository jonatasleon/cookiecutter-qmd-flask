from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_security import Security
{% if cookiecutter.admin in ['yes', 'y'] -%}
from {{cookiecutter.project_core_dir}}.admin import admin
{%- endif %}

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
security = Security()


def register_extensions(app):
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db=db)
    security.init_app(app, datastore=user_datastore)
    {% if cookiecutter.admin in ['yes', 'y'] -%}
    admin.init_app(app)
    {%- endif %}
