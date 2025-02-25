# admin_layout.py
"""Layout construction for the admin interface."""
from dash import html
import dash_bootstrap_components as dbc

from admin_components import (
    create_admin_header, create_book_form, 
    create_books_table, create_delete_modal
)
from admin_data import load_books_data

def serve_admin():
    """
    Returns the admin page content for managing books with CRUD operations.
    """
    # Load books data
    books_df = load_books_data()
    
    return html.Div([
        # Admin Header
        create_admin_header(),
        
        # Book Management Section
        html.Section(
            dbc.Container([
                dbc.Row([
                    # Left Column - Add/Edit Book Form
                    dbc.Col([
                        create_book_form()
                    ], md=5),
                    
                    # Right Column - Books List/Table
                    dbc.Col([
                        create_books_table(books_df.to_dict('records'))
                    ], md=7)
                ], className="py-5 gap-4")
            ], fluid=True),
            className="bg-base-100 min-h-screen"
        ),
        
        # Confirmation Modal for Delete
        create_delete_modal(),
    ])
