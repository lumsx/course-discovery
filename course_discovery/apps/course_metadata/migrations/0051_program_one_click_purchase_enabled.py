# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-05 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0050_person_profile_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='one_click_purchase_enabled',
            field=models.BooleanField(default=False, help_text='Allow courses in this program to be purchased in a single transaction'),
        ),
    ]
