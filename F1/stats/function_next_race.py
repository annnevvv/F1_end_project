import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'F1.settings')
django.setup()

from stats.models import Circuits
from django.shortcuts import render



upcoming_races = Circuits.get_upcoming_races()

def nextRace():

    for race in upcoming_races:
            return (race.city, race.time)


