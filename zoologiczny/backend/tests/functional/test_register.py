import requests
import pytest

BASE_URL = 'http://127.0.0.1:5000'

# this is for simplicity, create an user first to not have to clear the database each test
@pytest.mark.order(1)
def test_register_user_success():
    url = f'{BASE_URL}/api/register'
    payload = {
        'username': 'test_user',
        'email': 'testuser@email.com',
        'password': 'password',
        'first_name': 'Test',
        'last_name': 'User',
        'phone': '123456789'
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 201
    assert response.json()['message'] == 'User registered successfully'

def test_register_user_missing_fields():    
    url = f'{BASE_URL}/api/register'
    payload = {
        'username': 'test_user',
        'email': 'testuser@email.com',
        'password': 'password',
        'first_name': 'Test',
        'last_name': 'User'
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 400
    assert response.json()['error'] == 'All fields are required'

def test_register_user_already_exists():
    url = f'{BASE_URL}/api/register'
    payload = {
        'username': 'test_user',
        'email': 'testuser@email.com',
        'password': 'password',
        'first_name': 'Test',
        'last_name': 'User',
        'phone': '123456789'
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 400
    assert response.json()['error'] == 'User already exists'