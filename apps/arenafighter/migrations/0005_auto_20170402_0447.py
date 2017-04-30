# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arenafighter', '0004_character_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arena',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.OneToOneField(related_name='arena', null=True, default=None, blank=True, to='arenafighter.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.ForeignKey(related_name='stores', default=None, blank=True, to='arenafighter.Location', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='armor',
            name='shop',
            field=models.ForeignKey(related_name='armors', default=None, blank=True, to='arenafighter.Store', null=True),
        ),
        migrations.AddField(
            model_name='potion',
            name='shop',
            field=models.ForeignKey(related_name='potions', default=None, blank=True, to='arenafighter.Store', null=True),
        ),
        migrations.AddField(
            model_name='weapon',
            name='shop',
            field=models.ForeignKey(related_name='weapons', default=None, blank=True, to='arenafighter.Store', null=True),
        ),
    ]
