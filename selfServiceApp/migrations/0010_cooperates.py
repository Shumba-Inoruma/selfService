# Generated by Django 4.1.5 on 2023-02-16 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("selfServiceApp", "0009_users_allocatednumber"),
    ]

    operations = [
        migrations.CreateModel(
            name="cooperates",
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
                ("companyName", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("number", models.CharField(max_length=100)),
                ("password", models.CharField(max_length=50)),
                ("registered", models.BooleanField(blank=True, null=True)),
                ("requestVerificationCode", models.IntegerField(default=1)),
                ("attempts", models.IntegerField(default=1)),
                ("allocatedNumber", models.IntegerField(default=0)),
                ("cr6", models.FileField(upload_to="")),
                ("cr14", models.FileField(upload_to="")),
                ("proofOfResidence", models.FileField(upload_to="")),
            ],
        ),
    ]
