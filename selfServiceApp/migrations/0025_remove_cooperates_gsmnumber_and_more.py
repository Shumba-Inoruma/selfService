# Generated by Django 4.1.5 on 2023-02-27 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("selfServiceApp", "0024_remove_cooperates_requestverificationcode"),
    ]

    operations = [
        migrations.RemoveField(model_name="cooperates", name="gsmNumber",),
        migrations.AlterField(
            model_name="cooperates",
            name="password",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="cooperates",
            name="registered",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name="cooperates",
            name="gsmnumber",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
