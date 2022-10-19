from django.test import TestCase

class SimpleTest(TestCase):
    def test_details(self):
        response = self.client.get('home')
        self.assertEqual(response.status_code, 200)
