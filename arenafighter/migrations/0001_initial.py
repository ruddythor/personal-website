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
            ('character', self.gf('django.db.models.fields.related.OneToOneField')(related_name='inventory', null=True, default=None, to=orm['arenafighter.Character'], blank=True, unique=True)),
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
            ('equipped_on', self.gf('django.db.models.fields.related.OneToOneField')(related_name='equipped_items', null=True, default=None, to=orm['arenafighter.Character'], blank=True, unique=True)),
            ('inventory', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='items', null=True, blank=True, to=orm['arenafighter.Inventory'])),
            ('type', self.gf('django.db.models.fields.TextField')(default='InventoryItem')),
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
            ('slots_required', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('inventory', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='armor', null=True, blank=True, to=orm['arenafighter.Inventory'])),
            ('type', self.gf('django.db.models.fields.TextField')(default='Armor')),
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
            ('slots_required', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('inventory', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='weapons', null=True, blank=True, to=orm['arenafighter.Inventory'])),
            ('type', self.gf('django.db.models.fields.TextField')(default='Weapon')),
        ))
        db.send_create_signal('arenafighter', ['Weapon'])

        # Adding M2M table for field equipped_on on 'Weapon'
        m2m_table_name = db.shorten_name(u'arenafighter_weapon_equipped_on')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('weapon', models.ForeignKey(orm['arenafighter.weapon'], null=False)),
            ('character', models.ForeignKey(orm['arenafighter.character'], null=False))
        ))
        db.create_unique(m2m_table_name, ['weapon_id', 'character_id'])

        # Adding model 'Profile'
        db.create_table(u'arenafighter_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='profile', unique=True, to=orm['auth.User'])),
            ('current_character', self.gf('django.db.models.fields.related.ForeignKey')(related_name='current_character', null=True, to=orm['arenafighter.Character'])),
        ))
        db.send_create_signal('arenafighter', ['Profile'])

        # Adding model 'Character'
        db.create_table(u'arenafighter_character', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('level', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('name', self.gf('django.db.models.fields.TextField')(default='The Stranger')),
            ('hpmax', self.gf('django.db.models.fields.IntegerField')(default=46)),
            ('equipped_armor', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='equipped_on', null=True, blank=True, to=orm['arenafighter.Armor'])),
            ('current_hp', self.gf('django.db.models.fields.IntegerField')()),
            ('base_attack', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('base_defense', self.gf('django.db.models.fields.IntegerField')(default=3)),
            ('gold', self.gf('django.db.models.fields.IntegerField')(default=50)),
            ('xp', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('renown', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('next_levelup', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('num_armor', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('fights_won', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('fights_lost', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('arenafighter', ['Character'])

        # Adding model 'Enemy'
        db.create_table(u'arenafighter_enemy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')(default='An Enemy!')),
            ('xp_value', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('renown_value', self.gf('django.db.models.fields.IntegerField')(default=10)),
            ('hpmax', self.gf('django.db.models.fields.IntegerField')(default=46)),
            ('current_hp', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('base_attack', self.gf('django.db.models.fields.IntegerField')(default=4)),
            ('base_defense', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('gold', self.gf('django.db.models.fields.IntegerField')(default=18)),
        ))
        db.send_create_signal('arenafighter', ['Enemy'])


    def backwards(self, orm):
        # Deleting model 'Inventory'
        db.delete_table(u'arenafighter_inventory')

        # Deleting model 'InventoryItem'
        db.delete_table(u'arenafighter_inventoryitem')

        # Deleting model 'Armor'
        db.delete_table(u'arenafighter_armor')

        # Deleting model 'Weapon'
        db.delete_table(u'arenafighter_weapon')

        # Removing M2M table for field equipped_on on 'Weapon'
        db.delete_table(db.shorten_name(u'arenafighter_weapon_equipped_on'))

        # Deleting model 'Profile'
        db.delete_table(u'arenafighter_profile')

        # Deleting model 'Character'
        db.delete_table(u'arenafighter_character')

        # Deleting model 'Enemy'
        db.delete_table(u'arenafighter_enemy')


    models = {
        'arenafighter.armor': {
            'Meta': {'object_name': 'Armor'},
            'buy_value': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'defense_value': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'armor'", 'null': 'True', 'blank': 'True', 'to': "orm['arenafighter.Inventory']"}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'sell_value': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slots_required': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'type': ('django.db.models.fields.TextField', [], {'default': "'Armor'"})
        },
        'arenafighter.character': {
            'Meta': {'object_name': 'Character'},
            'base_attack': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'base_defense': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'current_hp': ('django.db.models.fields.IntegerField', [], {}),
            'equipped_armor': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'equipped_on'", 'null': 'True', 'blank': 'True', 'to': "orm['arenafighter.Armor']"}),
            'fights_lost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fights_won': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gold': ('django.db.models.fields.IntegerField', [], {'default': '50'}),
            'hpmax': ('django.db.models.fields.IntegerField', [], {'default': '46'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'name': ('django.db.models.fields.TextField', [], {'default': "'The Stranger'"}),
            'next_levelup': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'num_armor': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'renown': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'xp': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'arenafighter.enemy': {
            'Meta': {'object_name': 'Enemy'},
            'base_attack': ('django.db.models.fields.IntegerField', [], {'default': '4'}),
            'base_defense': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'current_hp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gold': ('django.db.models.fields.IntegerField', [], {'default': '18'}),
            'hpmax': ('django.db.models.fields.IntegerField', [], {'default': '46'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'default': "'An Enemy!'"}),
            'renown_value': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'xp_value': ('django.db.models.fields.IntegerField', [], {'default': '5'})
        },
        'arenafighter.inventory': {
            'Meta': {'object_name': 'Inventory'},
            'character': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'inventory'", 'null': 'True', 'default': 'None', 'to': "orm['arenafighter.Character']", 'blank': 'True', 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slots': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'slots_empty': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'slots_filled': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'arenafighter.inventoryitem': {
            'Meta': {'object_name': 'InventoryItem'},
            'buy_value': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'equipped_on': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'equipped_items'", 'null': 'True', 'default': 'None', 'to': "orm['arenafighter.Character']", 'blank': 'True', 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'items'", 'null': 'True', 'blank': 'True', 'to': "orm['arenafighter.Inventory']"}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'sell_value': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slots_required': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'type': ('django.db.models.fields.TextField', [], {'default': "'InventoryItem'"})
        },
        'arenafighter.profile': {
            'Meta': {'object_name': 'Profile'},
            'current_character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'current_character'", 'null': 'True', 'to': "orm['arenafighter.Character']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profile'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        'arenafighter.weapon': {
            'Meta': {'object_name': 'Weapon'},
            'attack_value': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'buy_value': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'equipped_on': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'equipped_weapon'", 'default': 'None', 'to': "orm['arenafighter.Character']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'weapons'", 'null': 'True', 'blank': 'True', 'to': "orm['arenafighter.Inventory']"}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'sell_value': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slots_required': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'type': ('django.db.models.fields.TextField', [], {'default': "'Weapon'"})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['arenafighter']