from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
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
            return HttpResponseRedirect("/simple-file-upload")
