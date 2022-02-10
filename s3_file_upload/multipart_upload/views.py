import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views import View

from .forms import MultipartUploadForm
from shared_utils.s3fileuploader import S3ParallelMultipartUploader

s3uploader = S3ParallelMultipartUploader()


class MultipartUploadView(View):

    def get(self, request):
        form = MultipartUploadForm()
        return render(request, "file_upload_form.html", {
            "form": form,
            "title": 'Multipart File Upload',
            "upload_url": 'multipart-upload'
        })

    def post(self, request):
        submitted_form = MultipartUploadForm(request.POST, request.FILES)
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
