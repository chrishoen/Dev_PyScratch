import pandas as pd
import plotly.express as px

filename = '20250226-191429.SAMPLES'
filename = '20250226-192210.SAMPLES'
filename = '20250227-200045.SAMPLES'
filename = '20250227-201845.SAMPLES'

filename = '20250227-201845.SAMPLES'

df = pd.read_csv(filename, header=None, usecols=[2], names=['values'])

fig = px.line(df, y='values', title='samples')
fig.show()
