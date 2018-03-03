from flask import Blueprint
from {{cookiecutter.project_core_dir}}.client_module.views import get_views

kwargs = {
    'static_folder': 'static',
    'static_url_path': 'static/site',
    'template_folder': 'templates',
    'url_prefix': '/',
}
site = Blueprint('site', __name__, **kwargs)

for view in get_views():
    site.add_url_rule('/', view_func=view)
