from django.shortcuts import render

import sympy
import numpy as np
import matplotlib.pyplot as plt

from io import BytesIO
from urllib import parse
from base64 import b64encode

from .forms import In


def newton_view(request):
    form = In()
    context = {"form":form}

    if request.method == 'GET':
        form = In(request.GET)
        if form.is_valid():
            return newton_calcula(request, form)

    return render(request, "newton_input.html", context)

def newton_calcula(request, form):

    valores = form.cleaned_data #funcion y valor inicial
    context = {'form': form}
    starting = valores['ini']

    x, y, z, t = sympy.symbols('x y z t')

    fucn = valores['f']
    fx = sympy.sympify(fucn)

    dfdx = sympy.diff(fx, x)

    e = .001
    x0 = starting
    iterations = 0
    delta = 1
    b = 1

    while e < delta:
        r = x0 - fx.subs(x, x0) / dfdx.subs(x, x0)
        delta = abs((r - x0) / r)
        iterations += 1
        x0 = r
        if iterations > 50:
            b = 0
            break

    print(f'Root {r} calculated after {iterations} iterations {fucn}')

    # ------------------------------------------------------------------

    nuevo = ''
    for c in range(len(fucn)):
        if fucn[c] == '*':
            if fucn[c + 1] == '*':
                c += 2
                nuevo += "^"
        else:
            nuevo += fucn[c]


    t = np.arange(r - 25, r + 25, .5)
    s = []

    for n in t:
        s.append(float(fx.subs(x, n)))

    plt.rc_context({'axes.edgecolor': 'w', 'xtick.color': 'w', 'ytick.color': 'w'})

    fig, ax = plt.subplots()

    # plt.axvline(0, color='black')
    ax.axhline(0, color='black')

    ax.plot(t, s, label=f'f(x) = {nuevo}', color='navy')
    ax.set(title='Método de Newton', xlabel='x', ylabel='f(x)')
    ax.grid(color="azure")

    if b == 1: #si se encontro corte despues de 50 iteraciones
        plt.plot(r, fx.subs(x, r), marker='o', markersize=5, color="red", label=f"Corte con Eje X = {r:.2f}")
    else:
        ax.hlines(0, 0, 0, color='r', label='No Se Encontró Corte con Eje X')

    plt.legend(loc='best')

    buf = BytesIO()
    fig.savefig(buf, format='png', dpi = 150, facecolor= "#004c3f", edgecolor='#004c3f', transparent=True)
    buf.seek(0)
    string = b64encode(buf.read())
    uri = 'data:image/png;base64,' + parse.quote(string)
    buf.flush()

    context['image'] = uri

    return render(request, "newton_calculado.html", context)

