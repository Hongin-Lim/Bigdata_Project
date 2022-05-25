from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post
# Create your tests here.

class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_list(self):

        reponse = self.client.get('/blog/')
        self.assertEqual(reponse.status_code, 200)
        soup = BeautifulSoup(reponse.content, 'html.parser')
        self.assertEqual(soup.title.text, 'Blog')

