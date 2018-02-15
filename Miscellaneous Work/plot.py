import plotly.plotly as py
import plotly.graph_objs as go

Quarter = ['2016Q1', '2016Q2', '2016Q3', '2016Q4']
BatsY = [84.51338303, 71.59582228, 57.76053362, 51.34425478]
BatsZ = [102.28369, 89.46587409, 83.78831136, 82.63636173]
Arca  =  [100.3674987, 90.20344116, 98.88106929, 103.0167841]
Nasdaq = [60.46445937, 55.58930882, 54.40818976, 51.10898963]
CHX = [1912.293435, 113.3580182, 3940.969007, 2038.233254]
EdgeA = [130.3762074, 3167.686572, 84.43120548, 79.91376836]
EdgeX = [69.40928052, 60.03921337, 52.45261368, 48.77767106]
Amex  =  [37.72417409, 35.72124268, 42.88003108, 44.1530655]
Boston = [137.2185188, 90.08089943, 75.85279399, 68.87423699]
NYSE   = [48.36375383, 40.37699342, 37.01241896, 37.68597664]
NSX = [2468.867964, 1062.216486, 504.4639954, 190.5419538]
Phlx  =  [327.5186694, 240.8287311, 236.187382,  240.2995586]

# Create and style traces
trace0 = go.Scatter(
    x = Quarter,
    y = BatsY,
    name = 'Bats-Y',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4,)
)
trace1 = go.Scatter(
    x = Quarter,
    y = BatsZ,
    name = 'Bats-Z',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,)
)
trace2 = go.Scatter(
    x = Quarter,
    y = Arca,
    name = 'Arca',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,)
)
trace3 = go.Scatter(
    x = Quarter,
    y = Nasdaq,
    name = 'Nasdaq',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,)
)
trace4 = go.Scatter(
    x = Quarter,
    y = CHX,
    name = 'CHX',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,)
)
trace5 = go.Scatter(
    x = Quarter,
    y = EdgeA,
    name = 'Edge-A',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,)
)
trace6 = go.Scatter(
    x = Quarter,
    y = EdgeX,
    name = 'Edge-X',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,)
)
trace7 = go.Scatter(
    x = Quarter,
    y = Amex,
    name = 'Amex',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,)
)
trace8 = go.Scatter(
    x = Quarter,
    y = Boston,
    name = 'Boston',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,)
)
trace9 = go.Scatter(
    x = Quarter,
    y = NYSE,
    name = 'NYSE',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,)
)
trace10 = go.Scatter(
    x = Quarter,
    y = NSX,
    name = 'NSX',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,)
)
trace11 = go.Scatter(
    x = Quarter,
    y = Phlx,
    name = 'Phlx',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,)
)
data = [trace0, trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10, trace11]

# Edit the layout
layout = dict(title = 'TOR',
              xaxis = dict(title = 'Quarter'),
              yaxis = dict(title = 'TOR'),
              )

fig = dict(data=data, layout=layout)
py.iplot(fig, filename='styled-line')