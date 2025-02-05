from django import forms

from .models import Clients


class CreateClientForm(forms.ModelForm):

    class Meta:
        model = Clients
        fields = '__all__'