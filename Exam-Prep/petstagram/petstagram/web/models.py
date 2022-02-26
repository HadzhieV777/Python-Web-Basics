import datetime
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.web.validators import MaxFileSizeInMbValidator


def only_letters_validator(value):
    if not value.isalpha():
        raise ValidationError('This fields should consist only of letters!')
    return value


def validate_file_max_size(value):
    max_size = 5

    filesize = value.file.size
    if filesize > max_size * 1024 * 1024:
        raise ValidationError("Max file size is %sMB" % str(max_size))

    return value


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30

    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    MALE = 'Male'
    FEMALE = 'Female'
    DO_OT_SHOW = 'Do not show'

    GENDERS = [
        (x, x) for x in (MALE, FEMALE, DO_OT_SHOW)
    ]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            only_letters_validator,
            # RegexValidator(
            #     regex='^[a-zA-Z]*$',
            #     message="Letters only.",
            # )
        ),
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            only_letters_validator,
            # RegexValidator(
            #     regex='^[a-zA-Z]*$',
            #     message="Letters only.",
            # )
        ),
    )
    profile_picture = models.URLField()
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    email = models.EmailField(
        null=True,
        blank=True,
    )
    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Pet(models.Model):
    PET_NAME_MAX_LENGTH = 30

    CAT = "Cat"
    DOG = "Dog"
    BUNNY = "Bunny"
    PARROT = "Parrot"
    FISH = "Fish"
    OTHER = "Other"

    TYPES = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]

    name = models.CharField(
        max_length=PET_NAME_MAX_LENGTH,
    )
    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    # To link the current pet to a user profile(one to many)
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name}'

    # To make the pet name unique
    class Meta:
        unique_together = ('user_profile', 'name')


class PetPhoto(models.Model):
    MAX_FILE_SIZE = 5

    photo = models.ImageField(
        upload_to='profiles/',
        validators=(
            MaxFileSizeInMbValidator(MAX_FILE_SIZE),
        ),
    )
    tagged_pets = models.ManyToManyField(
        Pet,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    publication_date = models.DateTimeField(
        auto_now_add=True,
        # when a picture is created (only), the date and time of publication are automatically generated.
    )
    likes = models.IntegerField(
        default=0,
    )
