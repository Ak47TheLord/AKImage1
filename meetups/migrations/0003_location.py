# Generated by Django 3.2.5 on 2021-08-02 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0002_meetups_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=300)),
            ],
        ),
    ]
