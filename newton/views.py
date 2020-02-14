from base64 import b64encode
from io import BytesIO
from traceback import print_exc
from urllib import parse

import matplotlib.pyplot as plt
import numpy as np
import sympy
from django.shortcuts import render

from error.views import errors_view
from .forms import In


def newton_view(request):
    form = In()
    context = {"form": form}

    if request.method == 'GET':
        form = In(request.GET)
        if form.is_valid():
            return newton_calcula(request, form)

    return render(request, "newton_input.html", context)


def newton_calcula(request, form):

    plt.rcParams.update(plt.rcParamsDefault)
    plt.close('all')

    try:
        valores = form.cleaned_data  # funcion y valor inicial
        context = {'form': form}
        starting = valores['ini']
        fucn = valores['f']

        x, y, z, t = sympy.symbols('x y z t')
        fx = sympy.sympify(fucn)

        dfdx = sympy.diff(fx, x)

        e = .001
        x0 = starting
        iterations = 0
        delta = 1
        b = 1
        iteraciones_permitidas = 60

        while e < delta:
            r = x0 - fx.subs(x, x0) / dfdx.subs(x, x0)
            delta = abs((r - x0) / r)
            iterations += 1
            x0 = r
            if iterations > iteraciones_permitidas:
                b = 0
                break

    except Exception:
        print_exc()
        return errors_view(request)

    else:
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
        plt.style.use("dark_background")
        fig, ax = plt.subplots()

        # plt.axvline(0, color='black')
        ax.axhline(0, color='black')

        ax.plot(t, s, label=f'f(x) = {nuevo}', color='navy')
        ax.grid(color="azure")

        if b == 1:  # si se encontro corte antes de 50 iteraciones
            plt.plot(r, fx.subs(x, r), marker='o', markersize=5, color="red", label=f"Corte con Eje x = {r:.2f}")
            ax.set(xlabel='x', ylabel='f(x)', title=f"Raíz calculada después de {iterations} iteraciones")
        else:
            ax.hlines(0, 0, 0, color='r', label='No Se Encontró Corte con Eje X')
            ax.set(xlabel='x', ylabel='f(x)',
                   title=f"No se logro encontrar raíz después de {iteraciones_permitidas} iteraciones")

        plt.legend(loc='best')

        buf = BytesIO()
        fig.savefig(buf, format='png', dpi=160, facecolor="#004c3f", edgecolor='#004c3f', transparent=True)
        buf.seek(0)
        # string = b64encode(buf.read())
        uri = 'data:image/png;base64,' + parse.quote(b64encode(buf.read()))

        context['image'] = uri

        return render(request, "newton_calculado.html", context)
