# Generated by Django 4.2.4 on 2023-09-01 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_reservation_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='name',
            new_name='room',
        ),
    ]
