from flask import render_template
from flask_security import login_required
from flask.views import MethodView


def get_views():
    return [
        IndexView.as_view('index'),
    ]


class IndexView(MethodView):

    @login_required
    def get(self):
        return render_template('index.html')
