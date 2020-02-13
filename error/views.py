from django.shortcuts import render


# Create your views here.

def errors_view(request):
    return render(request, "error.html")
