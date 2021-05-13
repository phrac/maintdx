from django.shortcuts import render


def index(request):
    context = None
    return render(request, "index.html", context)
