# Generated by Django 4.1.3 on 2022-11-10 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("custom_users", "0001_initial"),
        ("grades", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="grade",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="grades.grade"
            ),
        ),
    ]
