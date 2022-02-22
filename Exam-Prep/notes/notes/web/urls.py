from django.urls import path

from notes.web.views import show_index, create_profile, add_note, edit_note, delete_note, note_details, \
    show_profile, delete_profile, edit_profile

urlpatterns = (
    path('', show_index, name='index'),
    path('unregistered/', create_profile, name='create profile'),

    path('add/', add_note, name='add note'),
    path('edit/<int:pk>/', edit_note, name='edit note'),
    path('delete/<int:pk>/', delete_note, name='delete note'),
    path('details/<int:pk>/', note_details, name='note details'),

    path('profile/', show_profile, name='show profile'),
    path('delete-profile', delete_profile, name='delete profile'),
    path('edit-profile', edit_profile, name='edit profile'),
)
