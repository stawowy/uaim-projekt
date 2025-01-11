import unittest
from flask import current_app
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta
from ..models import User

class LoginTestCase(unittest.TestCase):

    def test_login_success(self):
        response = self.client.post('/login', json={
            'email': 'test@example.com',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.json)
        self.assertIn('refresh_token', response.json)

    def test_login_missing_fields(self):
        response = self.client.post('/login', json={
            'email': 'test@example.com'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

    def test_login_invalid_credentials(self):
        response = self.client.post('/login', json={
            'email': 'test@example.com',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 401)
        self.assertIn('error', response.json)

    def test_refresh_token(self):
        with self.app.app_context():
            user = User.query.filter_by(email='test@example.com').first()
            refresh_token = create_refresh_token(identity=str(user.user_id))
        
        response = self.client.post('/refresh', headers={
            'Authorization': f'Bearer {refresh_token}'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.json)

if __name__ == '__main__':
    unittest.main()
    