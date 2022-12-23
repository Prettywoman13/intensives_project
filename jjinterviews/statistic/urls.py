from django.urls import path

from .views import InterviewDetailStatistic, StatisticMainPage

app_name = "statistic"

urlpatterns = [
    path("", StatisticMainPage.as_view(), name="main"),
    path("detail/<int:pk>", InterviewDetailStatistic.as_view(), name="detail"),
]
