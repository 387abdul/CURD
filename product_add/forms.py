from django import forms
from .models import Create

class CreateForm(forms.ModelForm):
    class Meta:
        model = Create
        fields = ['name', 'description', 'price', 'image']
