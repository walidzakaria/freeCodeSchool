# Generated by Django 3.0.7 on 2020-06-27 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waitlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='waitlistentry',
            options={'verbose_name_plural': 'waitlist entries'},
        ),
    ]