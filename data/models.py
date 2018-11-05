# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify

import datetime

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True, blank=False)
	slug = models.SlugField(unique=True)
	created = models.DateField(default=datetime.date.today)
	tooltip = models.CharField(max_length=128)


	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'Categories'
	
	def __str__(self): # For Python 2, use __unicode__ too
		return self.name

class WorkFlow(models.Model):
	name = models.CharField(max_length=128, unique=True, blank=False)
	slug = models.SlugField(unique=True)
	description = models.CharField(max_length=512, default="")
	views = models.IntegerField(default=0)
	downloads = models.IntegerField(default=0)
	versionInit = models.CharField(max_length=128)
	category = models.ManyToManyField(Category, blank=False)
	client_ip = models.GenericIPAddressField()
	keywords = models.CharField(max_length=256, default="")
	json = models.TextField(default="")
	created =  models.DateField(default=datetime.date.today)


	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(WorkFlow, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'Workflows'
	
	def __str__(self): # For Python 2, use __unicode__ too
		return self.name
