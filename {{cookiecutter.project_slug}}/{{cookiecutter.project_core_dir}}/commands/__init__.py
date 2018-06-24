from .user import create_cli


def register_commands(app):
    """Register commands with Flask application."""
    app.cli.add_command(create_cli)
