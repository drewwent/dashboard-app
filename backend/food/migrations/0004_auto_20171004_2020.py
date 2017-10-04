# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_auto_20171004_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='name',
            field=models.CharField(db_index=True, default='', max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(db_index=True, default='', max_length=256),
        ),
    ]
