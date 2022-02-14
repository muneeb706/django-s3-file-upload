import boto3
from boto3.s3.transfer import TransferConfig

from .progresshandler import ProgressHandler
from s3_file_upload import settings


class S3Uploader(object):

    def __init__(self):
        self.s3 = boto3.client('s3',
                               aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                               aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY, )
        self.config = TransferConfig(
            multipart_threshold=1024 * 100,
            max_concurrency=1,
            multipart_chunksize=1024 * 100,
            use_threads=False
        )
        self.folder_name = 'simple_file_upload'
        self.progress_handler = None

    def upload(self, file_obj, filename, file_type, file_size):
        self.progress_handler = ProgressHandler(self.folder_name, filename, file_size)
        # TODO: why fileobj?
        self.s3.upload_fileobj(file_obj,
                               settings.AWS_STORAGE_BUCKET_NAME,
                               f'{self.folder_name}/{filename}',
                               ExtraArgs={'ContentType': file_type},
                               Config=self.config,
                               Callback=self.progress_handler)

    def get_upload_status(self):
        if self.progress_handler:
            return self.progress_handler.get_upload_status()
        return None


class S3ParallelMultipartUploader(S3Uploader):

    def __init__(self):
        super(S3ParallelMultipartUploader, self).__init__()

        # TODO: talk about config in a bit detail, how to decide concurrency and threshold
        self.config = TransferConfig(
            multipart_threshold=1024 * 100,
            max_concurrency=10,
            multipart_chunksize=1024 * 100,
            use_threads=True
        )

        self.folder_name = 'multipart_upload'
