from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Meetups, Participants
from .forms import RegistrationForm


# Create your views here.


def index(request):
    meetups = Meetups.objects.all()
    return render(request, 'meetups/index.html', {
        'meetups': meetups
    })


def meetup_detail(request, meetup_slug):
    try:
        print(meetup_slug)
        selected_meetups = Meetups.objects.get(slug=meetup_slug)
        print(selected_meetups)
        if request.method == 'GET':
            registration_form = RegistrationForm()

        else:
            print('T2')
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participants.objects.get_or_create(email=user_email)
                selected_meetups.participants.add(participant)
                print('T1')
                return redirect('confirm-registration', meetup_slug=meetup_slug)
        return render(request, 'meetups/Meetup_detail.html', {
            'meetup_found': True,
            'meetup': selected_meetups,
            'form': registration_form
        })
    except Exception as exc:
        print(exc)
        return render(request, 'meetups/Meetup_detail.html',
                      {'meetup_found': False})


def confirm_registration(request, meetup_slug):
    meetups = Meetups.objects.get(slug=meetup_slug)
    return render(request, 'meetups/register-success.html', {
        'organizer_email': meetups.organizer_email
    })
