# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='idea',
            old_name='likes',
            new_name='votes',
        ),
    ]
