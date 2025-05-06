from django import forms
from .models import PetrolEntry

class PetrolEntryForm(forms.ModelForm):
    class Meta:
        model = PetrolEntry
        fields = ['date', 'bikes', 'amount']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'bikes': forms.CheckboxSelectMultiple()
        }
