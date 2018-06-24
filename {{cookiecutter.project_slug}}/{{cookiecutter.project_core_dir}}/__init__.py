from os import path
from flask import Flask
from {{cookiecutter.project_core_dir}}.extensions import register_extensions
from {{cookiecutter.project_core_dir}}.admin import admin
from {{cookiecutter.project_core_dir}}.models import user_datastore
from {{cookiecutter.project_core_dir}}.modules import register_blueprints
from {{cookiecutter.project_core_dir}}.commands import register_commands


def create_app(cfg_file=path.curdir):
    app = Flask(__name__, instance_path=path.dirname(cfg_file))
    app.config.from_object('{{cookiecutter.project_core_dir}}.DefaultConfig')
    app.config.from_pyfile(path.basename(cfg_file), silent=True)

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)

    return app
