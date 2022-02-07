import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views import View
from shared_utils.utils import get_upload_status_from_cache

from .forms import SimpleFileUploadForm
from .models import File


class SimpleFileUploadView(View):

    def get(self, request):
        form = SimpleFileUploadForm()
        return render(request, "file_upload_form.html", {
            "form": form,
            "title": 'Simple File Upload',
            "upload_url": '/simple_file_upload/'
        })

    def post(self, request):
        submitted_form = SimpleFileUploadForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            file = File(path=request.FILES["file"])
            file.save()
            return HttpResponse(json.dumps({'status': 'uploaded'}), content_type="application/json")


def progress(request):
    if request.method == 'GET' and request.GET['filename']:
        filename = request.GET['filename']
        return HttpResponse(json.dumps(get_upload_status_from_cache(filename)),
                            content_type="application/json")
    else:
        return HttpResponseBadRequest('Invalid Request Method. Only GET is allowed')
