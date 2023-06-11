from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from stats.models import Constructors, Circuits, DriverStandings, ConstructorStandings, Drivers, DriversResults


def constructors(request):
    constructors = Constructors.objects.all()
    return render(request, 'constructors.html', {'constructors': constructors})

def circuits(request):
    circuits = Circuits.objects.all()
    return render(request, 'circuits.html', {'circuits': circuits})


def driver_standings(request):
    standings = DriverStandings.objects.select_related('constructorid').all()
    race_no = DriversResults.get_last_race()
    context = {
        'standings': standings,
        'race_no': race_no
    }
    return render(request, 'driver_standings.html', context)

def constructor_standings(request):
    standings = ConstructorStandings.objects.select_related('constructorid').all()
    race_no = DriversResults.get_last_race()
    context = {
        'standings': standings,
        'race_no': race_no
    }
    return render(request, 'constructor_standings.html', context)

def drivers(request):
    drivers = Drivers.objects.all()
    return render(request, "drivers.html", {'drivers': drivers})


def driver_results(request, circuitid):
    results = DriversResults.objects.select_related('circuitid').all()
    circuit = Circuits.objects.get(circuitid=circuitid)
    circuit_name = circuit.name
    context = {
        'results': results,
        'circuitid': circuitid,
        'circuit_name': circuit_name,
    }
    return render(request, 'driver_results.html', context)

def upcoming_races_view(request):
    upcoming_races = Circuits.get_upcoming_races()
    context = {
        'upcoming_races': upcoming_races
    }
    return render(request, 'upcoming_races.html', context)
