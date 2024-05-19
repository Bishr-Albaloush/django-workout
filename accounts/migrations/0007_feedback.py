# Generated by Django 4.2.11 on 2024-05-19 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("exercise", "0004_muscle_rename_exerxise_practice_exercise_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("accounts", "0006_alter_profile_blankduration"),
    ]

    operations = [
        migrations.CreateModel(
            name="FeedBack",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "text",
                    models.IntegerField(
                        choices=[
                            (1, "Foolproof"),
                            (2, "Easy"),
                            (3, "Normal"),
                            (4, "Difficult"),
                            (5, "Fiendish"),
                        ]
                    ),
                ),
                (
                    "muscle",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="exercise.muscle",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
