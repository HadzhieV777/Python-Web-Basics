from django.shortcuts import render, redirect

from online_library.main.forms import AddBookForm, BookEditForm, BookDeleteForm
from online_library.main.models import Book


def book_action(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)

    context = {
        'form': form,
        'book': instance,
    }

    return render(request, template_name, context)


def add_book(request):
    return book_action(request, AddBookForm, 'index', Book(), 'add-book.html')


def edit_book(request, pk):
    return book_action(request, BookEditForm, 'index', Book.objects.get(pk=pk), 'edit-book.html')


def book_details(request, pk):
    book = Book.objects.get(pk=pk)

    context = {
        'book': book
    }
    return render(request, 'book-details.html', context)


def delete_book(request, pk):
    return book_action(request, BookDeleteForm, 'index', Book.objects.get(pk=pk), 'delete-book.html')
