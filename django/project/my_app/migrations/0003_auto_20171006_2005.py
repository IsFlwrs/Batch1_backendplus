# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-06 20:05
from __future__ import unicode_literals

from django.db import migrations, models
import my_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('My application', '0002_person_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(default=0, help_text='solo numeros', validators=[my_app.validators.age_validation]),
        ),
    ]
