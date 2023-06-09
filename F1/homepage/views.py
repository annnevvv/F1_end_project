from django.shortcuts import render
import datetime
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import requests
from dateutil import tz
import pytz

from stats.models import Circuits
from stats.function_next_race import nextRace

from django.templatetags.static import static


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
        case 'Spielberg':
            return 'Knittelfeld'
        case whatever:
            return CITY_RACE


def raceTimer(city, day_race, time_race, timezone):
    race_time = datetime.datetime.strptime(f"{day_race} {time_race}",
                                           "%Y-%m-%d %H:%M:%S")

    geolocator = Nominatim(user_agent="my-app")
    location = geolocator.geocode(city)

    try:
        tf = TimezoneFinder()
        timezone_str = tf.timezone_at(lng=location.longitude,
                                      lat=location.latitude)
    except ValueError:
        print("No match for timezone for that city")

    city_timezone = tz.gettz(timezone_str)

    race_time = race_time.replace(tzinfo=city_timezone)
    local_race_time = race_time.astimezone(tz.tzlocal())

    local_race_time += datetime.timedelta(seconds=timezone)
    local_race_city_time = datetime.datetime.now(city_timezone)
    time_difference = local_race_time - local_race_city_time

    user_timezone = pytz.timezone('Europe/Warsaw')
    current_time = datetime.datetime.now(user_timezone)
    current_time = current_time + datetime.timedelta(hours=2)

    local_race_city_time = local_race_city_time + datetime.timedelta(hours=-4)

    return (
    local_race_time, local_race_city_time, time_difference, current_time)


def homePage(request):
    """Weather API for City race"""

    upcoming_races = Circuits.get_upcoming_races()
    DATA_RACE = nextRace(upcoming_races)
    CITY_RACE = DATA_RACE[0]
    TIME_RACE = str(DATA_RACE[1])
    DATE_RACE = DATA_RACE[2]
    CITY_RACE = matchCitiesToApi(CITY_RACE)

    appid = '490aa8f1a63ecf555ff9a003341030cf'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': CITY_RACE, 'appid': appid, 'units': 'metric'}
    requ = requests.get(url=URL, params=PARAMS)
    res = requ.json()

    SUN_RISE = int(res['sys']['sunrise'])
    SUN_SET = int(res['sys']['sunset'])
    TIMEZONE = res['timezone']

    data = raceTimer(CITY_RACE, DATE_RACE, TIME_RACE, TIMEZONE)
    RACE_DATA = data[0]
    TIME_IN_RACE_CITY_NOW = data[1]
    TIME_DELTA = str(data[2]).split('.', 2)[0][:-3]
    CURRENT_USER_TIME = data[3]

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
        'time_race': TIME_RACE,

        'RACE_DATA': RACE_DATA,
        'TIME_IN_RACE_CITY_NOW': TIME_IN_RACE_CITY_NOW,
        'TIME_DELTA': TIME_DELTA,
        'CURRENT_USER_TIME': CURRENT_USER_TIME
    }

    return render(request, 'homepage/homepage.html', context)


def about(request):
    return render(request, 'homepage/about.html')
