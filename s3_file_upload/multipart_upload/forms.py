from django import forms


class MultipartUploadForm(forms.Form):
    file = forms.FileField()
