# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-29 09:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pyfreebill', '0003_auto_20161025_1701'),
    ]

    database_operations = [
        migrations.AlterModelTable(
            name='CustomerDirectory',
            table='customer_directory',
        ),
    ]

    state_operations = [

    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=database_operations,
            state_operations=state_operations)
    ]
