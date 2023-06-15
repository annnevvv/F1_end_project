from django.test import TestCase
from django.urls import reverse
from .models import StatsDriverresult, Circuits


class StatsUrlsTestsCase(TestCase):
    def test_url_exists_at_correct_location(self): # pass
        url = reverse("stats")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  # pass
        url = reverse("stats")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "stats/index.html")

    def test_template_content(self):  # pass
        url = reverse("stats")
        response = self.client.get(url)
        self.assertContains(response, "F1 STATISTICS 2023")
        self.assertNotContains(response, "Not on the page")


class StatsDriverresultModelTestCase(TestCase): #bigfail
    databases = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'test_database_name',
        },
        'mySQL': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'formula1',
            'USER': 'root',
            'PASSWORD': 'Ania123!',
            'HOST': 'localhost',
            'PORT': '3306',
        },
    }

    @classmethod
    def setUpTestData(cls):
        circuits = Circuits.objects.create(
            circuitid='co1',
            # Field name made lowercase. db_column='circuitID' - co to z referencja ?
            name='C01',
            country='CO',
            city='Montreal',
            date='2023-12-26',
            time='01:05:00',
        )

        StatsDriverresult.objects.create(
            driverid=1,
            driver='Michael Schumacher',
            position=1,
            points=25,
            constructor='Ferrari FXX',
            laps=50,
            circuitid=circuits
        )

    def test_stats_driverresult_fields(self):
        stats_driverresult = StatsDriverresult.objects.get(driverid=1)
        self.assertEqual(stats_driverresult.driverid, 1)
        self.assertEqual(stats_driverresult.driver, 'Michael Schumacher')
        self.assertEqual(stats_driverresult.position, 1)
        self.assertEqual(stats_driverresult.points, 25)
        self.assertEqual(stats_driverresult.constructor, 'Ferrari FXX')
        self.assertEqual(stats_driverresult.laps, 50)
        self.assertEqual(stats_driverresult.circuitid, 1)
