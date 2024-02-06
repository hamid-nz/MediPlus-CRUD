# forms.py
from django import forms
from .models import Page, TopCard

class PageForm(forms.ModelForm):
    class Meta:
        model = Page

class TopCardForm(forms.Form):
    class Meta:
        model = TopCard

