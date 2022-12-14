# Generated by Django 4.1.2 on 2022-10-20 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0002_remove_dream_steps_step"),
    ]

    operations = [
        migrations.CreateModel(
            name="Resource",
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
                ("name", models.CharField(max_length=100)),
                ("url", models.CharField(max_length=100)),
                ("description", models.TextField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name="dream",
            name="resources",
            field=models.ManyToManyField(to="main_app.resource"),
        ),
    ]
