from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index),
    path('cats/<int:catid>/', category),
    re_path(r'^arhive/(?P<year>[0-9]{4})/', arhive),
]
