from django import forms
from data.models import Category, WorkFlow

class WorkFlowForm(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text="Please enter the name of the workflow.")
    categories = models.ManyToManyField(Category, blank=False)
    keywords = CharField(max_length=256, help_text="Please enter the keywords for workflow")
	description = forms.CharField(max_length=512, help_text="Please write a description for the workflow")
	versionInit = forms.CharField(max_length=128, help_text="Enter the versionInit")

	class Meta:
		# Provide an association between the ModelForm and a models
		model = WorkFlow
		exclude = ('categories',)
