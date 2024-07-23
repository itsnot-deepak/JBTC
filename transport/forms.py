from django import forms
from .models import LoadInfo

class LoadInfoForm(forms.ModelForm):
    class Meta:
        model = LoadInfo
        fields = ['name', 'weight', 'size', 'pickup_location', 'drop_location', 'date', 'mobile_number', 'time_of_pickup']
