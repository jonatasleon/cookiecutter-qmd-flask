from flask import render_template
from flask_security import login_required
from flask_classy import FlaskView


def get_views():
    # You can append new views here
    return [
        IndexView,
    ]


class IndexView(FlaskView):
    route_base = '/'

    # @login_required  # You can set index page as login required
    def index(self):
        return render_template('index.html')


# Add your own views here
