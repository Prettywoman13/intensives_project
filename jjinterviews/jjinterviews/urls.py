from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("homepage.urls", namespace="homepage")),
    path("feedback/", include("feedback.urls", namespace="feedback")),
    path("auth/", include("users.urls", namespace="users")),
    path("auth/", include("django.contrib.auth.urls")),
    path("interview/", include("interviews.urls", namespace="interviews")),
    path("summernote/", include("django_summernote.urls")),
    path("statistic/", include("statistic.urls", namespace="statistic")),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
