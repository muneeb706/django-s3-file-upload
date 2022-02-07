from django.core.cache import cache

def get_upload_status_from_cache(key):
    upload_status = cache.get(key)
    return {'progress_perc': upload_status['progress_perc'],
    'time_taken_s': round(upload_status['time_taken_s'], 2)}