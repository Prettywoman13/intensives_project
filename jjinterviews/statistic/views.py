from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView

from interviews.models import Interview, InterviewStatistic, QuestionStatistic


class StatisticMainPage(LoginRequiredMixin, ListView):
    model = InterviewStatistic
    template_name = "pages/statistic/main.html"
    context_object_name = "statistics"

    def get_queryset(self):
        return self.model.objects.all().filter(user=self.request.user)


class InterviewDetailStatistic(DetailView):
    model = Interview
    template_name = "pages/statistic/detail.html"
    context_object_name = "item"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        pk = kwargs["object"].id
        statistic = QuestionStatistic.objects.filter(interview=pk)
        bad = statistic.filter(mark=0).count()
        normal = statistic.filter(mark=1).count()
        good = statistic.filter(mark=2).count()
        data["pk"] = pk
        data["interview"] = kwargs["object"]
        data["all_questions"] = statistic.count()
        data["rates"] = [bad, normal, good]
        return data
