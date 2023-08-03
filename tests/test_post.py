import unittest
import requests
import json

class TestPost(unittest.TestCase):
    def test_get_post(self):
        response = requests.get('http://localhost:8080/posts/1')
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertEqual(json_response['id'], 1)

    def test_create_post(self):
        post_data = {'user_id': 1, 'content': 'This is a new post'}
        response = requests.post('http://localhost:8080/posts', json=post_data)
        self.assertEqual(response.status_code, 201)
        json_response = response.json()
        self.assertEqual(json_response['content'], post_data['content'])

    def test_repost(self):
        repost_data = {'user_id': 2, 'original_post_id': 1}
        response = requests.post('http://localhost:8080/posts/repost', json=repost_data)
        self.assertEqual(response.status_code, 201)
        json_response = response.json()
        self.assertEqual(json_response['original_post_id'], repost_data['original_post_id'])

if __name__ == '__main__':
    unittest.main()
