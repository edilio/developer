# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ideas', '0005_idea_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='created_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='idea',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
