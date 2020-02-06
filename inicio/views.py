from django.shortcuts import render
from django.http import HttpResponse

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import io
import urllib, base64
  
def home_view(request):   
  # Data for plotting
  t = np.arange(0.0, 2.0, 0.01)
  s = 1 + np.sin(2 * np.pi * t)

  fig, ax = plt.subplots()
  ax.plot(t, s)

  ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='About as simple as it gets, folks')
  ax.grid()

  buf = io.BytesIO()
  fig.savefig(buf, format='png')
  buf.seek(0)
  string = base64.b64encode(buf.read())
  
  uri = 'data:image/png;base64,' + urllib.parse.quote(string)
  
  args = {'image':uri}

  return render(request, "home.html", args)