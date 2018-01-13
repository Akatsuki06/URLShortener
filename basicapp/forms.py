from django import forms
from basicapp import models

from urllib.parse import urlparse

class LinkForm(forms.ModelForm):
    # targetURL=forms.CharField(label='URL')
    class Meta():
        model=models.Link
        fields=('targetURL',)
        widgets={
        'targetURL':forms.TextInput(attrs={'class':'form-control  input-lg','id':'shortenURL','placeholder':'paste your url here'})
        }
        labels={
        'targetURL':''
        }
#url cleaning
    # def clean_targetURL(self):
    #     targetURL=self.cleaned_data['targetURL'].lower()
    #     if urlparse(targetURL).scheme=='':
    #         targetURL='http://'+targetURL
    #     return targetURL
