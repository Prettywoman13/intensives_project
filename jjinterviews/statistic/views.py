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
        bad_rates = statistic.filter(mark=0).count()
        if bad_rates:
            rates.append(bad_rates)
            values.append("Плохо")

        normal_rates = statistic.filter(mark=1).count()
        if normal_rates:
            rates.append(normal_rates)
            values.append("Нормально")

        good_rates = statistic.filter(mark=2).count()
        if good_rates:
            rates.append(good_rates)
            values.append("Хорошо")

        all_questions = statistic.count()
        if all_questions != (bad_rates + normal_rates + good_rates):
            remaining_questions = all_questions - (
                bad_rates + normal_rates + good_rates
                )
            rates.append(remaining_questions)
            values.append("Неоцененные ответы")
        data["all_questions"] = all_questions
        data["pk"] = pk
        data["interview"] = kwargs["object"]
        data["rates"] = rates
        data["values"] = values
        return data
