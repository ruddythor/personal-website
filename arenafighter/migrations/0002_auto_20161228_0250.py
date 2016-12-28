# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arenafighter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='area_difficulty_level',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='location',
            name='name',
            field=models.TextField(default=b'Random Location'),
        ),
        migrations.AlterField(
            model_name='character',
            name='hpmax',
            field=models.IntegerField(default=59),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='gold',
            field=models.IntegerField(default=18),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='hpmax',
            field=models.IntegerField(default=52),
        ),
    ]
