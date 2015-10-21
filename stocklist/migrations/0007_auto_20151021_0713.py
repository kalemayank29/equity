# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocklist', '0006_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pick',
            name='tickr',
            field=models.CharField(max_length=200),
        ),
    ]
