from base64 import b64encode
from io import BytesIO
from urllib import parse

import matplotlib.pyplot as plt
import numpy as np
from django.shortcuts import render

# from django.http import HttpResponse
from django.views.decorators.gzip import gzip_page

@gzip_page
def home_view(request):
    plt.rcParams.update(plt.rcParamsDefault)
    plt.close('all')

    N = 80
    r = 2 * np.random.rand(N)
    theta = 4 * np.pi * np.random.rand(N)
    area = np.random.randint(50, 100) * r ** 4
    colors = theta

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='polar')
    ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.50)

    buf = BytesIO()

    fig.savefig(buf, format='png', bbox_inches='tight', transparent=True, dpi=200)  # dpi = 300
    buf.seek(0)
    string = b64encode(buf.read())
    uri = 'data:image/png;base64,' + parse.quote(string)

    args = {'image': uri}

    return render(request, "home.html", args)
