from django import forms
from basicapp import models
class LinkForm(forms.ModelForm):
    class Meta():
        model=models.Link
        fields=('targetURL','label')
