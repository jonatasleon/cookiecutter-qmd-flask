from flask import render_template
from flask_classy import FlaskView


class IndexView(FlaskView):
    route_base = '/'

    # @login_required  # You can set index page as login required
    def index(self):
        return render_template('index.html')


# Add your own views here
