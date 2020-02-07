from django.shortcuts import render
# from django.http import HttpResponse

import matplotlib.pyplot as plt
import numpy as np

import io, urllib, base64
from random import randint

def home_view(request):

    '''
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(randint(1, 50) * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='About as simple as it gets, folks')
    ax.grid()

    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    area = np.pi * (15 * np.random.rand(N)) ** 2  # 0 to 15 point radii

    fig = plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    '''

    # Compute areas and colors
    N = 150
    r = 2 * np.random.rand(N)
    theta = 2 * np.pi * np.random.rand(N)
    area = 200 * r ** 2
    colors = theta

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='polar')
    c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)


    buf = io.BytesIO()

    #plt.savefig(buf, format='png')

    fig.savefig(buf, format='png', bbox_inches = 'tight')  # dpi = 300
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)
    buf.flush()

    args = {'image': uri}

    return render(request, "home.html", args)
