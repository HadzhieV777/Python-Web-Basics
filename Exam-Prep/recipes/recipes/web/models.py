from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models


class Recipe(models.Model):
    TITLE_MAX_LENGTH = 30
    INGREDIENTS_MAX_LENGTH = 250

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )
    image_url = models.URLField()
    description = models.TextField(
        validators=[],
    )
    ingredients = models.CharField(
        max_length=INGREDIENTS_MAX_LENGTH,
        validators=[
            RegexValidator(
                regex=f'^[a-zA-Z]+(, [a-zA-Z]+)*$',
                message="The ingredients should be separated by ', '.",
            )
        ],
    )
    time = models.IntegerField()
