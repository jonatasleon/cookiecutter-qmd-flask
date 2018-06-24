from flask import Blueprint
from .views import IndexView

options = {
    'static_folder': 'static',
    'static_url_path': 'static/client',
    'template_folder': 'templates',
    'url_prefix': '/',
}

client = Blueprint('client', __name__, **options)
client.add_view(IndexView())
