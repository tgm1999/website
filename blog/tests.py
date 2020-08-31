from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.db import models

from blog.views import post_list, cv_page, cv_new
from .models import CVEntry

# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, post_list)

class CVPageTest(TestCase):

    def test_cv_page_returns_correct_html(self):
        request = HttpRequest()
        response = cv_page(request)
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('\n<html>'))
        self.assertIn("<title>Thomas Mills</title>", html)
        self.assertTrue(html.endswith('</html>'))

    def test_each_entry_displays_correctly(self):
        request = HttpRequest()
        response = cv_page(request)
        html = response.content.decode('utf-8')
        for entry in CVEntry.objects.all():
            self.assertIn(entry.title, html)
            self.assertIn(entry.text, html)
            self.assertNotIn(entry.author, html)
            self.assertNotIn(entry.created_date, html)
            self.assertNotIn(entry.pk, html)
            self.assertNotIn(entry.published_date, html)

    def test_new_entry_button_resolves_to_new_entry_view(self):
        found = resolve('/cv/new/')
        self.assertEqual(found.func, cv_new)