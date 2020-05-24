from newton.views import errors_view
from django.shortcuts import render
from .forms import forma

import numpy as np
import sympy

from operator import itemgetter

from base64 import b64encode
from io import BytesIO
from urllib import parse
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import matplotlib.lines as mlines


def Sim13_views(request):
    form = forma()
    context = {"form": form}

    if request.method == 'GET':
        form = forma(request.GET)

        if form.is_valid():
            return Sim13_Calcula(request, form)

    return render(request, "Sim13_input.html", context)

def Sim13_Calcula(request, form):
    plt.rcParams.update(plt.rcParamsDefault)
    plt.close('all')
    try:
        a = form.cleaned_data['a']
        b = form.cleaned_data['b']
        funcion = form.cleaned_data['f']
        n = form.cleaned_data['n']

        x = sympy.symbols('x')
        fsym = sympy.sympify(funcion)
        f = sympy.lambdify(x, fsym, "math")
        real = sympy.integrate(fsym, (x, a, b))

        tabla = []
        k = 0.0
        h = (b-a)/n
        x = a + h

        aux = f(a)
        tabla.append([a, f"{aux:.3f}", 1, f"{(aux):.3f}"])

        for i in range(1, int(n/2) + 1):
            aux = f(x)
            tabla.append([x, f"{aux:.3f}", 4, f"{(aux*4):.3f}"])
            k += 4*aux
            x += 2*h

        x = a + 2*h

        for i in range(1, int(n/2)):
            aux = f(x)
            tabla.append([x, f"{aux:.3f}", 2, f"{(aux*2):.3f}"])
            k += 2*aux
            x += 2*h

        aux = f(b)
        tabla.append([b, f"{aux:.3f}", 1, f"{(aux):.3f}"])

        tabla.sort(key=itemgetter(0))

        for n in tabla:
            n[0] = f"{(n[0]):.3f}"

        sigma = (h/3)*(f(a)+aux+k)

        titulos = ["\(x_i\)", "\(f(x_i)\)", "\(c_i\)", "\(c_if(x_i)\)"]

        # --------- graficacion ------------

        fig, ax = plt.subplots()
        t = np.linspace(a, b)
        s = []

        for n in t:
            s.append(f(n))

        plt.rc_context({'axes.edgecolor': 'black', 'xtick.color': 'black', 'ytick.color': 'black'})
        ax.plot(t, s, label=f'f(x) = ${sympy.latex(fsym)}$', color='#40E0D0')
        ax.grid(color="gray")
        ax.set_ylim(bottom=0)

        ix = np.linspace(a, b)
        iy = f(ix)
        verts = [(a, 0), *zip(ix, iy), (b, 0)]
        poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
        ax.add_patch(poly)

        ax.xaxis.set_ticks_position('bottom')
        plt.legend(loc='best')

        buf = BytesIO()
        fig.savefig(buf, format='jpg', quality=90, dpi=160, facecolor="#f3f2f1", edgecolor='#f3f2f1')
        buf.seek(0)
        uri = 'data:image/png;base64,' + parse.quote(b64encode(buf.read()))

        context = {
            'image': uri,
            'I1': a,
            'I2': b,
            "sigma": f"{sigma:.3f}",
            "funcion": sympy.latex(fsym),
            "real": f"{real:.3f}",
            "tabla": tabla,
            "titulos": titulos,
            "error": f"{abs(real - sigma):.3f}"
        }

    except Exception as e:
        print(e)
        return errors_view(request)

    return render(request, "Sim13_calculado.html", context)
