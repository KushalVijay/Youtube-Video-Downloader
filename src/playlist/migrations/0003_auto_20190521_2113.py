# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-05-21 15:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0002_videolink_qualtiy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videolink',
            old_name='qualtiy',
            new_name='quality',
        ),
    ]
