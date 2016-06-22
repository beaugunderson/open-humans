# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-22 13:43
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('private_sharing', '0028_projectdatafile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datarequestproject',
            name='request_sources_access',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=list, help_text='List of sources this project is requesting access to on Open Humans.', size=None, verbose_name="Data sources you're requesting access to"),
        ),
    ]
