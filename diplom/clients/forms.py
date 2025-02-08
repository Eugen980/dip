from django import forms

from .models import Clients


class CreateClientForm(forms.ModelForm):

    class Meta:
        model = Clients
        fields = ['last_name', 'first_name', 'patronymic', 'bank', 'phone', 'date_of_birth', 'passports_series', 'passports_number', 'services', 'user_state']