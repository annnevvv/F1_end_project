from django.http import HttpResponseBadRequest
from django.shortcuts import render
from stats.models import Constructors, Circuits, DriverStandings, ConstructorStandings, Drivers, DriversResults

def stats(request):
    return render(request, 'stats/index.html')

def constructors(request):
    constructors = Constructors.objects.all()
    return render(request, 'stats/constructors.html', {'constructors': constructors})

def circuits(request):
    circuits = Circuits.objects.all()
    return render(request, 'stats/circuits.html', {'circuits': circuits})


def driver_standings(request):
    standings = DriverStandings.objects.all()
    race_no = DriversResults.get_last_race()
    context = {
        'standings': standings,
        'race_no': race_no
    }
    return render(request, 'stats/driver_standings.html', context)

def constructor_standings(request):
    standings = ConstructorStandings.objects.all()
    race_no = DriversResults.get_last_race()
    context = {
        'standings': standings,
        'race_no': race_no
    }
    return render(request, 'stats/constructor_standings.html', context)

def drivers(request):
    drivers = Drivers.objects.all()
    return render(request, "stats/drivers.html", {'drivers': drivers})


def driver_results(request, circuitid, circuit_name):
    results = DriversResults.objects.filter(circuitid=circuitid)
    if not results.exists():
        return HttpResponseBadRequest("<h1>Race has not yet taken place</h1>")

    context = {
        'results': results,
        'circuitid': circuitid,
        'circuit': {'name': circuit_name},
    }
    return render(request, 'stats/driver_results.html', context)

def upcoming_races_view(request):
    upcoming_races = Circuits.get_upcoming_races()
    context = {
        'upcoming_races': upcoming_races
    }
    return render(request, 'stats/upcoming_races.html', context)

