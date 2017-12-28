from django import forms
from basicapp import models

from urllib.parse import urlparse

class LinkForm(forms.ModelForm):
    class Meta():
        model=models.Link
        exclude=('shortenURL',)

    def clean_targetURL(self):
        targetURL=self.cleaned_data['targetURL'].lower()
        if urlparse(targetURL).scheme=='':
            targetURL='http://'+targetURL
        return targetURL
