from datetime import date

from django import forms
from django.forms import HiddenInput

from petstagram.web.helpers import BootstrapFormsMixin
from petstagram.web.models import Profile, Pet, PetPhoto

# profiles
from petstagram.web.validators import MaxDateValidator


class CreateProfileForm(forms.ModelForm, BootstrapFormsMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'profile_picture')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                    # 'class': 'form-control', setting the class without our Mixin
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            ),
            'profile_picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL'
                }
            ),
        }


class EditProfileForm(forms.ModelForm, BootstrapFormsMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.initial['gender'] = Profile.DO_OT_SHOW

    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter email',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter description',
                    'rows': 3,
                },
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'min': '1920-01-01',
                }
            )
        }


class DeleteProfileForm(forms.ModelForm, BootstrapFormsMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


# pets
class CreatePetForm(BootstrapFormsMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter pet name',
                }
            ),
        }


class EditPetForm(BootstrapFormsMixin, forms.ModelForm):
    MIN_DATE_OF_BIRTH = date(1920, 1, 1)
    MAX_DATE_OF_BIRTH = date.today()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def clean_date_of_birth(self):
        MaxDateValidator(date.today())(self.cleaned_data['date_of_birth'])
        return self.cleaned_data['date_of_birth']

    class Meta:
        model = Pet
        exclude = ('user_profile',)


class DeletePetForm(forms.ModelForm, BootstrapFormsMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Pet
        exclude = ('user_profile',)


# photos
class AddPhotoForm(BootstrapFormsMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        # for _, field in self.fields.items():
        #     field.required = False

    class Meta:
        model = PetPhoto
        fields = ('photo', 'description', 'tagged_pets')
        labels = {
            'photo': 'Pet Image',
            'description': 'Description',
            'tagged_pets': 'Tag Pets',
        }


class EditPhotoForm(BootstrapFormsMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = PetPhoto
        fields = ('description', 'tagged_pets')
        labels = {
            'description': 'Description',
            'tagged_pets': 'Tag Pets',
        }


class DeletePhotoForm(forms.ModelForm, BootstrapFormsMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = PetPhoto
        fields = ()
        # widgets = {
        #     'photo': HiddenInput(),
        #     'description': HiddenInput(),
        #     'tagged_pets': HiddenInput(),
        # }
