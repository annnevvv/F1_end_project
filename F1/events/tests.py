from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Event, Circuit


class EventsMainTests(TestCase):  # pass
    def test_url_exists_at_correct_location(self):
        url = reverse("events")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        url = reverse("events")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "events/index.html")

    def test_template_content(self):  # pass
        url = reverse("events")
        response = self.client.get(url)
        self.assertContains(response, "<h2>All Events</h2>")
        self.assertNotContains(response, "Not on the page")


class EventModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='Jey123',
                                   email='jay@op.pl',
                                   password='Pies123!')
        circuit = Circuit.objects.create(name='TestCircuits01',
                                         location='Baku')

        cls.event = Event.objects.create(
            title='TestEvent01',
            organizer_email='email@gmail.com',
            date='2023-09-11',
            slug='event-one',
            description='Lorem ipsum dolor sit amet.',
            image='posts/F1.png',
            circuit=circuit,
        )

        cls.event.user.set([user])

    def test_event_str_representation(self):  # pass
        self.assertEqual(str(self.event), 'TestEvent01 - 2023-09-11')

    def test_event_field(self):  # pass
        self.assertEqual(self.event.title, 'TestEvent01')
        self.assertEqual(self.event.organizer_email, 'email@gmail.com')
        self.assertEqual(self.event.date, '2023-09-11')
        self.assertEqual(self.event.slug, 'event-one')
        self.assertEqual(self.event.description, 'Lorem ipsum dolor sit amet.')
        self.assertEqual(self.event.image, 'posts/F1.png')
        self.assertEqual(self.event.circuit.name, 'TestCircuits01')

        user_list = [user.username for user in self.event.user.all()]

        self.assertCountEqual(user_list, ['Jey123'])

    def test_event_str_representation(self):
        expected_str = 'TestEvent01 - 2023-09-11'
        self.assertEqual(str(self.event), expected_str)
