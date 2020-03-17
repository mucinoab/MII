# import sys
# import time
from base64 import b64encode
from io import BytesIO
# from traceback import print_exc
from urllib import parse

import matplotlib.pyplot as plt
import numpy as np
import sympy
from django.shortcuts import render
from sympy import *

from .forms import In, E1, E2, E3


def estiliza_string(fucn):
    superscript_map = {"0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸",
                       "9": "⁹", "x": "ˣ", "y": "ʸ", "z": "ᶻ"}
    nuevo = ''
    c = 0
    p = len(fucn)

    while c < p:
        if fucn[c] == '*':
            if fucn[c + 1] == '*':
                nuevo += superscript_map[fucn[c + 2]]
                c += 2
        else:
            nuevo += fucn[c]
        c += 1
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

    return render(request, "fijo_elegir.html", context)


def fijo_input(request, n):
    if n == 1:
        form = E1()
    elif n == 2:
        form = E2()
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

    # start = time.time()

    iteraciones = 20

    # inicia cosas de sympy
    x, y, z = sympy.symbols('x y z')

    # Inicia cosas de matplotlib
    plt.rcParams.update(plt.rcParamsDefault)
    plt.close('all')

    valores = request.POST  # obtiene el input

    n = len(request.POST)  # 1 llave y par de valores por ecuación.

    if n == 3:  # una variable
        funo = str(valores['fx'])  # +"+x"
        x0 = float(valores['x0'])

        # print(type(x0), type(funo), x0, funo)

        # x, y, z = sympy.symbols('x y z')
        fux = sympy.sympify(funo)

        # print(sympy.solve(fux, 0, implicit=True, numerical=False, warn=True, manual=True, cubics=True))

        fx = sympy.sympify(str(sympy.solve(fux, x, implicit=True, quick=True, manual=True)).strip('[]'))

        for q in range(10):
            x0 = round(fx.subs(x, x0))
            print(x0.n(4), fx.subs(x, x0))

    elif n == 5:  # dos variables

        resul = {'titulos': ['n', 'Xn', 'Yn'], 'filas': []}

        funo = sympy.sympify(valores['fx'])
        x0 = float(valores['x0'])

        fundos = sympy.sympify(valores['fy'])
        y0 = float(valores['x0'])

        fx = sympy.sympify(str(sympy.solve(funo, x, implicit=True, rational=False)).strip('[]'))
        fy = sympy.sympify(str(sympy.solve(fundos, y, implicit=True, rational=False)).strip('[]'))

        for q in range(1, iteraciones + 1):
            # x0 = fx.subs({x: x0, y: y0})
            # y0 = fy.subs({x: x0, y: y0})
            x0 = round(fx.subs({x: x0, y: y0}), 8)
            y0 = round(fy.subs({x: x0, y: y0}), 8)

            resul['filas'].append([q, x0.n(5), y0.n(5)])

        context = {'context': resul}

        # graficación

        plt.rc_context({'axes.edgecolor': 'w', 'xtick.color': 'w', 'ytick.color': 'w'})
        plt.style.use("dark_background")

        titulo = '\n' + estiliza_string(valores['fx']) + "  y  " + estiliza_string(valores['fy']) + '\n'

        p1 = plot_implicit(funo, show=False, line_color='#27864d', title=titulo)
        p2 = plot_implicit(fundos, show=False, line_color='#40E0D0')
        p1.extend(p2)

        p1.show()
        buf = BytesIO()
        # experimental, que la compresión dependa del timepo, para así dar una respuesta más rádi

        p1._backend.fig.savefig(buf, format='jpg', quality=90, bbox_inches='tight', facecolor="#000000",
                                edgecolor='#000000', dpi=150, transparent=True)
        # p1._backend.fig.savefig(buf, format='png', quality=1, facecolor="#004c3f", edgecolor='#004c3f', dpi=150, transparent=True)
        buf.seek(0)
        uri = 'data:image/png;base64,' + parse.quote(b64encode(buf.read()))
        context['image'] = uri

        # print(sys.getsizeof(buf))
        # end = time.time()
        # print(end - start)

    return render(request, "fijo_calculado.html", context)


def fijo_ejemplo_1(request):  # Ejemplo 1 para una variable

    # Calculando valores

    iteraciones = 20
    resul = {'titulos': ['n', 'Xn', 'f(x)'], 'filas': []}

    x = sympy.symbols('x')

    # Ejemplos de Curiel
    fun = "x**3+4*x**2-10"
    gx = "sqrt((10)/(x+4))"
    x0 = 1

    fuxx = sympy.lambdify(x, fun, "math")
    gxxx = sympy.lambdify(x, gx, "math")

    for q in range(1, iteraciones + 1):
        x0 = gxxx(x0)
        num = "{0:.6f}".format(fuxx(x0))
        resul['filas'].append([q, "{0:.6f}".format(x0), num])

    context = {'context': resul}

    # Graficación

    plt.rcParams.update(plt.rcParamsDefault)
    plt.close('all')

    r = float(resul['filas'][-1][1])
    t = np.arange(r - 5, r + .5, .1)
    s = []
    for n in t:
        s.append(fuxx(n))

    plt.rc_context({'axes.edgecolor': 'black', 'xtick.color': 'black', 'ytick.color': 'black'})
    # plt.style.use("dark_background")
    fig, ax = plt.subplots()

    ax.axhline(0, color='black')

    ax.plot(t, s, label=f'f(x) = {estiliza_string(fun)}', color='navy')
    ax.grid(color="gray")

    plt.plot(r, fuxx(r), marker='o', markersize=5, color="red", label=f"Corte con Eje x = {r:.4f}")
    ax.set(xlabel='x', ylabel='f(x)', title=f"Raíz calculada después de {iteraciones} iteraciones")

    plt.legend(loc='best')

    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=160, transparent=True)
    buf.seek(0)
    uri = 'data:image/png;base64,' + parse.quote(b64encode(buf.read()))
    context['image'] = uri

    return render(request, "fijo_calculado.html", context)


def fijo_ejemplo_2(request):  # Ejemplo 2 para una variables

    # Calculando valores

    iteraciones = 10
    resul = {'titulos': ['n', 'Xn', 'Yn', 'f(x, y)', 'g(x, y)'], 'filas': []}

    x, y = sympy.symbols('x y')

    # Ejemplos de Curiel
    funx = "x**2-10*x+y**2+8"
    funy = "x*y**2+x-10*y+8"

    # despejes
    fx = "(x**2+y**2+8)/(10)"
    fy = "(x*y**2+x+8)/(10)"
    x0 = 0
    y0 = 0

    fux = sympy.sympify(funx)
    fuy = sympy.sympify(funy)

    # fxx = sympy.sympify(fx)
    # fyy = sympy.sympify(fy)

    fxn = sympy.lambdify([x, y], funx, "numpy")
    fyn = sympy.lambdify([x, y], funy, "numpy")

    fxxn = sympy.lambdify([x, y], fx, "numpy")
    fyyn = sympy.lambdify([x, y], fy, "numpy")

    for q in range(1, iteraciones + 1):
        x0 = fxxn(x0, y0)
        y0 = fyyn(x0, y0)

        num = fxn(x0, y0)
        num2 = fyn(x0, y0)

        resul['filas'].append([q, f'{x0:.6}', f'{y0:.6}', f'{num:.6}', f'{num2:.6}'])

    context = {'context': resul}

    # Graficación

    plt.rc_context({'axes.edgecolor': 'black', 'xtick.color': 'black', 'ytick.color': 'black'})

    titulo = '\n' + estiliza_string(funx) + "  y  " + estiliza_string(funy) + '\n'

    p1 = plot_implicit(fux, (x, x0 - 1.5, x0 + 1.5), (y, y0 - 1, y0 + 1), show=False, line_color='#27864d',
                       title=titulo, adaptative=False, points=1)
    p2 = plot_implicit(fuy, (x, x0 - 1.5, x0 + 1.5), (y, y0 - 1, y0 + 1), show=False, line_color='#40E0D0',
                       adaptative=False, points=1)
    p1.extend(p2)

    buf = BytesIO()
    p1.show()

    p1._backend.fig.savefig(buf, format='jpg', quality=90, bbox_inches='tight', facecolor="#f3f2f1",
                            edgecolor='#f3f2f1', dpi=150)
    buf.seek(0)
    uri = 'data:image/png;base64,' + parse.quote(b64encode(buf.read()))
    context['image'] = uri
    return render(request, "fijo_calculado.html", context)


def fijo_ejemplo_3(request):  # Ejemplo 3 para una variables
    # unset_show()

    # calculando valores
    iteraciones = 15
    resul = {'titulos': ['n', 'Xn', 'Yn', 'f(x, y)', 'g(x, y)'], 'filas': []}
    context = {}

    # x, y = symbols('x y')
    # p1 = plot3d(x * y, (x, -5, 5), (y, -5, 5), show=False, title="Fijo")
    # p1.show()
    #
    # buf = BytesIO()
    # p1._backend.fig.savefig(buf, format='jpg', quality=90, bbox_inches='tight', facecolor="#000000",
    #                         edgecolor='#000000', dpi=150, transparent=True)
    # buf.seek(0)
    # uri = 'data:image/png;base64,' + parse.quote(b64encode(buf.read()))
    # context['image'] = uri

    return render(request, "fijo_calculado.html", context)
