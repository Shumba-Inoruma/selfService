# Generated by Django 4.1.5 on 2023-02-16 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("selfServiceApp", "0008_remove_users_verificationcode"),
    ]

    operations = [
        migrations.AddField(
            model_name="users",
            name="allocatedNumber",
            field=models.IntegerField(default=0),
        ),
    ]