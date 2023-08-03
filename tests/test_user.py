import unittest
import requests

class TestUser(unittest.TestCase):
    def test_get_user_posts(self):
        response = requests.get('http://localhost:8080/users/user1/posts')
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertTrue(isinstance(json_response, list))
        self.assertTrue(all('id' in post for post in json_response))

    def test_get_user(self):
        response = requests.get('http://localhost:8080/users/user1')
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertEqual(json_response['id'], 1)
        self.assertTrue(isinstance(json_response['posts'], list))

if __name__ == '__main__':
    unittest.main()
