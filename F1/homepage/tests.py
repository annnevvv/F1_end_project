from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class HomepageAboutPageTestsCase(TestCase): #pass
    def test_url_exists_at_correct_location(self):
        url = reverse("about")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        url = reverse("about")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "homepage/about.html")

    def test_template_content(self): #pass
        url = reverse("about")
        response = self.client.get(url)
        self.assertContains(response, "ABOUT PROJECT")
        self.assertNotContains(response, "Not on the page")
