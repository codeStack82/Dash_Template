import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

# Form - email and password
email_input = dbc.FormGroup([
    dbc.Label("Email", html_for="example-email-row", width=2),
    dbc.Col(
        dbc.Input(
            type="email", id="example-email-row", placeholder="Enter email"
        ),
        width=8,
    ),
], row=True, )

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
], row=True, )

submit = dbc.Button("  Login  ", color="primary")

#test code
modal = html.Div(
    [
        dbc.Button("Open modal", id="open"),
        dbc.Modal(
            [
                dbc.ModalHeader("Header"),
                dbc.ModalBody("This is the content of the modal"),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close", className="ml-auto")
                ),
            ],
            id="modal",
        ),
    ]
)


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
            ], md=8, ),
        ]),

        # Submit Login section
        dbc.Row([
            dbc.Col([
                submit, modal,
            ], md=10),
        ])

    ],
    className="mt-8",
)

layout = html.Div([body])

# --- Callbacks --- #
# TODO: Finish test & implementing the modal function with callback in the index.py

# TODO: add data validation

