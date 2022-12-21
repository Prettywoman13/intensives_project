from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView

from interviews.models import Interview, InterviewStatistic, QuestionStatistic


class StatisticMainPage(LoginRequiredMixin, ListView):
    model = InterviewStatistic
    template_name = "pages/statistic/main.html"
    context_object_name = "statistics"

    def get_queryset(self):
        """
        Получаю всю статистику по собеседованиям от юзера
        """
        return (
            self.model.objects.all()
            .filter(user=self.request.user)
            .order_by("-interview__created_at")
        )


class InterviewDetailStatistic(DetailView):
    """
    Вью детальной статистики
    """
    model = Interview
    template_name = "pages/statistic/detail.html"
    context_object_name = "item"

    def get_context_data(self, **kwargs) -> dict:
        data = super().get_context_data(**kwargs)
        pk = kwargs["object"].id
        statistic = QuestionStatistic.objects.filter(interview=pk)
        rates = []
        values = []
        bad = statistic.filter(mark=0).count()
        if bad:
            rates.append(bad)
            values.append("Плохо")
        normal = statistic.filter(mark=1).count()
        if normal:
            rates.append(normal)
            values.append("Нормально")
        good = statistic.filter(mark=2).count()
        if good:
            rates.append(good)
            values.append("Хорошо")
        all_questions = statistic.count()
        if all_questions != (bad + normal + good):
            remaining_questions = all_questions - (bad + normal + good)
            rates.append(remaining_questions)
            values.append("Неоцененные ответы")
        data["all_questions"] = all_questions
        data["pk"] = pk
        data["interview"] = kwargs["object"]
        data["rates"] = rates
        data["values"] = values
        return data
