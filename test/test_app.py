import pytest
from app import home, app


def test_home_route():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
   

def test_not_found_route():
    tester = app.test_client()
    response = tester.get('/nonexistent')
    assert response.status_code == 404
