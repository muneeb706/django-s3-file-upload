from django.core.files.uploadhandler import FileUploadHandler
from django.core.cache import cache


class FileUploadProgressHandler(FileUploadHandler):

    def __init__(self, request=None):
        super(FileUploadProgressHandler, self).__init__(request)
        self.file_name = None
        self.file_size = None

    def new_file(self, field_name, file_name, content_type, content_length, charset=None, content_type_extra=None):
        self.file_name = file_name
        cache.set(self.file_name, {
            'uploaded_size': 0,
            'progress_perc': 0
        })

    def handle_raw_input(self, input_data, META, content_length, boundary, encoding=None):
        self.file_size = content_length

    def receive_data_chunk(self, raw_data, start):
        if self.file_name:
            file_upload_status = cache.get(self.file_name)
            file_upload_status['uploaded_size'] += self.chunk_size
            file_upload_status['progress_perc'] = (file_upload_status['uploaded_size'] / self.file_size) * 100
            cache.set(self.file_name, file_upload_status)
        return raw_data

    def file_complete(self, file_size):
        if self.file_name:
            file_upload_status = cache.get(self.file_name)
            file_upload_status['uploaded_size'] = self.file_size
            file_upload_status['progress_perc'] = 100
            cache.set(self.file_name, file_upload_status)

    def upload_complete(self):
        print(cache.get(self.file_name))