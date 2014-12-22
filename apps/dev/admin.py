__author__ = 'edilio'

from django.contrib import admin

from apps.dev.models import *


class TechnologyAdmin(admin.ModelAdmin):
    list_per_page = 25


class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'PH', 'S8', 'PBS8', 'submodules')
    list_per_page = 25


class SubModuleAdmin(admin.ModelAdmin):
    list_display = ('dev_module', 'name', 'PH', 'S8', 'PBS8', 'technology',)
    list_per_page = 18
    ordering = ('dev_module__name', 'name')
    list_filter = ('technology', 'PH', 'S8', 'PBS8')


def register(model,admin_class):
    admin.site.register(model, admin_class)

register(Technology, TechnologyAdmin)
register(DevModule, ModuleAdmin)
register(SubModule, SubModuleAdmin)