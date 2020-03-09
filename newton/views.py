from base64 import b64encode
from io import BytesIO
from traceback import print_exc
from urllib import parse

import matplotlib.pyplot as plt
import numpy as np
import sympy
from django.shortcuts import render
from sympy.plotting import plot3d

from error.views import errors_view
from .forms import In, E2, E3, E4, In1


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


def newton_view(request):
    form = In1()
    context = {"form": form}

    if request.method == 'GET':
        form = In1(request.GET)

        if form.is_valid():
            return newton_calcula(request, form)

    return render(request, "newton_input.html", context)


def newton_view_multi(request):
    form = In()
    context = {"form": form}

    if request.method == 'POST':

        form = In(request.POST)

        if form.is_valid():
            if form.cleaned_data['n'] == 2:
                return newton_input(request, 2)

            elif form.cleaned_data['n'] == 3:
                return newton_input(request, 3)
            else:
                return newton_input(request, 4)

    return render(request, "newton_elegir.html", context)


def newton_input(request, n):
    if n == 2:
        form = E2()
    elif n == 3:
        form = E3()
    else:
        form = E4()

    context = {"form": form}

    return render(request, "newton_input_multi.html", context)


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

        e = .00001
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

        nuevo = estiliza_string(fucn)

        t = np.arange(r - 25, r + 25, .5)
        s = []

        for n in t:
            s.append(float(fx.subs(x, n)))

        plt.rc_context({'axes.edgecolor': 'black', 'xtick.color': 'black', 'ytick.color': 'black'})
        # plt.style.use("dark_background")
        fig, ax = plt.subplots()

        # plt.axvline(0, color='black')
        ax.axhline(0, color='gray')

        ax.plot(t, s, label=f'f(x) = {nuevo}', color='#40E0D0')
        ax.grid(color="gray")

        if b == 1:  # si se encontro corte antes de 50 iteraciones
            plt.plot(r, fx.subs(x, r), marker='o', markersize=5, color="red", label=f"Corte con Eje x = {r:.4f}")
            ax.set(xlabel='x', ylabel='f(x)', title=f"Raíz calculada después de {iterations} iteraciones")

        else:
            ax.hlines(0, 0, 0, color='r', label='No Se Encontró Corte con Eje X')
            ax.set(xlabel='x', ylabel='f(x)',
                   title=f"No se logro encontrar raíz después de {iteraciones_permitidas} iteraciones")

        plt.legend(loc='best')

        buf = BytesIO()
        fig.savefig(buf, format='jpg', quality=90, dpi=160, facecolor="#f3f2f1", edgecolor='#f3f2f1')
        # # p1._backend.fig.savefig(buf, format='jpg', quality=90, bbox_inches='tight', facecolor="#f3f2f1",
        #                         edgecolor='#f3f2f1', dpi=150)
        buf.seek(0)
        uri = 'data:image/png;base64,' + parse.quote(b64encode(buf.read()))

        context['image'] = uri

        return render(request, "newton_calculado.html", context)


def newton_multi(request):
    x, y, z, w = sympy.symbols('x y z w')

    valores = request.POST
    n = len(valores)

    plt.rcParams.update(plt.rcParamsDefault)
    plt.close('all')

    if n == 5:
        iteraciones = 10

        resul = {'titulos': ['n', 'Vector Solución', 'f₁(x, y), f₂(x, y)'], 'filas': []}
        f1 = sympy.sympify(valores['f1'])
        x0 = float(valores['x0'])

        f2 = sympy.sympify(valores['f2'])
        y0 = float(valores['y0'])

        # derivadas parciales
        f1x = sympy.diff(f1, x)
        f1y = sympy.diff(f1, y)

        f2x = sympy.diff(f2, x)
        f2y = sympy.diff(f2, y)

        # vector de las funciones iniciales
        v = sympy.Matrix([[f1], [f2]])

        # inversa,de la jacobiana
        j_inv = (sympy.Matrix([[f1x, f1y],
                               [f2x, f2y]])) ** -1

        # lamdify de las matrices
        jaco = sympy.lambdify([x, y], j_inv, 'numpy')
        fxfy = sympy.lambdify([x, y], v, 'numpy')

        solucion = np.array([[x0], [y0]])

        for n in range(1, iteraciones + 1):
            # Dandole formato a los valores
            sol = fxfy(solucion[0][0], solucion[1][0])
            xs = f'{solucion[0][0]:.6f}'
            ys = f'{solucion[1][0]:.6f}'
            fxn = f'{float(sol[0]):.6f}'
            fyn = f'{float(sol[1]):.6f}'

            resul['filas'].append([n, xs + ' | ' + ys, fxn + ' | ' + fyn])

            j = jaco(solucion[0][0], solucion[1][0]).dot(fxfy(solucion[0][0], solucion[1][0]))
            solucion = solucion - j

        context = {'context': resul}

        # graficación
        plt.rc_context({'axes.edgecolor': 'w', 'xtick.color': 'w', 'ytick.color': 'w'})
        plt.style.use("dark_background")

        xs = solucion[0][0]  # x solucion
        ys = solucion[1][0]  # y solucion

        titulo = '\n' + estiliza_string(valores['f1']) + ' and ' + estiliza_string(valores['f2']) + '\n'

        p = plot3d(f1, f2, (x, xs - 3, xs + 3), (y, ys - 3, ys + 3), title=titulo, nb_of_points_x=15, nb_of_points_y=15,
                   xlabel='X', ylabel='Y')
        buf = BytesIO()
        p._backend.fig.savefig(buf, format='jpg', quality=90, bbox_inches='tight', facecolor="#000000",
                               edgecolor='#000000', dpi=150, transparent=True)
        buf.seek(0)
        uri = 'data:image/png;base64,' + parse.quote(b64encode(buf.read()))
        context['image'] = uri
        p._backend.close()


    elif n == 7:
        iteraciones = 15

        resul = {'titulos': ['n', 'Vector Solución', 'f₁ | f₂ | f₃'], 'filas': []}
        f1 = sympy.sympify(valores['f1'])
        x0 = float(valores['x0'])

        f2 = sympy.sympify(valores['f2'])
        y0 = float(valores['y0'])

        f3 = sympy.sympify(valores['f3'])
        z0 = float(valores['z0'])

        # derivadas parciales
        f1x = sympy.diff(f1, x)
        f1y = sympy.diff(f1, y)
        f1z = sympy.diff(f1, z)

        f2x = sympy.diff(f2, x)
        f2y = sympy.diff(f2, y)
        f2z = sympy.diff(f2, z)

        f3x = sympy.diff(f3, x)
        f3y = sympy.diff(f3, y)
        f3z = sympy.diff(f3, z)

        # funciones iniciales
        v = sympy.Matrix([[f1], [f2], [f3]])

        # inversa jacobiana

        j_inv = (sympy.Matrix([[f1x, f1y, f1z],
                               [f2x, f2y, f2z],
                               [f3x, f3y, f3z]])) ** -1

        jaco = sympy.lambdify([x, y, z], j_inv, "numpy")
        fxfyfz = sympy.lambdify([x, y, z], v, "numpy")

        solucion = np.array([[x0], [y0], [z0]])

        for n in range(1, iteraciones + 1):

            # Dandole formato a los valores
            sol = fxfyfz(solucion[0][0], solucion[1][0], solucion[2][0])
            xs = f'{solucion[0][0]:.4f}'
            ys = f'{solucion[1][0]:.4f}'
            zs = f'{solucion[2][0]:.4f}'

            fxn = f'{float(sol[0]):.4f}'
            fyn = f'{float(sol[1]):.4f}'
            fzn = f'{float(sol[2]):.4f}'

            resul['filas'].append([n, xs + ' | ' + ys + ' | ' + zs, fxn + ' | ' + fyn + ' | ' + fzn])

            j = jaco(solucion[0][0], solucion[1][0], solucion[2][0]).dot(
                fxfyfz(solucion[0][0], solucion[1][0], solucion[2][0]))
            solucion -= j

            context = {'context': resul}

    return render(request, "newton_calculado_multi.html", context)
