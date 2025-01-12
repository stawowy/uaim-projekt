import requests

BASE_URL = 'http://127.0.0.1:5000'

def test_login_user_success():
    url = f'{BASE_URL}/api/login'
    payload = {
        'email': 'testuser@email.com',
        'password': 'password'
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 200
    assert response.json()['message'] == 'Login successful'
    assert response.json()['access_token']
    assert response.json()['refresh_token']

def test_login_missing_fields():
    url = f'{BASE_URL}/api/login'
    payload = {
        'email': 'testuser@example.com'
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 400
    assert response.json()['error'] == 'Email and password are required'

def test_login_invalid_credentials():
    url = f'{BASE_URL}/api/login'
    payload = {
        'email': 'testuser@example.com',
        'password': 'wrongpassword'
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 401
    assert response.json()['error'] == 'Invalid email or password'

def test_refresh_token():
    login_url = f"{BASE_URL}/api/login"
    refresh_url = f"{BASE_URL}/api/refresh"
    login_payload = {
        'email': 'testuser@email.com',
        'password': 'password'
    }

    login_response = requests.post(login_url, json=login_payload)
    refresh_token = login_response.json()['refresh_token']

    headers = {"Authorization": f"Bearer {refresh_token}"}
    refresh_response = requests.post(refresh_url, headers=headers)

    assert refresh_response.status_code == 200
    assert refresh_response.json()['access_token']