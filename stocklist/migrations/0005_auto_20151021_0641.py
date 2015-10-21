# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocklist', '0004_auto_20151021_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pick',
            name='tickr',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
