# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arenafighter', '0002_auto_20161228_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='hpmax',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='gold',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='hpmax',
            field=models.IntegerField(),
        ),
    ]
