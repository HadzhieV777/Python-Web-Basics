from django.shortcuts import render, redirect

from notes.web.forms import CreateProfileForm, DeleteProfileForm, EditProfileForm, AddNoteForm, EditNoteForm, \
    DeleteNoteForm
from notes.web.models import Profile, Note


def get_profile():
    profiles = Profile.objects.all()

    if profiles:
        return profiles[0]
    return None


def show_index(request):
    profile = get_profile()
    notes = Note.objects.all()
    if not profile:
        return redirect('create profile')
    context = {
        'profile': profile,
        'notes': notes,
    }
    return render(request, 'home-with-profile.html', context)


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

    return render(request, 'home-no-profile.html', context)


def add_note(request):
    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddNoteForm()

    context = {
        'form': form,
    }

    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditNoteForm(instance=note)

    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteNoteForm(instance=note)

    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'note-delete.html', context)


def note_details(request, pk):
    note = Note.objects.get(pk=pk)

    context = {
        'note': note
    }
    return render(request, 'note-details.html', context)


def show_profile(request):
    profile = get_profile()
    notes = Note.objects.all()
    notes_count = len(notes)

    context = {
        'profile': profile,
        'notes_count': notes_count,
    }
    return render(request, 'profile.html', context)


def delete_profile(request):
    profile = get_profile()
    notes_count = len(Note.objects.all())

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
        'notes_count': notes_count,
    }
    return render(request, 'profile-delete.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show profile')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form
    }
    return render(request, 'profile-edit.html', context)
