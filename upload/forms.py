from django import forms
from django.db import models
from data.models import Category, WorkFlow

class WorkFlowForm(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text="Please enter the name of the workflow.")
	category = models.ManyToManyField(Category, blank=False)
	keywords = forms.CharField(max_length=256, help_text="Please enter the keywords for workflow")
	description = forms.CharField(max_length=512, help_text="Please write a description for the workflow")
	versionInit = forms.CharField(max_length=128, help_text="Enter the versionInit")
	json = forms.FileField()
	class Meta:
		# Provide an association between the ModelForm and a models
		model = WorkFlow
		exclude = ('slug', 'views', 'downloads', 'client_ip', 'created')


	def clean(self):
		cleaned_data = self.cleaned_data
		url = cleaned_data.get('url')

		if url and not url.startswith('http://'):
			url = 'http://' + url
			cleaned_data['url'] = url;
			return cleaned_data; 	
