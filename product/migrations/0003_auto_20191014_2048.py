# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-14 20:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20191014_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='authors',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Author'),
        ),
    ]