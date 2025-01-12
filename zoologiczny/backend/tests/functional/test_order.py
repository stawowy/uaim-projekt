import requests

BASE_URL = 'http://127.0.0.1:5000'

def test_place_order():
    login_url = f"{BASE_URL}/api/login"
    order_url = f"{BASE_URL}/api/order"
    login_payload = {
        'email': 'testuser@email.com',
        'password': 'password'
    }

    login_response = requests.post(login_url, json=login_payload)
    assert login_response.status_code == 200
    access_token = login_response.json()['access_token']
    
    order_payload = {
        'user_id': 1,
        'products': {
            '1': 2,
            '2': 1
        },
        'shipping_address': 'Test address'
    }

    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.post(order_url, headers=headers, json=order_payload)
    assert response.status_code == 201
    assert response.json()['message'] == 'Order placed successfully'

def test_place_order_missing_fields():
    login_url = f"{BASE_URL}/api/login"
    order_url = f"{BASE_URL}/api/order"
    login_payload = {
        'email': 'testuser@email.com',
        'password': 'password'
    }

    login_response = requests.post(login_url, json=login_payload)
    assert login_response.status_code == 200
    access_token = login_response.json()['access_token']
    
    order_payload = {
        'products': {
            '1': 2,
            '2': 1
        },
        'shipping_address': 'Test address'
    }

    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.post(order_url, headers=headers, json=order_payload)
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing fields'

def test_place_order_product_not_found():
    login_url = f"{BASE_URL}/api/login"
    order_url = f"{BASE_URL}/api/order"
    login_payload = {
        'email': 'testuser@email.com',
        'password': 'password'
    }

    login_response = requests.post(login_url, json=login_payload)
    assert login_response.status_code == 200
    access_token = login_response.json()['access_token']
    
    order_payload = {
        'user_id': 1,
        'products': {
            '5234232': 2,
            '2': 1
        },
        'shipping_address': 'Test address'
    }

    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.post(order_url, headers=headers, json=order_payload)
    
    assert response.status_code == 404
    assert response.json()['error'] == 'Product not found'

def test_place_order_invalid_quantity():
    login_url = f"{BASE_URL}/api/login"
    order_url = f"{BASE_URL}/api/order"
    login_payload = {
        'email': 'testuser@email.com',
        'password': 'password'
    }

    login_response = requests.post(login_url, json=login_payload)
    assert login_response.status_code == 200
    access_token = login_response.json()['access_token']
    
    order_payload = {
        'user_id': 1,
        'products': {
            '1': 500,
            '2': 1
        },
        'shipping_address': 'Test address'
    }

    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.post(order_url, headers=headers, json=order_payload)
    
    assert response.status_code == 409
    assert response.json()['error'] == 'Specified quantity too large'
