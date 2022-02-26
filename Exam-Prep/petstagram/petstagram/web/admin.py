from django.contrib import admin

from petstagram.web.models import Profile, Pet, PetPhoto


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


@admin.register(PetPhoto)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('publication_date', 'likes')
