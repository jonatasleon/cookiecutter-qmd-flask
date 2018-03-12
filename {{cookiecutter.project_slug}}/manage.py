#!/usr/bin/env python
import click
from flask.cli import FlaskGroup


def create_app(info):
    from {{cookiecutter.project_core_dir}} import create_app
    return create_app(cfg_file='config.cfg')


@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    pass


@cli.command()
def createadmin():
    """Create a user with administrative privileges"""
    from {{cookiecutter.project_core_dir}} import db
    from {{cookiecutter.project_core_dir}}.models import user_datastore
    from flask_security import utils
    db.create_all()

    admin_role = dict(name='admin', description='Administrator')
    user_datastore.find_or_create_role(**admin_role)
    db.session.commit()

    email = click.prompt('Enter a e-mail')
    password = click.prompt('Enter a password', hide_input=True, confirmation_prompt=True)
    encrypted_password = utils.encrypt_password(password)

    if user_datastore.get_user(email):
        click.echo('\'{}\' user already exists'.format(email))

    user_datastore.create_user(email=email, password=encrypted_password)
    user_datastore.add_role_to_user(email, admin_role['name'])
    db.session.commit()

    click.echo('\'{}\' created with success'.format(email))


@cli.command()
def routes():
    """List all routes to project"""
    import urllib
    from flask import current_app as app
    output = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        line = urllib.parse.unquote('{:50s} {:23s} {}'.format(rule.endpoint, methods, rule))
        output.append(line)

    for line in sorted(output):
        click.echo(line)


if __name__ == '__main__':
    cli()
