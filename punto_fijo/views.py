from django.shortcuts import render
from .forms import In, E1, E2, E3

from sympy import symbols, sympify, solve

from base64 import b64encode
from io import BytesIO
from traceback import print_exc
from urllib import parse

import matplotlib.pyplot as plt
import numpy as np

from error.views import errors_view


def fijo_view(request):
    form = In()
    context = {"form": form}

    if request.method == 'GET':
        form = In(request.GET)
        if form.is_valid():

            if form.cleaned_data['n'] == 1:
                return fijo_input(request, 1)

            elif form.cleaned_data['n'] == 2:
                return fijo_input(request, 2)

            else:
                return fijo_input(request, 3)

    return render(request, "fijo_elejir.html", context)


def fijo_input(request, n):

    if n == 1:
        form = E1()
    elif n == 2:
        form = E2()
    else:
        form = E3()




    if request.method == 'GET':
        if n == 1:
            form = E1(request.GET)
        elif n == 2:
            form = E2(request.GET)
        else:
            form = E3(request.GET)

        if form.is_valid():
            print("paso")
            return fijo_calcula(request, form, n)
        else:
            print(form.cleaned_data, form.errors)

        context = {"form": form}
            
    return render(request, "fijo_input.html", context)


def fijo_calcula(request, form, n):

    #inicia cosas de sympy
    x, y, z, t = sympy.symbols('x y z t')

    #Inicia cosas de matplotlib
    plt.rcParams.update(plt.rcParamsDefault)
    plt.close('all')


    valores = form.cleaned_data #obtiene el input
    context = {'form': form}

    if n == 1:
        funo = valores['fx']
        x0 = valores['x0']

        fux = sympify(funo)

        fx = sympify(str(solve(fux, x, implicit=True, quick=True, manual=True)).strip('[]'))

        for z in range(10):
            x0 = round(fx.subs(x, x0))
            print(x0.n(4), fx.subs(x, x0) )

    #
    #
    # elif n == 2:
    # else:



    return render(request, "fijo_calculado.html", context)
















