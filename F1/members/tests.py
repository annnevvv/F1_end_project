from django.test import TestCase

from .forms import RegistrationForm


# Create your tests here.


class RegistrationFormTestCase(TestCase): #pass
    def test_registration_form_valid(self):
        form_data = {
            'username': 'Tim123',
            'email': 'tim@op.com',
            'password1': 'TestPass1!',
            'password2': 'TestPass1!',
        }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_registration_form_invalid(self):
        form_data = {
            'username': 'te',
            'email': '@email',
            'password1': 'test',
            'password2': 'pest',
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)
        self.assertIn('email', form.errors)
        self.assertIn('password2', form.errors)


class RegistrationFormFixtureTestCase(TestCase): #pass
    fixtures = ['members.json']
    def test_registration_form_valid(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_registration_form_invalid(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword1',
            'password2': 'testpassword2'
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())