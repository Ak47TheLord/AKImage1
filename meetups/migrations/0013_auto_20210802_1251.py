# Generated by Django 3.2.5 on 2021-08-02 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0012_auto_20210802_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetups',
            name='date',
        ),
        migrations.RemoveField(
            model_name='meetups',
            name='organizer_email',
        ),
    ]
