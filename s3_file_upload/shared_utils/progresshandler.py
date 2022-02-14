import threading
from time import perf_counter

from django.core.cache import cache


class ProgressHandler(object):

    def __init__(self, cache_key_prefix, filename, size):
        self._filename = filename
        self._size = size
        self.perf_counter_start = perf_counter()

        self.cache_key = f'{cache_key_prefix}_{self._filename}'

        cache.set(self.cache_key, {
            'uploaded_size': 0,
            'progress_perc': 0,
            'time_taken_s': 0
        })

        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        with self._lock:
            upload_status = cache.get(self.cache_key)
            upload_status['uploaded_size'] += bytes_amount
            upload_status['progress_perc'] = int((upload_status['uploaded_size'] / self._size) * 100)
            upload_status['time_taken_s'] = perf_counter() - self.perf_counter_start
            cache.set(self.cache_key, upload_status)

    def get_upload_status(self):
        upload_status = cache.get(self.cache_key)
        if upload_status:
            return {'progress_perc': upload_status['progress_perc'],
                    'time_taken_s': round(upload_status['time_taken_s'], 2)}

        return {'progress_perc': 0, 'time_taken_s': 0}
