import json

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.core.cache import cache
from .forms import SimpleFileUploadForm
from .models import File


class SimpleFileUploadView(View):

    def get(self, request):
        form = SimpleFileUploadForm()
        return render(request, "simple_file_upload/simple_file_upload.html", {
            "form": form
        })

    def post(self, request):
        submitted_form = SimpleFileUploadForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            file = File(path=request.FILES["file"])
            file.save()
            return HttpResponse(json.dumps({'status': 'uploaded'}), content_type="application/json")


def progress(request):
    if request.method == 'GET' and request.GET['filename']:
        file_name = request.GET['filename']
        return HttpResponse(json.dumps({'progress_perc': cache.get(file_name)['progress_perc']}),
                            content_type="application/json")

    else:
        return HttpResponse(json.dumps({'error': 'Only Get request with filename parameter is allowed '}),
                            content_type="application/json")