# Generated by Django 4.2.4 on 2023-09-01 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_delete_comments_user_delete_contacts_delete_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hotel.rooms'),
            preserve_default=False,
        ),
    ]