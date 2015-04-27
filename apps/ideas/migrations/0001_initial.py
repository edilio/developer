# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('long_description', models.TextField(blank=True)),
                ('market_population', models.PositiveIntegerField(default=0, help_text=b'Total Market population')),
                ('market_percentage', models.PositiveSmallIntegerField(default=2, help_text=b'% of Market population that we expect to cover', verbose_name=b'Market %')),
                ('monthly_sales', models.PositiveIntegerField(default=0, help_text=b'Number(avg) of sales we expect to do monthly')),
                ('initial_cost', models.PositiveIntegerField(default=0, help_text=b'How much is going to cost us to create this piece of software')),
                ('monthly_cost', models.PositiveIntegerField(default=0, help_text=b'Monthly cost for having the service up and running')),
                ('sale_price', models.PositiveIntegerField(default=0, help_text=b'Price of one copy of the app')),
                ('subscription_fee', models.PositiveIntegerField(default=0, help_text=b'monthly price for using this product or service')),
                ('years', models.PositiveSmallIntegerField(default=1, help_text=b'Number of years we want to use for guessing how much profits we will get')),
                ('expectation_x_years', models.PositiveIntegerField(default=0, help_text=b'How much do we expect to earn in x years')),
            ],
            options={
                'ordering': ('-expectation_x_years',),
            },
        ),
    ]
