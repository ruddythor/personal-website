# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arenafighter', '0002_auto_20161228_0250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area_difficulty_level', models.IntegerField(default=1)),
                ('name', models.TextField(default=b'Random Location')),
            ],
        ),
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
        migrations.AddField(
            model_name='character',
            name='location',
            field=models.ForeignKey(related_name='characters', default=None, blank=True, to='arenafighter.Location', null=True),
        ),
    ]
