from django.test import TestCase
from django.urls import reverse


class MyURLTests(TestCase):


    def test_test_view(self):
        url = reverse('test_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello, World!')
