# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from data.models import Category, Workflow

# Classes
 
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug')
	prepopulated_fields = {'slug':('name',)}

class WorkflowAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'views', 'downloads', 'client_ip', 'created')
	prepopulated_fields = {'slug':('name',)}

# Register your models here.

admin.site.register(Category, CategoryAdmin)
admin.site.register(Workflow, WorkflowAdmin)
