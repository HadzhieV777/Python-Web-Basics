# Generated by Django 4.0.2 on 2022-02-22 12:20

import django.core.validators
from django.db import migrations, models
import expenses_tracker.web.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.RegexValidator('^[a-zA-Z]+$', 'Ensure this value contains only letters.')])),
                ('last_name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.RegexValidator('^[a-zA-Z]+$', 'Ensure this value contains only letters.')])),
                ('budget', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profiles/', validators=[expenses_tracker.web.validators.MaxFileSizeInMbValidator(5)])),
            ],
        ),
    ]
