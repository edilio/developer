__author__ = 'edilio'

from models import *
from django.contrib import admin

class IdeaAdmin(admin.ModelAdmin):
    list_display = ('name','market_population','market_percentage','max_number_of_sales',
                    'monthly_sales',
                    'initial_cost','monthly_cost','sale_price','subscription_fee',
                    'expectation','years','expectation_x_years')


    fieldsets = (
        (None, {
            'fields': (
                        ('name','long_description',),
            )
        }),
        ('Market', {
            'fields': (

                        ('market_population', 'market_percentage'),

            )
        }),
        ('Cost', {
            'fields': (

                        ('initial_cost', 'monthly_cost'),

            )
        }),
        ('Sales', {
            'fields': (

                        ('monthly_sales', 'sale_price','subscription_fee'),

            )
        }),
        ('Profits', {
            'fields': (

                        ('years', ) # 'expectation_x_years'),

            )
        }),
        )


    list_per_page = 25

def register(model,admin_class):
    admin.site.register(model, admin_class)

register(Idea, IdeaAdmin)
