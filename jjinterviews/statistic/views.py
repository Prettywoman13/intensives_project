from django.views.generic import ListView

from interviews.models import InterviewStatistic


class StatisticMainPage(ListView):
    model = InterviewStatistic
    template_name = "pages/statistic/main.html"

    def get_queryset(self):
        return self.model.objects.all().filter(user=self.request.user)
