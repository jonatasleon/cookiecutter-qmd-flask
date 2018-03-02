from flask import url_for


def test_index(client):
    assert client.get(url_for('site.index')).status_code == 200


def test_admin(client):
    assert client.get(url_for('admin.index')).status_code == 200
