from django.contrib import admin
from django.urls import include, path

from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls

private_urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
]

urlpatterns = [path("", include(wagtail_urls))]

urlpatterns = (
    private_urlpatterns
    + urlpatterns
    + [
        # Add Wagtail URLs at the end.
        # Wagtail cache-control is set on the page models's serve methods.
    ]
)
