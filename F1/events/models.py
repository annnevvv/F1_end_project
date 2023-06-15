from django.db import models
from django.contrib.auth.models import User


class Circuit(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} ({self.location})'


class Event(models.Model):
    title = models.CharField(max_length=200)
    organizer_email = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='events/images')
    circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE)
    user = models.ManyToManyField(User, blank=True, null=True)

    def __str__(self):
        return f'{self.title} - {self.date}'
