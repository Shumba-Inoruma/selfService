# Generated by Django 4.1.5 on 2023-02-08 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("selfServiceApp", "0003_code"),
    ]

    operations = [
        migrations.RemoveField(model_name="users", name="token",),
        migrations.AddField(
            model_name="users",
            name="verificationCode",
            field=models.CharField(max_length=4, null=True),
        ),
    ]
