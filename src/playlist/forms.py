from django import forms
from .models import videolink

class getlink(forms.ModelForm):

    class Meta:
        model = videolink
        fields = '__all__'

    def clean(self):
        data = self.cleaned_data
        return data

class downlink(forms.ModelForm):

    class Meta:
        model = videolink
        fields = '__all__'

    def clean(self):
        data = self.cleaned_data
        return data
