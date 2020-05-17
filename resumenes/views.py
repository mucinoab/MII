from django.shortcuts import render
from django.views.decorators.gzip import gzip_page


def metodos_views(request):
    return render(request, "metodos.html")


def creditos_views(request):
    return render(request, "creditos.html")


def tuto_views(request):
    return render(request, "tutorial.html")


@gzip_page
def res_view(request):
    return render(request, "resumenes.html")
