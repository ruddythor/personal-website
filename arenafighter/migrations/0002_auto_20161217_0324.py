# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arenafighter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='hpmax',
            field=models.IntegerField(default=46),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='gold',
            field=models.IntegerField(default=16),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='hpmax',
            field=models.IntegerField(default=54),
        ),
    ]
