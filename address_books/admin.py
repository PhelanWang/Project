# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from address_books.models import Category, Entry

admin.site.register(Category, admin_class=None)
admin.site.register(Entry, admin_class=None)
