from base64 import b64encode
from io import BytesIO
from urllib import parse

import matplotlib.pyplot as plt
import numpy as np
import sympy
from django.shortcuts import render

from newton.views import estiliza_string
from .forms import datos


def lagrange_view(request):
    form = datos()
    context = {"form": form}

    if request.method == 'GET':
        form = datos(request.GET)

        if form.is_valid():
            return lagrange_calc(request, form.cleaned_data)

    return render(request, "lagrange_elegir.html", context)


def poli_lag(grado, datos):
    x = sympy.symbols('x')
    resul = ""

    for i in range(0, grado + 1):

        resul += f"{datos[i][1]}"

        for j in range(0, grado + 1):

            if j != i:
                resul += f"*((x-{datos[j][0]})/" \
                         f"({datos[i][0]}-{datos[j][0]}))"

        resul += '+'

    resul = resul.strip("+")
    return sympy.lambdify(x, resul, "math"), sympy.sympify(resul)


def lagrange_calc(request, datos, gx=""):
    # gx funcion objetivo, la que tratamos de emular.

    # resul = {"titulos": ["x", "f(x)"], "datos": []}
    dato2 = []

    c = 0
    for cc in datos:
        c += 1
        if c & 1:
            dato2.append([datos[cc], 0])
    c = 0
    ccc = 0
    for cc in datos:
        c += 1
        if c % 2 == 0:
            dato2[ccc][1] = datos[cc]
            ccc += 1

    datos = dato2

    x = sympy.symbols('x')
    f, fx = poli_lag(len(datos) - 1, datos)
    print(fx)

    t = np.arange(datos[0][0] - 2, datos[-1][0] + 2, .5)
    s = []
    m = []

    fig, ax = plt.subplots()
    # plt.rc_context({"axes.titlesize": "large", 'legend.fontsize': 'large'})
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(color="gray")
    plt.legend(loc='best')

    if len(gx) > 0:

        g = sympy.lambdify(x, gx, "math")

        for n in t:
            s.append(f(n))

            m.append(g(n))

        ax.plot(t, m, label=f'Función Original = {estiliza_string(gx)}', color='green')

    else:
        for n in t:
            s.append(f(n))

    # ax.plot(t, s, label=f"Polinomio de Lagrange = {estiliza_string(str(sympy.simplify(fx)))}", color='#40E0D0')
    ax.plot(t, s, label="Función Resultante", color='#40E0D0')

    if len(datos) > 1:
        for n in range(len(datos) - 1):
            plt.plot(datos[n][0], datos[n][1], marker='o', markersize=5, color="red")

    plt.plot(datos[-1][0], datos[-1][1], marker='o', markersize=5, color="red", label="Puntos Dados")

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(color="gray")
    plt.legend(loc='best')

    buf = BytesIO()
    fig.savefig(buf, format='jpg', quality=90, dpi=160, facecolor="#f3f2f1", edgecolor='#f3f2f1')
    buf.seek(0)
    uri = 'data:image/png;base64,' + parse.quote(b64encode(buf.read()))

    context = {"ss": estiliza_string(str((fx))),
               "Fun_obj": str(sympy.latex(fx)),
               "result": str(sympy.latex(sympy.simplify(fx))),
               "image": uri}

    return render(request, "lagange_calculado.html", context)
