import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
#
# def get_navbar():
#     return dbc.NavbarSimple(
#         children=[
#             dbc.NavItem(dbc.NavLink("Link", href="#")),
#             dbc.DropdownMenu(
#                 nav=True,
#                 in_navbar=True,
#                 label="Menu",
#                 children=[
#                     dbc.DropdownMenuItem(dcc.Link('App 1', href='/apps/app1')),
#                     dbc.DropdownMenuItem(dcc.Link('App 2', href='/apps/app2')),
#                     dbc.DropdownMenuItem(divider=True),
#                     dbc.DropdownMenuItem(dcc.Link('Go Home', href='/apps/home')),
#                 ],
#             ),
#         ],
#         brand="re:Imperio",
#         brand_href="#",
#         color='primary',
#         sticky="top",
#     )


def get_navbar():
    PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

    search_bar = dbc.Row(
        [
            dbc.Col(dbc.Input(type="search", placeholder="Search")),
            dbc.Col(
                dbc.Button("Search", color="primary", className="ml-2"),
                width="auto",
            ),
        ],
        no_gutters=False,
        className="ml-auto flex-nowrap mt-3 mt-md-0",
        align="center",
    )

    return dbc.Navbar(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("Navbar", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="https://plot.ly",
            ),
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.Collapse(search_bar, id="navbar-collapse", navbar=True),
        ],
        color="dark",
        dark=True,
    )
