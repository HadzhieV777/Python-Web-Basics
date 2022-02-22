from django import forms

from notes.web.models import Profile, Note


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'image_url': 'Link to Profile Page',
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        Note.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content', 'image')
        labels = {
            'title': 'Title',
            'content': 'Content',
            'image': 'Link to Image',
        }


class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content', 'image')
        labels = {
            'title': 'Title',
            'content': 'Content',
            'image': 'Link to Image',
        }


class DeleteNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Note
        fields = ('title', 'content', 'image')
        labels = {
            'title': 'Title',
            'content': 'Content',
            'image': 'Link to Image',
        }
