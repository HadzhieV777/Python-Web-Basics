from django.shortcuts import render

from online_library.main.helpers import get_profile
from online_library.main.models import Book


def home(request):
    profile = get_profile()
    books = Book.objects.all()
    template_to_show = ''

    if profile is None:
        template_to_show = 'home-no-profile.html'
    else:
        template_to_show = 'home-with-profile.html'

    context = {
        'profile': profile,
        'books': books,
    }

    return render(request, template_to_show, context)