from django import forms

from online_library.main.models import Profile, Book


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = {'first_name', 'last_name', 'image_url'}
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name',
                }
            ),
            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'URL',
                }
            ),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['image_url'].required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = {'first_name', 'last_name', 'image_url'}
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'disabled': 'disabled',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'disabled': 'disabled',
                }
            ),
            'image_url': forms.TextInput(
                attrs={
                    'disabled': 'disabled',
                }
            ),
        }


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Title',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                }
            ),
            'image': forms.TextInput(
                attrs={
                    'placeholder': 'Image',
                }
            ),
            'type': forms.TextInput(
                attrs={
                    'placeholder': 'Fiction, Novel, Crime..',
                }
            ),
        }


class BookDetailsForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class BookEditForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Title',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                }
            ),
            'image': forms.TextInput(
                attrs={
                    'placeholder': 'Image',
                }
            ),
            'type': forms.TextInput(
                attrs={
                    'placeholder': 'Fiction, Novel, Crime..',
                }
            ),
        }


class BookDeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].required = False
        self.fields['description'].required = False
        self.fields['image'].required = False
        self.fields['type'].required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Book
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'disabled': 'disabled',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'disabled': 'disabled',
                }
            ),
            'image': forms.TextInput(
                attrs={
                    'disabled': 'disabled',
                }
            ),
            'type': forms.TextInput(
                attrs={
                    'disabled': 'disabled',
                }
            ),
        }
