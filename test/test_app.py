import pytest
from app import app

def test_home_route():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Hello" in response.data or b"hello" in response.data

def test_not_found_route():
    tester = app.test_client()
    response = tester.get('/nonexistent')
    assert response.status_code == 404