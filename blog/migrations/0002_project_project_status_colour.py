# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_status_colour',
            field=models.CharField(default='#628d78', max_length=7),
            preserve_default=False,
        ),
    ]
