from django.shortcuts import render
import sympy
import matplotlib.pyplot as plt
import numpy as np

from io import BytesIO
from urllib import parse
from base64 import b64encode


def newton_view(request):
    x = sympy.Symbol('x')

    # starting = float(input("Valor inicial:"))
    #fucn = input("Función:")

    starting = .1
    fucn = -6 * x ** 2 + x - 14+120

    fx = sympy.S(fucn)
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
        if iterations > 100:
            b = 0
            break


    print(f'Root {r} calculated after {iterations} iterations {fucn}')
    # ------------------------------------------------------------------

    t = np.arange(r - 20, r + 20, .5)
    s = []

    for n in t:
        s.append(float(fucn.subs(x, n)))

    fig, ax = plt.subplots()
    ax.plot(t, s, label=f'f(x) = {str(fucn)}')
    # ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='About as simple as it gets, folks')
    ax.set(title='Método de Newton')
    ax.grid()
    if b == 1:
        plt.plot(r, fucn.subs(x, r), marker='o', markersize=5, color="red", label= f"Corte con Eje X = {r:.2f}")
    else:
        ax.hlines(0, 0, 0, color='r', label = 'No Ee Encontró Corte con Eje X')

    # ax.hlines(0, -5, 5, color='r')

    plt.legend(loc='best')

    buf = BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight')  # dpi = 300
    buf.seek(0)
    string = b64encode(buf.read())
    uri = 'data:image/png;base64,' + parse.quote(string)
    buf.flush()

    args = {'image': uri}

    return render(request, "newton.html", args)
