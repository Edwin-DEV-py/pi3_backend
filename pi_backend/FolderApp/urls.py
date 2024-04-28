from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path(r'^getFolder/(?P<parentFolder>\d+)/$', GetFolderByParentId.as_view(),name="folderByParent"),
    path('getFolder/', GetFolderByParentId.as_view(),name="folderNotParent"),
]