# Generated by Django 3.2.5 on 2021-08-02 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0013_auto_20210802_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetups',
            name='date',
            field=models.DateField(default='2021-08-2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meetups',
            name='organizer_email',
            field=models.EmailField(default='test@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]
