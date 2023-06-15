import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'F1.settings')
django.setup()

from stats.models import Circuits

upcoming_races = Circuits.get_upcoming_races()


def nextRace(upcoming_races):
    for race in upcoming_races:
        return (race.city, race.time, race.date)
