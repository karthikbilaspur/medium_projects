import unittest
import requests
from music_recommendation.src.api_integration import app

class TestAPIIntegration(unittest.TestCase):

    def test_recommend_endpoint(self):
        response = requests.post('http://localhost:5000/recommend', json={'user_id': 1})
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_invalid_user_id(self):
        response = requests.post('http://localhost:5000/recommend', json={'user_id': 'invalid'})
        self.assertEqual(response.status_code, 400)

    def test_missing_user_id(self):
        response = requests.post('http://localhost:5000/recommend')
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()