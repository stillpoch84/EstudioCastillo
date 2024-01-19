from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from gestion_estudio.views import inicio

urlpatterns = [
   path('', inicio, name='inicio'),
   path('admin/', admin.site.urls),
   path('estudiocastillo/', include("app_estudiocastillo.urls")),
   path('ckeditor/', include('ckeditor_uploader.urls')),
   path("perfiles/", include("perfiles.urls")),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)