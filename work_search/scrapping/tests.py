from django.test import TestCase
from django.urls import resolve
from .views import home_view
from django.http import HttpRequest

from selenium import webdriver
import unittest

# browser = webdriver.Firefox()
# browser.get('http://localhost:8000')


# class NewVisitorTest(unittest.TestCase):
#     '''test new user'''
#
#     def setUp(self):
#         self.browser = webdriver.Firefox()
#
#     def tearDown(self):
#         self.browser.quit()
#
#     def test_can_start_a_list_and_retrieve_it_later(self):
#         self.browser.get('http://localhost:8000')
#         self.assertIn('home', self.browser.title)
#         self.fail('Finish test!')
#
#
# if __name__ == '__main__':
#     unittest.main(warnings='ignore')


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_view)


    def test_home_page_returns_correct_html(self):
        """Home page returns correct html"""

        request = HttpRequest()
        response = home_view(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!doctype html>'))
        self.assertIn('<title>home</title>', html)
        self.assertTrue(html.endswith('</html>'))