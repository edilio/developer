__author__ = 'edilio'

from django.core.management import setup_environ
from django.core.management import execute_manager

import imp
try:
    imp.find_module('settings') # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
    sys.exit(1)

import settings
setup_environ(settings)
from ideas.models import *
import timeit

idea = Idea.objects.all()[2]
print idea.expection_in_years(10)

