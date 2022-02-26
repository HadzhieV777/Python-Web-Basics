from django.shortcuts import redirect, render

from petstagram.web.forms import CreatePetForm, EditPetForm, DeletePetForm
from petstagram.web.helpers import get_profile
from petstagram.web.models import Pet


def add_pet(request):
    pet = Pet(user_profile=get_profile())
    if request.method == 'POST':
        form = CreatePetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = CreatePetForm(instance=pet)

    context = {
        'form': form,
    }
    return render(request, 'pet_create.html', context)


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditPetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = EditPetForm(instance=pet)

    context = {
        'form': form,
        'pet': pet,
    }

    return render(request, 'pet_edit.html', context)


def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeletePetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = DeletePetForm(instance=pet)

    context = {
        'form': form,
        'pet': pet,
    }
    return render(request, 'pet_delete.html', context)
