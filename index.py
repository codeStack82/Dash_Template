import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import app
from apps import app1, app2, home

from components import navigation_bar as nav

navbar = nav.get_navbar()

app.layout = html.Div([
    navbar,
    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content')
])


# Index.py Callbacks ----------------------------------------------------------
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/app1':
        return app1.layout
    elif pathname == '/apps/app2':
        return app2.layout
    else:
        return home.layout


# Home.py Callbacks  ----------------------------------------------------------
@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


# App1.py Callbacks -----------------------------------------------------------

# App2.py Callbacks -----------------------------------------------------------

if __name__ == '__main__':
    app.run_server(debug=True)
