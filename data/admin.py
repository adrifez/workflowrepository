# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from data.models import Category, WorkFlow

# Classes
 
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug')
	prepopulated_fields = {'slug':('name',)}

class WorkFlowAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'views', 'downloads', 'client_ip', 'created')
	prepopulated_fields = {'slug':('name',)}

# Register your models here.

admin.site.register(Category, CategoryAdmin)
admin.site.register(WorkFlow, WorkFlowAdmin)
