import click
from click_datetime import Datetime
from flask.cli import AppGroup
from flask_security import utils
from {{cookiecutter.project_core_dir}}.extensions import db
from {{cookiecutter.project_core_dir}}.models import user_datastore

create_cli = AppGroup('download')
create_cli.__doc__ = """Download active fire files."""


@user_cli.command('admin')
@click.option('--email', default=None)
def createadmin(email):
    """Create an user with administrative privileges."""
    admin_role = dict(name='admin', description='Administrator')
    user_datastore.find_or_create_role(**admin_role)
    db.session.commit()

    if email is None:
        email = click.prompt('Enter an e-mail')
    password = click.prompt('Enter a password', hide_input=True, confirmation_prompt=True)
    password = utils.encrypt_password(password)

    if user_datastore.get_user(email):
        click.echo('\'{}\' user already exists'.format(email))

    user_datastore.create_user(email=email, password=password)
    user_datastore.add_role_to_user(email, admin_role['name'])
    db.session.commit()

    click.echo('\'{}\' created with success'.format(email))
