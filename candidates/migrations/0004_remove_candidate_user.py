# Generated by Django 4.2.5 on 2023-09-20 08:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("candidates", "0003_candidate_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="candidate",
            name="user",
        ),
    ]
