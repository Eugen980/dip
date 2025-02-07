from django import forms

from . models import Bid

class CreateBidForm(forms.ModelForm):

    class Meta:
        model = Bid
        fields = '__all__'