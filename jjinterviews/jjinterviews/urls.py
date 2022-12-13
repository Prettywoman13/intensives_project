from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/", include("about.urls", namespace="about")),
    # path("create/", include("interviews.urls", namespace="interviews")),
    path("", include("homepage.urls", namespace="homepage")),
    path("auth/", include("users.urls", namespace="users")),
]
