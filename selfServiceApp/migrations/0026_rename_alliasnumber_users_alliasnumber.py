# Generated by Django 4.1.5 on 2023-04-13 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selfServiceApp', '0025_remove_cooperates_gsmnumber_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='alliasNumber',
            new_name='alliasnumber',
        ),
    ]
