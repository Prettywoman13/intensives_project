from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from users.forms import UserUpdateForm

# from users.models import User


@login_required
def profile(request):
    user_form = UserUpdateForm(request.POST or None, instance=request.user)
    context = {"form": user_form, "user": request.user}
    if user_form.is_valid():
        user_form.save()
        return redirect("users:profile")
    return render(request, "pages/users/profile.html", context)
