# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocklist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.IntegerField(unique=True)),
                ('tickr', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('date', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='stock',
            name='id',
        ),
        migrations.AddField(
            model_name='stock',
            name='eps',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='pe',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='volume',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stock',
            name='tickr',
            field=models.CharField(max_length=200, serialize=False, primary_key=True),
        ),
    ]
