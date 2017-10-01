# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def create_initial_locations(apps, schema_editor):
	Location = apps.get_model('arenafighter', 'Location')
	Store = apps.get_model('arenafighter', 'Store')

	new_loc_1 = Location(area_difficulty_level=1, name='A random location')
	new_loc_1.save()

	store_1 = Store(location=new_loc_1)
	store_1.save()

	new_loc_2 = Location(area_difficulty_level=2, name='A slightly harder location')
	new_loc_2.save()

	store_2 = Store(location=new_loc_2)
	store_2.save()



def delete_locations(apps, schema_editor):
	Location = apps.get_model('arenafighter', 'Location')
	Location.objects.all().delete()

	Store = apps.get_model('arenafighter', 'Store')
	Store.objects.all().delete()




class Migration(migrations.Migration):

    dependencies = [
        ('arenafighter', '0006_auto_20171001_0532'),
    ]

    operations = [
	    migrations.RunPython(create_initial_locations, delete_locations),
    ]
