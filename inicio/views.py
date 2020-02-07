from django.shortcuts import render
# from django.http import HttpResponse

import matplotlib.pyplot as plt
import numpy as np

import io, urllib, base64
#from random import randint

def home_view(request):
   # plt.rcParams['axes.facecolor'] = '#004c3f'

    t = np.arange(-6.0, 6.0, .5)
    s = 3*t**2-10
    fig, ax = plt.subplots()


    ax.plot(t, s, label='f(x)')
    ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='About as simple as it gets, folks')
    ax.grid()
    ax.vlines(1.82, -10, 10, color = 'r', label = 'Corte con eje x')


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

    return render(request, "home.html", args)
