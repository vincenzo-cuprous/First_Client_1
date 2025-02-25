# app.py
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc  # Import dbc here
from layout import create_footer
from routes import register_callbacks
from books import register_book_callbacks, register_book_detail_callbacks
from settings import PORT, HOST

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Define the layout of the app
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='navbar-container'),
    html.Div(id='page-content'),
    create_footer(),
    dcc.Store(id='theme-store', data='light', storage_type='local')
])

# Register callbacks
register_callbacks(app)
register_book_callbacks(app)
register_book_detail_callbacks(app)

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
