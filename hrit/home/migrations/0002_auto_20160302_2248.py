# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-02 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='text',
            field=models.TextField(),
        ),
    ]