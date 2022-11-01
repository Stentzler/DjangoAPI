# Generated by Django 4.1.2 on 2022-11-01 14:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exams", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="exams",
            name="name",
        ),
        migrations.AddField(
            model_name="exams",
            name="score",
            field=models.PositiveIntegerField(
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(100),
                ],
            ),
        ),
    ]
