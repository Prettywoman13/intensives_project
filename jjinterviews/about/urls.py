from about import views
from django.urls import path

app_name = "about"

urlpatterns = [path("", views.AboutView.as_view(), name="main")]