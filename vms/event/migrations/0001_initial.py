# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.11.17 on 2020-05-23 13:04
=======
# Generated by Django 1.11 on 2020-01-29 16:27
>>>>>>> 12ab2afe0cb239a0b8f25d2d4c8f49784ec7dc6b
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities_light', '0008_city_timezone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
<<<<<<< HEAD
                ('name', models.CharField(max_length=75, validators=[django.core.validators.RegexValidator("^[(A-Z)|(a-z)|(0-9)|(\\s)|(\\.)|(,)|(\\-)|(!)|(\\')]+$")])),
                ('description', models.TextField(blank=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('address', models.CharField(blank=True, max_length=75, null=True, validators=[django.core.validators.RegexValidator("^[(A-Z)|(a-z)|(0-9)|(\\s)|(\\-)|(\\')|(,)]+$")])),
                ('venue', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.RegexValidator("^[(A-Z)|(a-z)|(\\s)|(\\-)|(\\')]+$")])),
=======
                ('name', models.CharField(max_length=75, validators=[django.core.validators.RegexValidator(b"^[(A-Z)|(a-z)|(0-9)|(\\s)|(\\.)|(,)|(\\-)|(!)|(\\')]+$")])),
                ('description', models.TextField(blank=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('address', models.CharField(blank=True, max_length=75, null=True, validators=[django.core.validators.RegexValidator(b"^[(A-Z)|(a-z)|(0-9)|(\\s)|(\\-)|(\\')|(,)]+$")])),
                ('venue', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.RegexValidator(b"^[(A-Z)|(a-z)|(\\s)|(\\-)|(\\')]+$")])),
>>>>>>> 12ab2afe0cb239a0b8f25d2d4c8f49784ec7dc6b
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_light.City')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_light.Country')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_light.Region')),
            ],
        ),
    ]
