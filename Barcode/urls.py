"""
URL configuration for Barcode project.
"""

from django.contrib import admin
from django.urls import path, include
from core.urls import urlpatterns as core_urls
from core.api.urls import urlpatterns as core_api_urls

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language

urlpatterns = [
    path("admin/", admin.site.urls),  
    path("summernote/", include("django_summernote.urls")),
]

urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls), 
    path("", include(core_urls)),  
    path("set_language/", set_language, name="set_language"),
    path("rosetta/", include("rosetta.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include(core_api_urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
