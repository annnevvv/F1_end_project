from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Event

class EventsMainTests(TestCase):
    def test_url_exists_at_correct_location(self):
        url = reverse("events")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        url = reverse("events")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "events/index.html")

    def test_template_content(self):
        url = reverse("events")
        response = self.client.get(url)
        self.assertContains(response, "<h2>Event Location</h2>")
        self.assertNotContains(response, "Not on the page")
