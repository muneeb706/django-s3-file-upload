import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views import View

from .forms import SimpleFileUploadForm
from shared_utils.s3fileupload import S3Upload

s3uploader = S3Upload()


class SimpleFileUploadView(View):

    def get(self, request):
        form = SimpleFileUploadForm()
        return render(request, "file_upload_form.html", {
            "form": form,
            "title": 'Simple File Upload',
            "upload_url": 'simple-file-upload'
        })

    def post(self, request):
        submitted_form = SimpleFileUploadForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            file = request.FILES["file"]
            s3uploader.upload(file.file, file.name, file.content_type, file.size)
            return HttpResponse(json.dumps({'status': 'uploaded'}), content_type="application/json")


def progress(request):
    if request.method == 'GET':
        return HttpResponse(json.dumps(s3uploader.get_upload_status()),
                            content_type="application/json")
    else:
        return HttpResponseBadRequest('Invalid Request Method. Only GET is allowed')
