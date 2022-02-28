from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator
from django.db import models


class Profile(models.Model):
    USERNAME_MIN_LEN = 2
    USERNAME_MAX_LEN = 15

    VALIDATION_ERROR_MESSAGE = "Ensure this value contains only letters, numbers, and underscore."
    AGE_MIN_VALUE = 0

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=(
            MinLengthValidator(USERNAME_MIN_LEN),
            RegexValidator(r'^[\w_]+$', VALIDATION_ERROR_MESSAGE),
        ),
    )
    email = models.EmailField()
    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        ),
    )


class Album(models.Model):
    ALBUM_NAME_MAX_LEN = 30
    ARTIST_MAX_LEN = 30
    GENRE_MAX_LEN = 30
    PRICE_MIN_VALUE = 0

    POP_MUSIC = "Pop Music"
    JAZZ_MUSIC = "Jazz Music"
    RNB_MUSIC = "R&B Music"
    ROCK_MUSIC = "Rock Music"
    COUNTRY_MUSIC = "Country Music"
    DANCE_MUSIC = "Dance Music"
    HIP_HOP_MUSIC = "Hip Hop Music"
    OTHER = "Other"

    GENRES = [(x, x) for x in
              (POP_MUSIC, JAZZ_MUSIC, RNB_MUSIC, ROCK_MUSIC, COUNTRY_MUSIC, DANCE_MUSIC, HIP_HOP_MUSIC, OTHER)]

    name = models.CharField(
        max_length=ALBUM_NAME_MAX_LEN,
        unique=True,
    )
    artist = models.CharField(
        max_length=ARTIST_MAX_LEN,
    )
    genre = models.CharField(
        max_length=max(len(x) for (x, _) in GENRES),
        choices=GENRES,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image = models.URLField()
    price = models.FloatField(
        validators=(
            MinValueValidator(PRICE_MIN_VALUE),
        ),
    )