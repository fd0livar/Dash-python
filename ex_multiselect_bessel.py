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


def update_plot(signals, freq):
    data = []
    for s in signals:
        trace1 = go.Scatter(
            x=xdata,
            y=special.jv(s, freq * xdata),
            mode='lines',
            name='bessel {}'.format(s),
            line=dict(shape='spline')
            )
        data.append(trace1)

    fig = go.Figure(data=data, layout=layout1)
    py.offline.iplot(fig)

signals = wigdets.SelectMultiple(options=list(range(6)), value=(0,), description='Bessel Order')
freq = widgets.FloatSlider(min=1, max=20, value=1, description='Freq')
widgets.interactive(update_plot, signals=signals, freq=freq)
