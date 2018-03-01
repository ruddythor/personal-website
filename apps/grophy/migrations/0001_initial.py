# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('portfolio_item_type', models.CharField(max_length=100, choices=[(b'image', b'Image'), (b'illustration', b'Illustration'), (b'logodesign', b'Logo Design'), (b'characterdesign', b'Character Design'), (b'userexperience', b'User Experience'), (b'painting', b'Painting'), (b'drawing', b'Drawing'), (b'twod', b'Two D'), (b'threed', b'Three D'), (b'shortfilm', b'Short Film'), (b'photography', b'Photography'), (b'videocompositing', b'Video Compositing')])),
                ('portfolio_item', models.FileField(upload_to=b'')),
            ],
        ),
    ]
