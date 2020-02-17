from base64 import b64encode
from io import BytesIO
# from traceback import print_exc
from urllib import parse

import matplotlib.pyplot as plt
import sympy
from django.shortcuts import render
from sympy import *

from .forms import In, E1, E2, E3


# import numpy as np


def estiliza_string(fucn):
    superscript_map = {
        "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶",
        "7": "⁷", "8": "⁸", "9": "⁹"}
    nuevo = ''
    for c in range(len(fucn)):
        if fucn[c] == '*':
            if fucn[c + 1] == '*':
                nuevo += superscript_map[fucn[c + 2]]
                c += 4
        else:
            nuevo += fucn[c]

    return nuevo


def fijo_view(request):
    form = In()
    context = {"form": form}

    if request.method == 'POST':

        form = In(request.POST)

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
        print("forma")
    elif n == 2:
        form = E2()
        print("2")

    else:
        form = E3()

    # if request.method == 'POST':
    #
    #     print(request.POST, "holapp")
    #     if n == 1:
    #         form = E1(request.GET)
    #     elif n == 2:
    #         form = E2(request.GET)
    #     else:
    #         form = E3(request.GET)
    #
    #
    #     if form.is_valid():
    #         context["form"] = form
    #         return fijo_calcula(request, form, n)
    #     else:
    #         print("no paso", form.cleaned_data, form.errors.as_data())

    context = {"form": form}

    return render(request, "fijo_input.html", context)


def fijo_calcula(request):
    # print(request.POST, len(request.POST))

    iteraciones = 20

    # inicia cosas de sympy
    x, y, z = sympy.symbols('x y z')

    # Inicia cosas de matplotlib
    plt.rcParams.update(plt.rcParamsDefault)
    plt.close('all')

    valores = request.POST  # obtiene el input

    n = len(request.POST)  # 1 llave y par de valores por ecuación.

    if n == 3:
        funo = str(valores['fx'])  # +"+x"
        x0 = float(valores['x0'])

        print(type(x0), type(funo), x0, funo)

        x, y, z = sympy.symbols('x y z')
        fux = sympy.sympify(funo)

        print(sympy.solve(fux, 0, implicit=True, numerical=False, warn=True, manual=True, cubics=True))

        # fx = sympy.sympify(str(sympy.solve(fux, x, implicit=True, quick=True, manual=True)).strip('[]'))

        for q in range(10):
            x0 = round(fx.subs(x, x0))
            print(x0.n(4), fx.subs(x, x0))

    elif n == 5:

        resul = {'titulos': ['n', 'Xn', 'Yn'], 'filas': []}

        funo = sympy.sympify(valores['fx'])
        x0 = float(valores['x0'])

        fundos = sympy.sympify(valores['fy'])
        y0 = float(valores['x0'])

        fx = sympy.sympify(str(sympy.solve(funo, x, implicit=True, rational=False)).strip('[]'))
        fy = sympy.sympify(str(sympy.solve(fundos, y, implicit=True, rational=False)).strip('[]'))

        for q in range(1, iteraciones + 1):
            x0 = round(fx.subs({x: x0, y: y0}), 25)
            y0 = round(fy.subs({x: x0, y: y0}), 25)

            resul['filas'].append([q, x0.n(6), y0.n(6)])

        context = {'context': resul}

        # graficación

        plt.rc_context({'axes.edgecolor': 'w', 'xtick.color': 'w', 'ytick.color': 'w'})
        plt.style.use("dark_background")

        titulo = estiliza_string(valores['fx']) + " and " + estiliza_string(valores['fy'])

        p1 = plot_implicit(funo, show=False, line_color='navy', title=titulo)
        p2 = plot_implicit(fundos, show=False, line_color='#4c002c')
        p1.extend(p2)

        p1.show()
        buf = BytesIO()
        p1._backend.fig.savefig(buf, format='png', dpi=150, transparent=True)
        buf.seek(0)
        uri = 'data:image/png;base64,' + parse.quote(b64encode(buf.read()))
        context['image'] = uri

    return render(request, "fijo_calculado.html", context)
