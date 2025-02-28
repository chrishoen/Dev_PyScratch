import pandas as pd
import plotly.express as px

filename = '20250228-061246.SAMPLES'
filename = '20250228-062234.SAMPLES'
filename = '20250228-062818.SAMPLES'
filename = '20250228-064204.SAMPLES'
filename = '20250228-064841.SAMPLES'
filename = '20250228-065251.SAMPLES'

df = pd.read_csv(filename, header=None, usecols=[2], names=['values'])

fig = px.line(df, y='values', title=filename)
fig.show()
