from django.shortcuts import render, redirect

from .models import Event, Participant
from .forms import RegistrationForm

# Create your views here.

def index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {
        'events': events
    })


def event_details(request, event_slug):
    try:
        selected_event = Event.objects.get(slug=event_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_event.participants.add(participant)
                return redirect('confirm-registration', event_slug=event_slug)

        return render(request, 'events/event-details.html', {
            'event_found': True,
            'event': selected_event,
            'form': registration_form
        })

    except Exception as exc:
        return render(request, 'events/event-details.html', {
            'event_found': False
        })

def confirm_registration(request, event_slug):
    event = Event.objects.get(slug=event_slug)
    return render(request, 'events/registration-success.html', {
        'organizer_email': event.organizer_email
    })