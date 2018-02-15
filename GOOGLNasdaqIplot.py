import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

df = pd.read_csv("~/GOOGLNasdaq2.csv")

data = [go.Scatter(
          x=df.Date,
          y=df['TradeVol'])]

py.iplot(data)