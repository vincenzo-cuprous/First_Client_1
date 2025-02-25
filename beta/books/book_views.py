# books/book_views.py
from dash import html, dcc
import dash_bootstrap_components as dbc
from .book_components import create_book_card, create_rating_stars

def serve_books_list_page():
    """Returns content for the books listing page."""
    return html.Div([
        # Hero Section
        html.Section(
            html.Div([
                html.Div([
                    html.H1("Islamic Books", className="text-6xl font-bold mb-6 text-center"),
                    html.P("Explore our collection of Islamic books and resources.", className="text-xl text-center text-base-content/80 mb-8"),
                ], className="max-w-4xl mx-auto px-4"),
            ], className="hero min-h-[30vh] bg-base-200"),
            className="bg-gradient-to-br from-base-100 to-base-200"
        ),
        # Books Grid Section
        html.Div([
            html.Div(id="books-loading", children=[
                html.Div(className="loading loading-spinner loading-lg mx-auto")
            ], className="py-8 text-center"),
            html.Div(id="books-list", className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap=6 container mx-auto px=4 py=8"),
        ], className="bg-base-100"),
        # Store for book data
        dcc.Store(id="books-data-store"),
        # Interval for initial load
        dcc.Interval(id="initial-books-load", interval=100, max_intervals=1)
    ])

def serve_book_page(book_id):
    """Returns content for the book details page."""
    return html.Div([
        # Hero Section
        html.Section(
            html.Div([
                html.Div([
                    html.H1("Book Details", className="text-6xl font-bold mb-6 text-center"),
                    html.P("Explore detailed information about the book.", className="text-xl text-center text-base-content/80 mb-8"),
                ], className="max-w-4xl mx-auto px-4"),
            ], className="hero min-h-[30vh] bg-base-200"),
            className="bg-gradient-to-br from-base-100 to-base-200"
        ),
        # Book Details Section
        html.Div(id="book-details-content", className="container mx-auto px-4"),
        # Store the book ID for callback use
        dcc.Store(id="book-id-store", data=book_id),
        # Interval for initial load
        dcc.Interval(id="load-book-details", interval=100, max_intervals=1),
    ])
