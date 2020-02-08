from base64 import b64encode
from io import BytesIO
from urllib import parse

import matplotlib.pyplot as plt
import numpy as np
from django.shortcuts import render


# from django.http import HttpResponse


def home_view(request):
    # fig = plt.scatter(x, y, s=area, c=colors, alpha=0.5)

    # Compute areas and colors
    N = 150
    r = 2 * np.random.rand(N)
    theta = 2 * np.pi * np.random.rand(N)
    area = 200 * r ** 2
    colors = theta

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='polar')
    c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

    buf = BytesIO()

    fig.savefig(buf, format='png', bbox_inches='tight')  # dpi = 300
    buf.seek(0)
    string = b64encode(buf.read())
    uri = 'data:image/png;base64,' + parse.quote(string)
    buf.flush()

    args = {'image': uri}

    return render(request, "home.html", args)
