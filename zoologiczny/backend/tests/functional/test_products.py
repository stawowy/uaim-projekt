import requests

BASE_URL = 'http://127.0.0.1:5000'

def test_get_products():
    url = f'{BASE_URL}/api/products'

    response = requests.get(url)

    assert response.status_code == 200
    assert response.json()

def test_get_product_by_id():
    url = f'{BASE_URL}/api/products/1'

    response = requests.get(url)

    assert response.status_code == 200
    assert response.json()

def test_get_product_by_id_not_found():
    url = f'{BASE_URL}/api/products/168974578'

    response = requests.get(url)

    assert response.status_code == 404
    assert response.json()