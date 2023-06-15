from django import forms
from django.contrib.auth.models import User


class RegistrationForEventForm(forms.Form):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
