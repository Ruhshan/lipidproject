# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 17:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0022_qc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qcdata',
            name='added_by',
        ),
        migrations.RemoveField(
            model_name='qcdata',
            name='lab',
        ),
        migrations.DeleteModel(
            name='QCData',
        ),
    ]
