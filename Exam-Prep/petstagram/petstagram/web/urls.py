from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path

from petstagram.web.views.generic import show_home, show_dashboard, show_unauthorized
from petstagram.web.views.pets import add_pet, edit_pet, delete_pet
from petstagram.web.views.pets_photos import show_pet_photo_details, like_pet_photo, add_photo, edit_photo, delete_photo
from petstagram.web.views.profile import create_profile, show_profile, edit_profile, delete_profile

urlpatterns = [
                  path('', show_home, name='index'),
                  path('dashboard/', show_dashboard, name='dashboard'),
                  path('unauthorized/', show_unauthorized, name='unauthorized'),

                  path('profile/create/', create_profile, name='create profile'),
                  path('profile/', show_profile, name='profile details'),
                  path('profile/edit/', edit_profile, name='edit profile'),
                  path('profile/delete/', delete_profile, name='delete profile'),

                  path('pet/add/', add_pet, name='add pet'),
                  path('pet/edit/<int:pk>/', edit_pet, name='edit pet'),
                  path('pet/delete/<int:pk>/', delete_pet, name='delete pet'),

                  path('photo/add/', add_photo, name='add photo'),
                  path('photo/edit/<int:pk>/', edit_photo, name='edit photo'),
                  path('photo/delete/<int:pk>/', delete_photo, name='delete photo'),
                  path('photo/details/<int:pk>/', show_pet_photo_details, name='pet photo details'),
                  path('photo/like/<int:pk>/', like_pet_photo, name='like pet photo'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
