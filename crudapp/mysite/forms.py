# In forms.py (nieuw bestand)

from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'grade']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'grade': forms.NumberInput(attrs={'class': 'form-control'}),
        }