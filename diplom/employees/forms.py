from django import forms

from .models import Emolyees


class CreateEmployeeForm(forms.ModelForm):

    class Meta:
        model = Emolyees
        fields = '__all__'