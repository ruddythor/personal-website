# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arenafighter', '0003_auto_20170213_0359'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='gender',
            field=models.TextField(default=b'male'),
        ),
    ]
