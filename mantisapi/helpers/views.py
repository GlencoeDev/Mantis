from django.shortcuts import render

# Create your views here.


def handleError400(request, exception):
    return render(request, "pages/errors/error-400.html")


def handleError403(request, exception):
    return render(request, "pages/errors/error-403.html")


def handleError404(request, exception):
    return render(request, "pages/errors/error-404.html")


def handleError500(request):
    return render(request, "pages/errors/error-500.html")
