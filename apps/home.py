import dash_bootstrap_components as dbc
import dash_html_components as html

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

layout = html.Div([body])

# --- Callbacks --- #
# TODO: add login feature(s)
# TDOD: add data validation
