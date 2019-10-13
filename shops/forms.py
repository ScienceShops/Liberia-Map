from django import forms


class NewShopForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
