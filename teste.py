from flask import Flask, render_template
from wrangling_scripts.wrangling import data_wrangling

import plotly.graph_objs as go
import plotly, json

df_2019 = data_wrangling()



print([x for _,x in sorted(zip(df_2019['Used in 2019'][:10],df_2019.index[:10]))])