from django import forms
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

from my_music_app.web.models import Profile, Album


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age')
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'label': 'Username',
                    'placeholder': 'Username'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'label': 'Email',
                    'placeholder': 'Email'
                }
            ),
            'age': forms.TextInput(
                attrs={
                    'label': 'Age',
                    'placeholder': 'Age'
                }
            ),
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        Album.objects.all().delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class AddAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('name', 'artist', 'genre', 'description', 'image', 'price')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name'
                },
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist'
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Description'
                }
            ),
            'image': forms.TextInput(
                attrs={
                    'placeholder': 'Image URL'
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Price'
                }
            ),

        }
        labels = {
            'name': 'Album Name',
            'artist': 'Artist',
            'description': 'Description',
            'image': 'Image URL',
            'price': 'Price',
            'genre': 'Genre',
        }


class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('name', 'artist', 'genre', 'description', 'image', 'price')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name'
                },
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist'
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Description'
                }
            ),
            'image': forms.TextInput(
                attrs={
                    'placeholder': 'Image URL'
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Price'
                }
            ),

        }
        labels = {
            'name': 'Album Name',
            'artist': 'Artist',
            'description': 'Description',
            'image': 'Image URL',
            'price': 'Price',
            'genre': 'Genre',
        }


class DeleteAlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = ('name', 'artist', 'genre', 'description', 'image', 'price')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name'
                },
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist'
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Description'
                }
            ),
            'image': forms.TextInput(
                attrs={
                    'placeholder': 'Image URL'
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Price'
                }
            ),

        }
        labels = {
            'name': 'Album Name',
            'artist': 'Artist',
            'description': 'Description',
            'image': 'Image URL',
            'price': 'Price',
            'genre': 'Genre',
        }
