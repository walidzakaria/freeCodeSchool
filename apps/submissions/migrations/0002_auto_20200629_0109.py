# Generated by Django 3.0.7 on 2020-06-28 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentsubmission',
            old_name='project_id',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='studentsubmission',
            old_name='student_id',
            new_name='student',
        ),
    ]
