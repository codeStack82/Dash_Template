import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_html_components as html

# navbar section
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Link", href="#")),
        dbc.DropdownMenu(
            nav=True,
            in_navbar=True,
            label="Menu",
            children=[
                dbc.DropdownMenuItem(dcc.Link('App 1', href='/apps/app1')),
                dbc.DropdownMenuItem(dcc.Link('App 2', href='/apps/app2')),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem(dcc.Link('Go Home', href='#')),
            ],
        ),
    ],
    brand="Ops-View Home",
    brand_href="#",
    # color='primary',
    sticky="top",
)

# Form - email and password
email_input = dbc.FormGroup([
        dbc.Label("Email", html_for="example-email-row", width=2),
        dbc.Col(
            dbc.Input(
                type="email", id="example-email-row", placeholder="Enter email"
            ),
            width=8,
        ),
    ],row=True,)

password_input = dbc.FormGroup([
        dbc.Label("Password", html_for="example-password-row", width=2),
        dbc.Col(
            dbc.Input(
                type="password",
                id="example-password-row",
                placeholder="Enter password",
            ),
            width=8,
        ),
    ],row=True,)

form = dbc.Form([email_input, password_input])


body = dbc.Container(
    [

        # Login section
        dbc.Row(
            dbc.Col([
                html.P(),
            ])
        ),

        # Login section
        dbc.Row([
                dbc.Col([
                    form,
            ], md=10, ),
        ])
    ],
    className="mt-10",
)

layout = html.Div([navbar, body])

# --- Callbacks --- #
# TODO: add login feature(s)
# TDOD: add data validation
