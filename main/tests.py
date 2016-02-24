from django.test import TestCase
from django.core.urlresolvers import resolve
from .views import homepage
from selenium import webdriver


# Check homepage exists
class HomePageTest(TestCase):
    def test_url_resolves_to_homepage(self):
        home = resolve('/')
        self.assertEqual(home.func, homepage)


# Check mimetype of page if it's image
class ImageMimeTypeTest(TestCase):
    def test_if_mimetype_is_image(self):
        response = self.client.get('/250')
        self.assertEqual(response['Content-Type'], 'image/gif')

    def test_if_mimetype_matches_requested(self):
        test_jpg = self.client.get('/250.jpg')
        test_png = self.client.get('/250.png')
        self.assertEqual(test_jpg['Content-Type'], 'image/jpg')
        self.assertEqual(test_png['Content-Type'], 'image/png')
        # test_gif was done in previous test since
        # is the default

# It is a bit harder to check for the texts on the images
# generated. A way to read and determine the color
# of the generated image will be great. But perhaps, overkill?


# In browser test
# Check image size of response if matches requested
# Using Selenium
class ImageDimensionTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/home/khophi/Downloads/chromedriver')

    def tearDown(self):
        self.browser.quit()

    def test_check_dimension_of_image_if_matches_request(self):
        # You must have app running on localhost:8000
        self.browser.get('http://localhost:8000/500')
        img = self.browser.find_element_by_tag_name('img')
        width, height = img.size['width'], img.size['height']
        self.assertEqual([width, height], [500, 500])
