# Build-a-visualization-dashboard-with-dash
![alt text](https://github.com/zalihat/Build-a-visualization-dashboard-with-dash/blob/master/cover.jpg?raw=true)

Have you ever created some awesome visualizations with Jupyter notebook and you wish you could build an app for it. Well, worry no more as you can do this and more with dash.

[Dash](https://dash.plotly.com/)  is a productive Python framework for building web analytic applications.

Written on top of Flask, Plotly.js, and React.js, Dash is ideal for building data visualization apps with highly custom user interfaces in pure Python. It's particularly suited for anyone who works with data in Python.

Through a couple of simple patterns, Dash abstracts away all of the technologies and protocols that are required to build an interactive web-based application. Dash is simple enough that you can bind a user interface around your Python code in an afternoon.

Dash apps are rendered in the web browser. You can deploy your apps to servers and then share them through URLs. Since Dash apps are viewed in the web browser, Dash is inherently cross-platform and mobile ready.
## **How do I get started?**
You can install dash using 'pip' just like every other python library. Dash currently supports python 2 and python 3. To install the latest version of dash run
pip install dash==1.19.0
For this article I will be using the simple app layout from the dash [tutorial](https://dash.plotly.com/layout). To get started create a file and name it app.py
Dataset
The dataset that I will be using for this tutorial is a time series data for daily minimum temperatures. Download the dataset using this [link](https://www.kaggle.com/shenba/time-series-datasets?select=daily-minimum-temperatures-in-me.csv)
### **Import all necessary libraries**
```import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
```
### **Load the dataset using pandas**
```path = 'daily-minimum-temperatures-in-me.csv'
df = pd.read_csv(path, infer_datetime_format=True, parse_dates=['Date'], index_col='Date')
```

## **Create visualization using plotly express**
Dash was made by Plotly's creators as a way to easily implement a web interface and create dashboards with Plotly without having to learn javascript, html and other web technologies. With Dash you don't make visualizations, you build an interface to display Plotly's visualizations.
To read more about creating visuals with plotly express checkout this [link](https://plotly.com/python/plotly-express/)
```
fig =  px.area(df, x = df.index, y = 'Daily minimum temperatures', color = df.index.year)
```

Copy and paste the code below into the app.py file
Note: Change the path variable to the path to your dataset.
```
# -*- coding: utf-8 -*-
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
fig = px.area(df, x = df.index, y = 'Daily minimum temperatures', color = df.index.year)
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
```

Then run this on your terminal
```python app.py
```

and visit http://127.0.0.1:8050/ in your web browser. You should see an app that looks like this.
![alt text](https://github.com/zalihat/Build-a-visualization-dashboard-with-dash/blob/master/cover.jpg?raw=true)
The drop down feature will be implemented in my next article " Dash callbacks".

Here is the link to the article on medium https://zalihatoyarazi.medium.com/build-a-visualization-dashboard-with-dash-ed154d85c196