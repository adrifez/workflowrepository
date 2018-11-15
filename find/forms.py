from django import forms
from data.models import WorkFlow


class SearchForm(forms.Form):
    key = forms.CharField(max_length=128, help_text="Search workflow by name:")
