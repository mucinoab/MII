from django.shortcuts import render
import sympy
import matplotlib.pyplot as plt
import numpy as np

import io, urllib, base64

def newton_view(request):

    x = sympy.Symbol('x')
    # convert the given function to a symbolic expression

    # starting = float(input("Valor inicial:"))
    # fucn = input("Función:")

    starting = .1
    fucn   = (3 * x ** 2) - 14

    fx = sympy.S(fucn)

    # calculate the differential of the function
    dfdx = sympy.diff(fx, x)

    e = .0001
    x0 = starting
    iterations = 0
    delta = 1
    while e < delta:
        r = x0 - fx.subs(x, x0) / dfdx.subs(x, x0)
        delta = abs((r - x0) / r)
        iterations += 1
        x0 = r

    print(f'Root {r} calculated after {iterations} iterations {fucn}')
#------------------------------------------------------------------

    r = float(r)
    t = np.arange(r-1, r+1, .1)
    s = []
    for n in t:
        s.append(float(fucn.subs(x, n)))



    fig, ax = plt.subplots()

    ax.plot(t, s, label=f'f(x) = {str(fucn)}')
    ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='About as simple as it gets, folks')
    ax.grid()
    ax.vlines(1.82, -10, 10, color = 'r', label = 'Corte con Eje X = '+'%.3f'%(r))

    print(fucn.subs(x, r))
    plt.legend(loc='best')

    ''' 
    fig = plt.scatter(x, y, s=area, c=colors, alpha=0.5)


    # Compute areas and colors
    N = 150
    r = 2 * np.random.rand(N)
    theta = 2 * np.pi * np.random.rand(N)
    area = 200 * r ** 2
    colors = theta  



    fig = plt.figure()
    ax = fig.add_subplot(111, projection='polar')
    c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

    '''

    buf = io.BytesIO()

    #plt.savefig(buf, format='png')

    fig.savefig(buf, format='png')  # dpi = 300
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)
    buf.flush()

    args = {'image': uri}

    return render(request, "newton.html", args)
