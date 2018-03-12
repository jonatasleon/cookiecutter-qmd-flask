from flask import Blueprint
from {{cookiecutter.project_core_dir}}.client_module.views import get_views
from {{cookiecutter.project_core_dir}}.helpers import register_views

kwargs = {
    'static_folder': 'static',
    'static_url_path': 'static/site',
    'template_folder': 'templates',
    'url_prefix': '/',
}
site = Blueprint('site', __name__, **kwargs)

register_views(site, get_views())
