from flask_admin import Admin
from {{cookiecutter.project_core_dir}}.admin.views import get_views

admin = Admin(name='{{cookiecutter.project_name}} Admin', template_mode='bootstrap3')
admin.add_views(*get_views())
