# Generated by Django 4.1.5 on 2023-02-24 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("selfServiceApp", "0016_remove_users_attempts_remove_users_cdmanumber"),
    ]

    operations = [
        migrations.RenameField(
            model_name="users", old_name="gsmNumber", new_name="gsmnumber",
        ),
    ]
