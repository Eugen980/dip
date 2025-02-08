from django import forms

from . models import Reports

class CreateReportForm(forms.ModelForm):

    class Meta:
        model = Reports
        fields = '__all__'