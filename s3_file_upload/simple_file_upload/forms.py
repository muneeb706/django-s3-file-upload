from django import forms


class SimpleFileUploadForm(forms.Form):
    file = forms.FileField()
