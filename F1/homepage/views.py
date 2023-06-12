from django.shortcuts import render
import datetime
import requests

from stats.models import Circuits
from stats.function_next_race import nextRace


# Create your views here.


# def homepage(request):
#     return render(request, 'homepage/homepage.html')

def matchCitiesToApi(CITY_RACE):
    match CITY_RACE:
        case 'Sakhir':
            return 'Awali'
        case 'Losail':
            return 'Doha'
        case 'Miami, FL':
            return 'Miami'
        case 'Austin, TX':
            return 'Austin'
        case 'Las Vegas, NV':
            return 'Las Vegas'
        case whatever:
            return CITY_RACE


def homePage(request):
    """Weather API for City race"""

    upcoming_races = Circuits.get_upcoming_races()
    CITY_RACE = nextRace(upcoming_races)[0]
    CITY_RACE = matchCitiesToApi(CITY_RACE)

    appid = '490aa8f1a63ecf555ff9a003341030cf'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': CITY_RACE, 'appid': appid, 'units': 'metric'}
    requ = requests.get(url=URL, params=PARAMS)
    res = requ.json()

    context = {
        'city': CITY_RACE,
        'icon': res['weather'][0]['icon'],
        'description': res['weather'][0]['description'],
        'temp': res['main']['temp'],
        'temp_min': res['main']['temp_min'],
        'temp_max': res['main']['temp_max'],
        'pressure': res['main']['pressure'],
        'humidity': res['main']['humidity'],
        'wind': res['wind']['speed'],
        'deg': res['wind']['deg'],
        'clouds': res['clouds']['all'],
        'country': res['sys']['country'],
        'sunrise': res['sys']['sunrise'],
        'sunset': res['sys']['sunset'],
        'timezone': res['timezone'],
        'day': datetime.date.today()
    }

    return render(request, 'homepage/homepage.html', context)
