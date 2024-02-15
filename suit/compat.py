"""
This file exists to contain all Django and Python compatibility issues.
In order to avoid circular references, nothing should be imported from suit lib.

Based on:
https://github.com/django-debug-toolbar/django-debug-toolbar/blob/master/debug_toolbar/compat.py

"""
import django
from django.contrib.contenttypes import admin as ct_admin
from django.template.defaulttags import url

tpl_context_class = dict
