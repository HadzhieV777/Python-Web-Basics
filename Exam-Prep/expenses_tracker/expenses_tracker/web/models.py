from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator
from django.db import models

# alphaSpaces = RegexValidator(r'^[a-zA-Z]+$', "Ensure this value contains only letters.")
from expenses_tracker.web.validators import MaxFileSizeInMbValidator


class Profile(models.Model):
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LENGTH = 15

    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LENGTH = 15
    ONLY_LETTERS_VALIDATOR_ERROR = "Ensure this value contains only letters."

    BUDGET_DEFAULT_VALUE = 0
    BUDGET_MIN_VALUE = 0

    IMAGE_UPLOAD_TO_DIR = 'profiles/'
    IMAGE_MAX_SIZE_IN_MB = 5

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            RegexValidator(r'^[a-zA-Z]+$', ONLY_LETTERS_VALIDATOR_ERROR),
        ),
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            RegexValidator(r'^[a-zA-Z]+$', ONLY_LETTERS_VALIDATOR_ERROR),
        ),
    )
    budget = models.FloatField(
        default=BUDGET_DEFAULT_VALUE,
        validators=(
            MinValueValidator(BUDGET_MIN_VALUE),
        ),
    )
    profile_image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        ),
    )


class Expense(models.Model):
    TITLE_MAX_LENGTH = 30

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )
    image = models.URLField()
    description = models.TextField(
        null=True,
        blank=True,
    )
    price = models.FloatField()

    class Meta:
        ordering = ('title', 'price',)
