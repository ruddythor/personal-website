# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Inventory'
        db.create_table(u'arenafighter_inventory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slots', self.gf('django.db.models.fields.IntegerField')(default=10)),
            ('slots_filled', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('slots_empty', self.gf('django.db.models.fields.IntegerField')(default=10)),
            ('owner', self.gf('django.db.models.fields.related.OneToOneField')(default=None, related_name='inventory', unique=True, to=orm['arenafighter.Player'])),
        ))
        db.send_create_signal('arenafighter', ['Inventory'])

        # Adding model 'InventoryItem'
        db.create_table(u'arenafighter_inventoryitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('buy_value', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sell_value', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('slots_required', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('inventory', self.gf('django.db.models.fields.related.OneToOneField')(default=None, related_name='items', unique=True, to=orm['arenafighter.Inventory'])),
        ))
        db.send_create_signal('arenafighter', ['InventoryItem'])

        # Adding model 'Armor'
        db.create_table(u'arenafighter_armor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('buy_value', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sell_value', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('defense_value', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('is_armor', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('equipped', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('slots_required', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('inventory', self.gf('django.db.models.fields.related.OneToOneField')(default=None, related_name='armor', unique=True, to=orm['arenafighter.Inventory'])),
        ))
        db.send_create_signal('arenafighter', ['Armor'])

        # Adding model 'Weapon'
        db.create_table(u'arenafighter_weapon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('buy_value', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sell_value', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('attack_value', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('equipped', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('slots_required', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('inventory', self.gf('django.db.models.fields.related.OneToOneField')(default=None, related_name='weapons', unique=True, to=orm['arenafighter.Inventory'])),
        ))
        db.send_create_signal('arenafighter', ['Weapon'])

        # Adding model 'Player'
        db.create_table(u'arenafighter_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('level', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('name', self.gf('django.db.models.fields.TextField')(default='Unknown')),
            ('hpmax', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('current_hp', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('base_attack', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('base_defense', self.gf('django.db.models.fields.IntegerField')(default=3)),
            ('gold', self.gf('django.db.models.fields.IntegerField')(default=50)),
            ('xp', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('renown', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('next_levelup', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('num_armor', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('arenafighter', ['Player'])


    def backwards(self, orm):
        # Deleting model 'Inventory'
        db.delete_table(u'arenafighter_inventory')

        # Deleting model 'InventoryItem'
        db.delete_table(u'arenafighter_inventoryitem')

        # Deleting model 'Armor'
        db.delete_table(u'arenafighter_armor')

        # Deleting model 'Weapon'
        db.delete_table(u'arenafighter_weapon')

        # Deleting model 'Player'
        db.delete_table(u'arenafighter_player')


    models = {
        'arenafighter.armor': {
            'Meta': {'object_name': 'Armor'},
            'buy_value': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'defense_value': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'equipped': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.related.OneToOneField', [], {'default': 'None', 'related_name': "'armor'", 'unique': 'True', 'to': "orm['arenafighter.Inventory']"}),
            'is_armor': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'sell_value': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slots_required': ('django.db.models.fields.IntegerField', [], {'default': '2'})
        },
        'arenafighter.inventory': {
            'Meta': {'object_name': 'Inventory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.OneToOneField', [], {'default': 'None', 'related_name': "'inventory'", 'unique': 'True', 'to': "orm['arenafighter.Player']"}),
            'slots': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'slots_empty': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'slots_filled': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'arenafighter.inventoryitem': {
            'Meta': {'object_name': 'InventoryItem'},
            'buy_value': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.related.OneToOneField', [], {'default': 'None', 'related_name': "'items'", 'unique': 'True', 'to': "orm['arenafighter.Inventory']"}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'sell_value': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slots_required': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'arenafighter.player': {
            'Meta': {'object_name': 'Player'},
            'base_attack': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'base_defense': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'current_hp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gold': ('django.db.models.fields.IntegerField', [], {'default': '50'}),
            'hpmax': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'name': ('django.db.models.fields.TextField', [], {'default': "'Unknown'"}),
            'next_levelup': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'num_armor': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'renown': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'xp': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'arenafighter.weapon': {
            'Meta': {'object_name': 'Weapon'},
            'attack_value': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'buy_value': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'equipped': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.related.OneToOneField', [], {'default': 'None', 'related_name': "'weapons'", 'unique': 'True', 'to': "orm['arenafighter.Inventory']"}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'sell_value': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slots_required': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['arenafighter']