# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocklist', '0003_auto_20151020_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pick',
            name='uid',
            field=models.IntegerField(),
        ),
    ]
