# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocklist', '0002_auto_20151020_2026'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Picks',
            new_name='Pick',
        ),
    ]
