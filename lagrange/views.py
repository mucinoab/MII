from .forms import In, datos
from newton.views import estiliza_string
from django.shortcuts import render
from django.forms import formset_factory
from urllib import parse
from base64 import b64encode
from io import BytesIO

import matplotlib.pyplot as plt
import numpy as np
import sympy


def lagrange_view(request):
    form = In()
    context = {"form": form}

    if request.method == 'POST':
        datosf = formset_factory(datos)
        context["datos"] = datosf
        print(request.POST["numero_datos"])
        return render(request, "lagrange_elegir.html", context)

    if request.method == 'GET':
        print("get")
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
    # print(resul)
    return sympy.lambdify(x, resul, "math"), sympy.sympify(resul)


def lagrange_calc(request, datos, gx=""):

    # gx funcion objetivo, la que tratamos de emular.

    x = sympy.symbols('x')

    f, fx = poli_lag(len(datos) - 1, datos)

    t = np.arange(datos[0][0] - 2, datos[-1][0] + 2, .5)
    s = []
    m = []

    fig, ax = plt.subplots()
    plt.rc_context({"axes.titlesize": "large", 'legend.fontsize': 'large'})
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

    ax.plot(t, s, label=f'Polinomio de Lagrange = {estiliza_string(str(sympy.simplify(fx)))}', color='#40E0D0')

    if len(datos) > 1:
        for n in range(len(datos) - 1):
            plt.plot(datos[n][0], datos[n][1], marker='o', markersize=5, color="red")

    plt.plot(datos[-1][0], datos[-1][1], marker='o', markersize=5, color="red", label=f"Puntos dados")

    buf = BytesIO()
    fig.savefig(buf, format='jpg', quality=90, dpi=160, facecolor="#f3f2f1", edgecolor='#f3f2f1')
    buf.seek(0)
    uri = 'data:image/png;base64,' + parse.quote(b64encode(buf.read()))

    context = {"ss": str(fx),
               "Fun_obj": str(sympy.latex(fx)),
               "result": str(sympy.simplify(fx)),
               "image": uri}

    return render(request, "html", context)
