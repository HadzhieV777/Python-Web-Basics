from django.contrib import admin
from django.urls import path

from my_music_app.web.views import homepage, add_album, album_details, album_edit, album_delete, profile_create, \
    profile_details, profile_delete

urlpatterns = (
    path('', homepage, name='homepage'),

    path('album/add/', add_album, name='add album'),
    path('album/details/<int:pk>/', album_details, name='album details'),
    path('album/edit/<int:pk>/', album_edit, name='album edit'),
    path('album/delete/<int:pk>/', album_delete, name='album delete'),

    path('profile/create/', profile_create, name='profile create'),
    path('profile/details/', profile_details, name='profile details'),
    path('profile/delete/', profile_delete, name='profile delete'),
)

