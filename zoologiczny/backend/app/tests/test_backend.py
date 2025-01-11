import unittest
import sys
import os

from backend.app import create_app

# Add the module path to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_api_test(self):
        response = self.client.get('/api/test')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Backend is running!', response.data)

    def test_error_404(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()