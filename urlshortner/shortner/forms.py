from django import forms
from django.forms import fields
from .models import Url

class SubmitUrl(forms.ModelForm):
    class Meta:
        model = Url
        fields = ['original_url', 'short_url']
        widgets = {'short_url': forms.HiddenInput()}