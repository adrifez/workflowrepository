from django import forms
from data.models import WorkFlow, Category


class SearchForm(forms.ModelForm):
	search = forms.CharField(max_length=128, help_text="Please enter the workflow name.")

	# An inline class to provide additional information on the form.
	class Meta:
 	# Provide an association between the ModelForm and a model
 		model = Workflow
        fields = ('name',)
