from django import forms

from . models import Services, Clients

class CreateServiseForm(forms.ModelForm):

    class Meta:
        model = Services
        fields = '__all__'


class CreateClientForm(forms.ModelForm):

    class Meta:
        model = Clients
        fields = '__all__'