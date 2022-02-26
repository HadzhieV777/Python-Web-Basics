from django.shortcuts import render, redirect

from petstagram.web.forms import AddPhotoForm, EditPhotoForm, DeletePhotoForm
from petstagram.web.models import PetPhoto


def add_photo(request):
    if request.method == 'POST':
        form = AddPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AddPhotoForm()

    context = {
        'form': form,
    }
    return render(request, 'photo_create.html', context)


def edit_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditPhotoForm(request.POST, instance=pet_photo)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditPhotoForm(instance=pet_photo)

    context = {
        'form': form,
        'pet_photo': pet_photo,
    }
    return render(request, 'photo_edit.html', context)


def delete_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeletePhotoForm(request.POST, instance=pet_photo)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditPhotoForm(instance=pet_photo)

    context = {
        'form': form,
        'pet_photo': pet_photo,
    }
    return render(request, 'photo_delete.html', context)


def show_pet_photo_details(request, pk):
    pet_photo = PetPhoto.objects \
        .prefetch_related('tagged_pets') \
        .get(pk=pk)

    context = {
        'pet_photo': pet_photo,
    }
    return render(request, 'photo_details.html', context)


def like_pet_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()

    return redirect('pet photo details', pk)
