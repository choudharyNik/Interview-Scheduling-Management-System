# Generated by Django 4.2.5 on 2023-09-19 14:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("requirements", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="requirement",
            name="title",
            field=models.CharField(default="Title", max_length=100),
        ),
    ]
