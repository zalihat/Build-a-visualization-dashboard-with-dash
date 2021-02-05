# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
path = 'daily-minimum-temperatures-in-me.csv'
df = pd.read_csv(path, infer_datetime_format=True, parse_dates=['Date'], index_col='Date')


fig =  px.area(df, x = df.index, y = 'Daily minimum temperatures', color = df.index.year)
fig.update_xaxes(
    # rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            
            dict(count=1, label="1M", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1Y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)

app.layout = html.Div(children=[
    html.H1(children='Build a visualization dashboard with DASH'),

    html.Div(children='''
        Year
    '''),
    dcc.Dropdown(
            id='my_dropdown',
            options=[
                     {'label': '1981', 'value': ''},
                     {'label': '1982', 'value': ''},
                     {'label': '1983', 'value': ''},
                     {'label': '1984', 'value': ''},
                     {'label': '1985', 'value': ''},
                     {'label': '1986', 'value': ''},
                     {'label': '1987', 'value': ''},
                     {'label': '1988', 'value': ''},
                     {'label': '1989', 'value': ''},
                     {'label': '1990', 'value': '1990'}
            ],
            value='1990',
            multi=False,
            clearable=False,
            style={"width": "50%"}
        ),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)