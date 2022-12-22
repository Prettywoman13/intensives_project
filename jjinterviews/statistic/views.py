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
        statistic = QuestionStatistic.objects.get_all_stats()
        bad = 0
        normal = 0
        good = 0
        non_rated = 0
        rates = []
        values = []
        for note in statistic:
            mark = note.mark
            match mark:
                case 0:
                    bad += 1
                case 1:
                    normal += 1
                case 2:
                    good += 1
                case _:
                    non_rated += 1

        if bad:
            rates.append(bad)
            values.append("Плохо")

        if normal:
            rates.append(normal)
            values.append("Нормально")

        if good:
            rates.append(good)
            values.append("Хорошо")

        if non_rated:
            rates.append(non_rated)
            values.append("Неоцененные ответы")

        data["all_questions"] = len(statistic)
        data["pk"] = pk
        data["interview"] = kwargs["object"]
        data["rates"] = rates
        data["values"] = values
        return data
