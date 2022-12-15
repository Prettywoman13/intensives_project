from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import FeedBackForm
from users.models import User


def feedback(request):
    form = FeedBackForm(request.POST or None)
    context = {"form": form}

    if request.method == "POST" and form.is_valid():
        text = form.cleaned_data["text"]
        mail = form.cleaned_data["mail"]
        send_mail(
            "Здравствуйте, админ. Вам пришла обратная связь.",
            text,
            mail,
            [user.email for user in User.objects.filter(is_superuser=True)],
            fail_silently=True,
        )
        form.save()
        messages.success(request, "Сообщение отправлено," "мы вас очень ценим")
        return redirect("feedback:main")
    return render(
        request, template_name="pages/feedback.html", context=context
    )
