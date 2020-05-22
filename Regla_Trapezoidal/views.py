from newton.views import errors_view
from django.shortcuts import render
from .forms import forma
import numpy as np
import sympy

from base64 import b64encode
from io import BytesIO
from traceback import print_exc
from urllib import parse
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def RegTra_views(request):
    form = forma()
    context = {"form": form}

    if request.method == 'GET':
        form = forma(request.GET)

        if form.is_valid():
            return RegTra_Calcula(request, form)

    return render(request, "RegTra_input.html", context)


def RegTra_Calcula(request, form):
    # cierra las graficas hechas anteriormente, libera memoria
    plt.rcParams.update(plt.rcParamsDefault)
    plt.close('all')

    try:
        form.cleaned_data
        I1 = form.cleaned_data['I1']
        I2 = form.cleaned_data['I2']
        funcion = form.cleaned_data['f']

        x, y, z, w, t = sympy.symbols('x y z w t')
        fsym = sympy.sympify(funcion)
        fx = sympy.lambdify(x, fsym, "math")

        rango = int((I2 - I1)) + 1
        h = 1
        x_i = np.arange(I1, I2 + 1, h)
        c_i = np.ones(rango)
        fx_i = []
        c_i[0] = .5
        c_i[-1] = .5

        sum = []
        sigma = 0

        for n in x_i:  # evalua en los puntos
            fx_i.append(fx(n))

        for n in range(0, rango):  # multiplica por intervalos
            sum.append(c_i[n] * fx_i[n])

        for n in sum:
            sigma += n

        titulos = ["\[x_i\]", "\[f(x_i)\]", "\[c_i\]", "\[c_if(x_i)\]", ]
        tabla = []
        for n in range(0, rango):
            tabla.append([f"{x_i[n]:.3f}", f"{fx_i[n]:.3f}", f"{c_i[n]:.3f}", f"{(sum[n]):.3f}"])

        # --------- graficacion ------------

        t = np.linspace(I1, I2)
        s = []

        for n in t:
            s.append(fx(n))

        plt.rc_context({'axes.edgecolor': 'black', 'xtick.color': 'black', 'ytick.color': 'black'})
        fig, ax = plt.subplots()

        ax.plot(t, s, label=f'f(x) = ${sympy.latex(fsym)}$', color='#40E0D0')
        ax.grid(color="gray")
        ax.set_ylim(bottom=0)

        ix = np.linspace(I1, I2)
        iy = fx(ix)
        verts = [(I1, 0), *zip(ix, iy), (I2, 0)]
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
            'I1': I1,
            'I2': I2,
            "sigma": f"{sigma:.3f}",
            "funcion": sympy.latex(fsym),
            "real": f"{sympy.integrate(fsym, (x, I1, I2)):.3f}",
            "tabla": tabla,
            "titulos": titulos
        }

    except Exception as e:
        print(e)
        return errors_view(request)

    return render(request, "RegTra_calculado.html", context)
