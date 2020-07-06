from flask import Flask, render_template
from wrangling_scripts.wrangling import data_wrangling
from wrangling_scripts.functions.functions import sort_graph_values, make_graph_layout

import plotly.graph_objs as go
import plotly, json

# creating the dataframes

column_names = ['LanguageWorkedWith', 'LanguageDesireNextYear']
df_worked, df_desired = data_wrangling(column_names)

# creating graph_one

sorty_one, sortx_one = sort_graph_values(df_worked, 'Used in 2019')
graph_one, layout_one = make_graph_layout(sortx_one, sorty_one, 'Top 10 Most Used Languages in 2019', 'Percentage', 'Language')

# creating graph two

sorty_two, sortx_two = sort_graph_values(df_desired, 'Desired for 2020')
graph_two, layout_two = make_graph_layout(sortx_two, sorty_two, 'Top 10 Most Desired Languages for 2020', 'Percentage', 'Language')

# appending grahps and layouts

figures = []
figures.append(dict(data=graph_one, layout=layout_one))
figures.append(dict(data=graph_two, layout=layout_two))


ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]
figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

# creating and running the app

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html',
                        ids=ids,
                        figuresJSON=figuresJSON)