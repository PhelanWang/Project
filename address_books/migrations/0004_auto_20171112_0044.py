# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 00:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address_books', '0003_auto_20171111_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='name',
            field=models.CharField(max_length=10),
        ),
    ]