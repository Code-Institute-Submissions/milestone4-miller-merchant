# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-26 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20191015_0545'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='author_bio',
            field=models.CharField(default='author-bio', max_length=1000),
        ),
        migrations.AddField(
            model_name='author',
            name='author_image',
            field=models.ImageField(default='', upload_to='images'),
        ),
        migrations.AddField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(default='1990-08-08'),
        ),
        migrations.AddField(
            model_name='author',
            name='nationality',
            field=models.CharField(default='nationality', max_length=100),
        ),
    ]
