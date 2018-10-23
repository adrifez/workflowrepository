# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
	name = models.CharField(_("Name"), max_length=128, unique=True, blank=false)
	slug = models.SlugField(_("Slug"), unique=True)
	created = models.DateField(_("Date"), default=datetime.date.today)
	tooltip = models.CharField(_("Tooltip"), max_length=128)


	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'Categories'
	
	def __str__(self): # For Python 2, use __unicode__ too
		return self.name

class Workflow(models.Model):
	name = models.CharField(max_length=128, unique=True, blank=false)
	slug = models.SlugField(unique=True)
	description = models.CharField(max_length=512, default="")


	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'Workflows'
	
	def __str__(self): # For Python 2, use __unicode__ too
		return self.name
