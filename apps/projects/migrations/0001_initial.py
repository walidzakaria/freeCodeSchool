# Generated by Django 3.0.7 on 2020-06-28 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='')),
                ('url', models.CharField(max_length=255)),
                ('level', models.IntegerField(choices=[(1, 'Level 1'), (2, 'Level 2')], default=1)),
                ('is_required', models.IntegerField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]