# Generated by Django 4.1.5 on 2023-02-27 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("selfServiceApp", "0023_rename_alliasnumber_cooperates_alliasnumber_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cooperates", name="requestverificationcode",
        ),
    ]
