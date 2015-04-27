# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    def insert_category(apps, schema_editor):
        # We can't import the Person model directly as it may be a newer
        # version than this migration expects. We use the historical version.
        Category = apps.get_model("ideas", "Category")
        Category.objects.create(name='General')

    dependencies = [
        ('ideas', '0002_category'),
    ]

    operations = [
        migrations.RunPython(insert_category),
    ]
