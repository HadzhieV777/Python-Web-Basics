from django.urls import path

from online_library.main.views.book_actions import add_book, edit_book, book_details, delete_book
from online_library.main.views.generic_views import home
from online_library.main.views.profile_actions import show_profile, edit_profile, delete_profile, create_profile

urlpatterns = (
    path('', home, name='index'),

    path('add/', add_book, name='add book'),
    path('edit/<int:pk>/', edit_book, name='edit book'),
    path('details/<int:pk>/', book_details, name='book details'),
    path('delete/<int:pk>/', delete_book, name='delete book'),

    path('profile/create', create_profile, name='create profile'),
    path('profile/', show_profile, name='show profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)
