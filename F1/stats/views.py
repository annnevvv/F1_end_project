from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from stats.models import Constructors, Circuits, DriverStandings, Drivers, DriversResults


# Create your views here.

def constructors(request):
    constructors = Constructors.objects.all()
    return render(request, 'constructors.html', {'constructors': constructors})

def circuits(request):
    circuits = Circuits.objects.all()
    return render(request, 'circuits.html', {'circuits': circuits})


def driver_standings(request):
    standings = DriverStandings.objects.select_related('constructorid').all()
    return render(request, 'driver_standings.html', {'standings': standings})

def constructor_standings(request):
    standings = DriverStandings.objects.all()
    return render(request, 'constructor_standings.html', {'standings': standings})

def drivers(request: HttpRequest):
    drivers = Drivers.objects.all()
    return render(request, "drivers.html", {'drivers': drivers})


def driver_results(request, circuit_id=None):
    results = DriversResults.objects.all()

    if circuit_id:
        results = results.filter(circuitid__circuitid=circuit_id)

    context = {
        'results': results,
        'clicked_circuit_id': circuit_id
    }
    return render(request, 'driver_results.html', context)

def upcoming_races_view(request):
    upcoming_races = Circuits.get_upcoming_races()
    context = {
        'upcoming_races': upcoming_races
    }
    return render(request, 'upcoming_races.html', context)

