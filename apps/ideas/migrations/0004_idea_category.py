# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.ideas.models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0003_insert_default_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='category',
            field=models.ForeignKey(default=apps.ideas.models.get_first_category, to='ideas.Category'),
        ),
    ]
