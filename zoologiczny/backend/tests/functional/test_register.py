import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'

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