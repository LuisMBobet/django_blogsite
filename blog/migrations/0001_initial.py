# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 11:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('image_name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_title', models.CharField(max_length=255, unique=True)),
                ('post_content', models.TextField()),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('post_slug', models.SlugField(unique=True)),
                ('post_images', models.ManyToManyField(blank=True, related_name='images', to='blog.Image')),
            ],
            options={
                'ordering': ['-post_date'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=255, unique=True)),
                ('project_slug', models.SlugField(unique=True)),
                ('project_date', models.DateTimeField(auto_now_add=True)),
                ('project_status', models.CharField(choices=[('Complete', 'Complete'), ('In Progress', 'In progress'), ('Not Started', 'Not started')], max_length=11)),
                ('project_colour', models.CharField(max_length=7)),
                ('project_summary', models.TextField()),
            ],
            options={
                'ordering': ['-project_date'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.AutoField(primary_key=True, serialize=False)),
                ('tag_name', models.CharField(max_length=255)),
                ('tag_type', models.CharField(choices=[('PL', 'Programming Language'), ('OT', 'Other Technology'), ('TP', 'Time Period'), ('MT', 'Misc Tag')], max_length=2)),
                ('tag_colour', models.CharField(blank=True, max_length=7, null=True)),
            ],
            options={
                'ordering': ['tag_type'],
            },
        ),
        migrations.AddField(
            model_name='project',
            name='project_tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='blog.Tag'),
        ),
        migrations.AddField(
            model_name='post',
            name='post_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projectPost', to='blog.Project'),
        ),
    ]
