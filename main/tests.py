from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from .views import home
from django.test import Client
from selenium import webdriver


# Check homepage exists
class HomePageTest(TestCase):
    def test_url_resolves_to_homepage(self):
        found = resolve('/')
        self.assertEqual(found.func, home)


# Check mimetype of page if it's image
class CheckMimeTypeTest(TestCase):
    def test_if_mimetype_is_image(self):
        self.client = Client()
        response = self.client.get('/default/')
        self.assertEqual(response['Content-Type'], 'image/png')


# Check image size of response if matches requested
class DimensionTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/home/khophi/Downloads/chromedriver')

    def tearDown(self):
        self.browser.quit()

    def test_check_dimension_of_image_if_matches_request(self):
        self.browser.get('http://localhost:8000/default/')
        img = self.browser.find_element_by_tag_name('img')
        width, height = img.size['width'], img.size['height']
        self.assertEqual([width, height], [500, 500])
