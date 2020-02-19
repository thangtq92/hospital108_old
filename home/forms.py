# home/forms.py

from django import forms
from .models import Menu

class CreateMenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'description', 'status' , 'id_parent']