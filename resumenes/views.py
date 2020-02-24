from django.shortcuts import render
from django.views.decorators.gzip import gzip_page

def metodos_views(request):
    return render(request, "metodos.html")

@gzip_page
def res_view(request):
    return render(request, "resumenes.html")
