from django.shortcuts import render
from django.views.decorators.gzip import gzip_page

@gzip_page
def res_view(request):
  return render(request, "resumenes.html")
