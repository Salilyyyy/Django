from django.urls import path
from myapp.views import my_async_view, safe_async_view, non_cache_view, async_view_using_sync_function

urlpatterns = [
    path('async/', my_async_view, name='my_async_view'),
    path('safe/', safe_async_view, name='safe_async_view'),
    path('no-cache/', non_cache_view, name='non_cache_view'),
    path('sync/', async_view_using_sync_function, name='sync_view'),
]