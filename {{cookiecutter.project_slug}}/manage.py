import click
from flask.cli import FlaskGroup


def create_app(info):
    from {{cookiecutter.project_core_dir}} import create_app
    return create_app(cfg_file='config.cfg')


@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    pass


@cli.command()
def init():
    """Initialize application"""
    from designer import db
    from designer.models import user_datastore
    from flask_security import utils
    db.create_all()

    admin_role = dict(name='admin', description='Administrator')
    user_role = dict(name='end-user', description='End user')
    user_datastore.find_or_create_role(**admin_role)
    user_datastore.find_or_create_role(**user_role)

    encrypted_password = utils.encrypt_password('123456')
    if not user_datastore.get_user('someone@example.com'):
        user_datastore.create_user(email='someone@example.com', password=encrypted_password)
    if not user_datastore.get_user('admin@example.com'):
        user_datastore.create_user(email='admin@example.com', password=encrypted_password)

    db.session.commit()

    user_datastore.add_role_to_user('someone@example.com', 'end-user')
    user_datastore.add_role_to_user('admin@example.com', 'admin')
    db.session.commit()


if __name__ == '__main__':
    cli()
