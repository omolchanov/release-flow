import unittest
from src.app import app


class EmailRouteTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_feature_email(self):
        response = self.client.get('/email')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"message": "Emails have been sent"})


if __name__ == '__main__':
    unittest.main()
