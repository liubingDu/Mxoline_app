# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-24 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20170724_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='desc',
            field=models.TextField(max_length=500, verbose_name='\u673a\u6784\u63cf\u8ff0'),
        ),
    ]
