# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-25 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_auto_20170724_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermessage',
            name='user',
            field=models.IntegerField(default=0, verbose_name='\u63a5\u6536\u7528\u6237ID'),
        ),
    ]