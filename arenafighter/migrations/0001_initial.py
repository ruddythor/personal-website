# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Armor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('buy_value', models.IntegerField(default=0)),
                ('sell_value', models.IntegerField(default=0)),
                ('slots_required', models.IntegerField(default=1)),
                ('equipped', models.BooleanField(default=False)),
                ('defense_value', models.IntegerField(default=2)),
                ('type', models.TextField(default=b'armor', editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField(default=1)),
                ('name', models.TextField(default=b'The Stranger')),
                ('hpmax', models.IntegerField(default=63)),
                ('current_hp', models.IntegerField()),
                ('base_attack', models.IntegerField(default=3)),
                ('base_defense', models.IntegerField(default=3)),
                ('gold', models.IntegerField(default=50)),
                ('xp', models.IntegerField(default=0)),
                ('renown', models.IntegerField(default=0)),
                ('next_levelup', models.IntegerField(default=100)),
                ('num_armor', models.IntegerField(default=0)),
                ('fights_won', models.IntegerField(default=0)),
                ('fights_lost', models.IntegerField(default=0)),
                ('dead', models.BooleanField(default=False)),
                ('times_died', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Enemy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(default=b'An Enemy!')),
                ('xp_value', models.IntegerField(default=5)),
                ('renown_value', models.IntegerField(default=10)),
                ('hpmax', models.IntegerField(default=53)),
                ('current_hp', models.IntegerField(default=0)),
                ('base_attack', models.IntegerField(default=4)),
                ('base_defense', models.IntegerField(default=5)),
                ('gold', models.IntegerField(default=19)),
                ('dead', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slots', models.IntegerField(default=10)),
                ('slots_filled', models.IntegerField(default=0)),
                ('slots_empty', models.IntegerField(default=10)),
                ('character', models.OneToOneField(related_name=b'inventory', default=None, to='arenafighter.Character')),
            ],
            options={
                'verbose_name_plural': 'inventories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Potion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('buy_value', models.IntegerField(default=0)),
                ('sell_value', models.IntegerField(default=0)),
                ('slots_required', models.IntegerField(default=1)),
                ('equipped', models.BooleanField(default=False)),
                ('heal_percent', models.IntegerField(default=20)),
                ('type', models.TextField(default=b'potion', editable=False)),
                ('inventory', models.ForeignKey(related_name=b'potion', default=None, blank=True, to='arenafighter.Inventory', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('current_character', models.ForeignKey(related_name=b'profile', to='arenafighter.Character', null=True)),
                ('user', models.OneToOneField(related_name=b'profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('buy_value', models.IntegerField(default=0)),
                ('sell_value', models.IntegerField(default=0)),
                ('slots_required', models.IntegerField(default=1)),
                ('equipped', models.BooleanField(default=False)),
                ('attack_value', models.IntegerField(default=2)),
                ('type', models.TextField(default=b'weapon', editable=False)),
                ('inventory', models.ForeignKey(related_name=b'weapon', default=None, blank=True, to='arenafighter.Inventory', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='character',
            name='created_by',
            field=models.ForeignKey(related_name=b'created_characters', to='arenafighter.Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='equipped_armor',
            field=models.ForeignKey(related_name=b'equipped_on', default=None, blank=True, to='arenafighter.Armor', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='armor',
            name='inventory',
            field=models.ForeignKey(related_name=b'armor', default=None, blank=True, to='arenafighter.Inventory', null=True),
            preserve_default=True,
        ),
    ]
