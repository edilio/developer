# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ideas', '0006_auto_20150427_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='modified_by',
            field=models.ForeignKey(related_name='users', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='idea',
            name='modified_on',
            field=models.DateTimeField(null=True),
        ),
    ]
