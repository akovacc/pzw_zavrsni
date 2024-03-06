from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
from main.models import Author
# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse('homepage')

class Testmodels(TestCase):

	def setUp(self):
		self.author1 = Author.objects.create(
			name = "Mario",
			surname = "neko-prezime",
			email = "mail",
			phone_number = "KB"
		)
	def test_author(self):
		self.assertEqual(self.author1.name, "Mario")
		