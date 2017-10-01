# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arenafighter', '0005_auto_20170402_0447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='armor',
            name='type',
        ),
        migrations.RemoveField(
            model_name='potion',
            name='type',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='type',
        ),
        migrations.AlterField(
            model_name='armor',
            name='shop',
            field=models.ForeignKey(related_name='armor_items', default=None, blank=True, to='arenafighter.Store', null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='next_levelup',
            field=models.IntegerField(default=25),
        ),
        migrations.AlterField(
            model_name='potion',
            name='shop',
            field=models.ForeignKey(related_name='potion_items', default=None, blank=True, to='arenafighter.Store', null=True),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='shop',
            field=models.ForeignKey(related_name='weapon_items', default=None, blank=True, to='arenafighter.Store', null=True),
        ),
    ]
