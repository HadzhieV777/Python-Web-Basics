from django.shortcuts import render, redirect

from petstagram.web.helpers import get_profile
from petstagram.web.models import PetPhoto


def show_home(request):
    context = {
        'hide_additional_nav_items': True,
    }
    return render(request, 'home_page.html', context)


def show_unauthorized(request):
    return render(request, '401_error.html')


def show_dashboard(request):
    profile = get_profile()
    if not profile:
        return redirect('unauthorized')
    # pets = profile.pet_set.all()  # The pet_set comes from the relation between the user profile and the pet models
    pet_photos = set(PetPhoto.objects.filter(tagged_pets__user_profile=profile))

    context = {
        'pet_photos': pet_photos,
    }
    return render(request, 'dashboard.html', context)
