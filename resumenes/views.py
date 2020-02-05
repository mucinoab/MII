from django.shortcuts import render

# Create your views here.
def res_view(request):
  return render(request, "resumenes.html")
