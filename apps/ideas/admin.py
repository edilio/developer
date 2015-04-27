__author__ = 'edilio'

from django.contrib import admin

from apps.ideas.models import *


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'status', 'market_population', 'market_percentage', 'max_number_of_sales',
                    'monthly_sales',
                    'initial_cost', 'monthly_cost', 'sale_price', 'subscription_fee',
                    'expectation', 'years', 'expectation_x_years')

    list_filter = ('category', 'status')

    search_fields = ('name', 'long_description')

    fieldsets = (
        (None, {
            'fields': (
                ('name', 'long_description',),
            )
        }),
        (None, {
            'fields': (
                ('category', 'status',),
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

                ('monthly_sales', 'sale_price', 'subscription_fee'),

            )
        }),
        ('Profits', {
            'fields': (

                ('years', ),

            )
        }),
        )

    list_per_page = 25


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


def register(model,admin_class):
    admin.site.register(model, admin_class)