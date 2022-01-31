from django import forms


class SimpleFileUploadForm(forms.Form):
    image = forms.ImageField()
