# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-15 15:28
from __future__ import unicode_literals

import stdimage.models
import stdimage.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ietf_language_tags', '0001_squashed_0005_fix_language_tag_names_again'),
        ('course_metadata', '0056_auto_20170620_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=stdimage.models.StdImageField(blank=True, help_text='Please provide a course preview image', null=True, upload_to=stdimage.utils.UploadToAutoSlug('uuid', path='media/course/image')),
        ),
        migrations.AddField(
            model_name='course',
            name='outcome',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='courserun',
            name='learner_testimonials',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='courserun',
            name='video_translation_languages',
            field=models.ManyToManyField(blank=True, related_name='_courserun_video_translation_languages_+', to='ietf_language_tags.LanguageTag'),
        ),
    ]
