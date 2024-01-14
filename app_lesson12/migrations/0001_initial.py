# Generated by Django 5.0.1 on 2024-01-14 12:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('dicription', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('movie_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_lesson12.movietype')),
            ],
        ),
    ]