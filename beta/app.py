# app.py
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from home import serve_home
from about import serve_about
from islamic_content import serve_islamic_content
from contact import serve_contact
from layout import create_navbar, create_footer
from settings import PORT, HOST

# Initialize the Dash app with suppress_callback_exceptions=True
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Define the layout of the app
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    # Navbar will be rendered once here
    html.Div(id='navbar-container'),  # Use a container for the navbar
    # Content div for pages
    html.Div(id='page-content'),
    # Footer will be rendered once here
    create_footer(),
    # Theme store
    dcc.Store(id='theme-store', data='light')
])

# Callback to update the navbar and page content based on the URL
@app.callback(
    [Output('navbar-container', 'children'),
     Output('page-content', 'children')],
    [Input('url', 'pathname')]
)
def update_layout(pathname):
    """Updates the navbar and page content based on the current pathname."""
    routes = {
        '/': 'home',
        '/about': 'about',
        '/islamic_content': 'islamic_content',
        '/contact': 'contact'
    }
    active_section = routes.get(pathname, 'home')

    # Define the page content based on the URL
    page_content = {
        '/': serve_home(),
        '/about': serve_about(),
        '/islamic_content': serve_islamic_content(),
        '/contact': serve_contact()
    }.get(pathname, '404 Page Not Found')

    # Re-render the navbar with the correct active section
    navbar = create_navbar(active_section=active_section)

    return navbar, page_content

# Callback to handle theme toggling
@app.callback(
    Output('theme-store', 'data'),
    [Input('theme-toggle', 'n_clicks')],
    [State('theme-store', 'data')]
)
def toggle_theme(n_clicks, current_theme):
    """Toggles the theme between light and dark."""
    if n_clicks is None:
        return current_theme
    return 'dark' if current_theme == 'light' else 'light'

# Run the app
if __name__ == '__main__':
    app.run_server(host=HOST, port=PORT, debug=True)
