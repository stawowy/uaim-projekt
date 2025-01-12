import requests

BASE_URL = 'http://127.0.0.1:5000'

def test_get_user():
    login_url = f'{BASE_URL}/api/login'
    profile_url = f'{BASE_URL}/api/profile/test_user'
    login_payload = {
        'email': 'testuser@email.com',
        'password': 'password'
    }

    login_response = requests.post(login_url, json=login_payload)
    access_token = login_response.json()['access_token']

    headers = {"Authorization": f"Bearer {access_token}"}
    profile_response = requests.get(profile_url, headers=headers)

    assert profile_response.status_code == 200
    assert profile_response.json()['username'] == 'test_user'

def test_get_user_not_found():
    login_url = f'{BASE_URL}/api/login'
    profile_url = f'{BASE_URL}/api/profile/unknown_user'
    login_payload = {
        'email': 'testuser@email.com',
        'password': 'password'
    }

    login_response = requests.post(login_url, json=login_payload)
    access_token = login_response.json()['access_token']

    headers = {"Authorization": f"Bearer {access_token}"}
    profile_response = requests.get(profile_url, headers=headers)

    assert profile_response.status_code == 404
    assert profile_response.json()['error'] == 'User not found'

def test_get_user_unauthorized():
    profile_url = f'{BASE_URL}/api/profile/test_user'
    profile_response = requests.get(profile_url)

    assert profile_response.status_code == 401
    assert profile_response.json()['msg'] == 'Missing Authorization Header'