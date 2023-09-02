# MainApp URL

from django.urls import path
from .views import UploadCSVView, download_json

urlpatterns = [
    path('upload/', UploadCSVView.as_view(), name='upload_csv'),   #path to upload_csv.html file
    path('download/', download_json, name='download_json'),
]
