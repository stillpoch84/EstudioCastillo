from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from listados.views import AutonomosListView

urlpatterns = [
path('listadoautonomos/', AutonomosListView.as_view(), name='listado_autonomos'),
path('ckeditor/', include('ckeditor_uploader.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)