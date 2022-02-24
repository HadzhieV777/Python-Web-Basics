from django.shortcuts import render, redirect

from online_library.main.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from online_library.main.helpers import get_profile
from online_library.main.models import Profile


def show_profile(request):
    profile = get_profile()

    context = {
        'profile': profile
    }
    return render(request, 'profile.html', context)


def profile_action(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)

    context = {
        'form': form,
    }

    return render(request, template_name, context)


def create_profile(request):
    return profile_action(request, CreateProfileForm, 'index', Profile(), 'home-with-profile.html')


def edit_profile(request):
    return profile_action(request, EditProfileForm, 'show profile', get_profile(), 'edit-profile.html')


def delete_profile(request):
    return profile_action(request, DeleteProfileForm, 'index', get_profile(), 'delete-profile.html')
