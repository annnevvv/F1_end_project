from django.test import TestCase
from django.urls import reverse
from .models import StatsDriverresult, Circuits, Constructors



class StatsUrlsTests(TestCase):  # pass
    def test_url_exists_at_correct_location(self):
        url = reverse("stats")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  # pass
        url = reverse("stats")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "stats/constructors.html")

    def test_template_content(self):  # pass
        url = reverse("stats")
        response = self.client.get(url)
        self.assertContains(response, "<h1>LIST OF CONSTRUCTORS IN 2023</h1>")
        self.assertNotContains(response, "Not on the page")


class StatsDriverresultModelTestCase(TestCase):  # bigfail
    databases = {'mySQL'}

    @classmethod
    def setUpTestData(cls):
        circuits = Circuits.objects.create(
            name='C01',
            country='CO',
            city='Montreal',
            date='2023-12-26',
            time='01:05:00',
        )


        StatsDriverresult.objects.create(
            driverid='1',
            driver='Michael Schumacher',
            position=1,
            points=25,
            constructor='Ferrari FXX',
            laps=50,
            circuitid=circuits
        )

    def test_stats_driverresult_fields(self):
        stats_driverresult = StatsDriverresult.objects.get(driverid=1)
        self.assertEqual(stats_driverresult.driverid, '1')
        self.assertEqual(stats_driverresult.driver, 'Michael Schumacher')
        self.assertEqual(stats_driverresult.position, 1)
        self.assertEqual(stats_driverresult.points, 25)
        self.assertEqual(stats_driverresult.constructor, 'Ferrari FXX')
        self.assertEqual(stats_driverresult.laps, 50)

