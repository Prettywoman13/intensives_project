from django.shortcuts import render


def test(request):
    return render(request, "pages/statistic/main.html")
