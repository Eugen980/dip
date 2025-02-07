from django import forms

from . models import Charts

class CreateChartForm(forms.ModelForm):

    class Meta:
        model = Charts
        fields = '__all__'