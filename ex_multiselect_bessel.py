#!/usr/bin/env python3

import numpy as np
import plotly as py
import plotly.graph_objs as go
import ipywidgets as wigdets
from scipy import special

#py.offline.init_notebook_mode(connected=True)

xdata = np.linspace(0, 2*np.pi, 1000)

layout1 = go.Layout(
    title='Simple Example',
    yaxis=dict(title='volts'),
    xaxis=dict(title='time (ns)')
)

trace1 = go.Scatter(
    x=xdata,
    y=np.sin(xdata),
    mode='lines',
    name='sin(x)',
    line=dict(shape='spline')
)

fig = go.Figure(data=[trace1], layout=layout1)
py.offline.iplot(fig)
