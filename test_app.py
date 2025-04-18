# test_app.py
from app import app

def test_root_route():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello World!'

def test_joke_route():
    client = app.test_client()
    response = client.get('/joke')
    assert response.status_code == 200
    assert isinstance(response.data, bytes)