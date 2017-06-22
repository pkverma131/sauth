from django import forms

class FetchForm(forms.Form):
    asset_code = forms.CharField(label='asset_code', max_length=32)
