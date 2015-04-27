# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0004_idea_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='status',
            field=models.PositiveSmallIntegerField(default=1, choices=[(1, b'Idea'), (2, b'Devel'), (3, b'QA'), (4, b'Prod'), (5, b'Rejected')]),
        ),
    ]
