import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc, html

data = pd.read_csv("gapminder.csv")
app = dash.Dash()
server=app.server


app.layout = html.Div([
    # Header - centered
    html.Div([
        html.H1("My First Dashboard", style={
            'color': 'red',
            'text-align': 'center',
            'margin': '0'
        })
    ], style={
        'border': '1px solid black',
        'padding': '15px',
        'background-color': '#f0f0f0'
    }),

    # Graphs - flexbox layout
    html.Div([
        html.Div([
            dcc.Graph(id='scatter-plot',
                      figure={'data': [go.Scatter(x=data['pop'], y=data['gdpPercap'], mode='markers')],
                              'layout': go.Layout(title='Scatter Plot')})
        ], style={'width': '50%', 'border': '1px solid black'}),

        html.Div([
            dcc.Graph(id='box-plot',
                      figure={'data': [go.Box(x=data['gdpPercap'])],
                              'layout': go.Layout(title='Box Plot')})
        ], style={'width': '50%', 'border': '1px solid black'})
    ], style={'display': 'flex'})
])

if __name__ == '__main__':
    app.run(debug=True)