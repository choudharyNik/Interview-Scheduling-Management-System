# Generated by Django 4.2.5 on 2023-09-21 13:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("requirements", "0003_requirement_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="requirement",
            name="vacancies",
            field=models.PositiveIntegerField(),
        ),
    ]