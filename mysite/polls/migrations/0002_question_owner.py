# Generated by Django 4.1.5 on 2024-05-15 07:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='owner',
            field=models.CharField(blank=True, max_length=200, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(10)]),
        ),
    ]
