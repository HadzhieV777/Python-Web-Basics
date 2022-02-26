from django.shortcuts import redirect, render

from petstagram.web.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from petstagram.web.helpers import get_profile
from petstagram.web.models import Pet, PetPhoto


def show_profile(request):
    profile = get_profile()
    pets = list(Pet.objects.filter(user_profile=profile))

    if not profile:
        return redirect('unauthorized')

    pet_photos = PetPhoto.objects.filter(tagged_pets__in=pets).distinct()
    # pets = Pet.objects.filter(user_profile=profile)
    # pet_photos = PetPhoto.objects.filter(tagged_pets__user_profile=profile).distinct()
    # it's possible to do it without taking Pet obj but this will add
    # one more query to the DB and the query will be slower

    total_likes_count = sum(pp.likes for pp in pet_photos)
    total_pet_photos_count = len(pet_photos)

    context = {
        'profile': profile,
        'total_likes_count': total_likes_count,
        'total_pet_photos_count': total_pet_photos_count,
        'pets': pets,
    }

    return render(request, 'profile_details.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }
    return render(request, 'profile_create.html', context)


def edit_profile(request):
    profile = get_profile()
    if not profile:
        return redirect('unauthorized')

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profile_edit.html', context)


def delete_profile(request):
    profile = get_profile()
    if not profile:
        return redirect('unauthorized')

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'profile_delete.html')
