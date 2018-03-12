from flask_classy import FlaskView


def register_views(app, views):
    if isinstance(views, FlaskView):
        views = [views]

    for view in views:
        view.register(app)
