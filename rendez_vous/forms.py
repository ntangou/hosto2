from django import forms
from .models import Rdv

class RdvForm(forms.ModelForm):

    class Meta:
        model = Rdv
        fields = ('nom', 'prenom', 'date', 'heure',)
        widgets = {
            'date': forms.DateInput(attrs={'type':'date'}),
        }


