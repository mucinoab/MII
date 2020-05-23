from newton.views import errors_view
from django.shortcuts import render
from Regla_Trapezoidal.forms import forma
import numpy as np
import sympy

from base64 import b64encode
from io import BytesIO
from traceback import print_exc
from urllib import parse
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def Sim38_views(request):
    form = forma()
    context = {"form": form}

    if request.method == 'GET':
        form = forma(request.GET)

        if form.is_valid():
            return Sim38_Calcula(request, form)

    return render(request, "Sim_38_input.html", context)

def Sim38_Calcula(request, form):
    return form
