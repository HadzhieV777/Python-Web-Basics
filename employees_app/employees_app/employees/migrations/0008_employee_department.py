# Generated by Django 4.0.1 on 2022-01-30 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_department_alter_employee_egn'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(default=1 , on_delete=django.db.models.deletion.CASCADE, to='employees.department'),
            preserve_default=False,
        ),
    ]
