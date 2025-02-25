# books/book_callbacks.py
from dash.dependencies import Input, Output, State
import requests
from dash import html, dcc
import dash_bootstrap_components as dbc  # Import dbc here
from .book_utils import load_comments_for_book
from .book_components import create_book_card, create_rating_stars

API_BASE_URL = "http://localhost:5000"

def register_book_callbacks(app):
    """Register callbacks related to the books page."""
    @app.callback(
        Output("books-data-store", "data"),
        Input("initial-books-load", "n_intervals")
    )
    def load_books_data(_):
        """Fetches books data from the API."""
        try:
            response = requests.get(f"{API_BASE_URL}/books")
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"Failed to load books: {response.status_code}"}
        except Exception as e:
            return {"error": f"Error fetching books: {str(e)}"}
    
    @app.callback(
        [Output("books-list", "children"),
         Output("books-loading", "children")],
        Input("books-data-store", "data")
    )
    def display_books(data):
        """Renders the books grid from the fetched data."""
        if not data:
            return [], html.Div(className="loading loading-spinner loading-lg")
        
        if "error" in data:
            return html.Div([
                html.P(f"Error: {data['error']}"),
                html.Button("Retry", id="retry-load", className="btn btn-primary mt-4")
            ], className="text-center py-8"), []
            
        books = data
        book_cards = [create_book_card(book) for book in books]
        return book_cards, []
    
    @app.callback(
        Output("books-data-store", "data", allow_duplicate=True),
        Input("retry-load", "n_clicks"),
        prevent_initial_call=True
    )
    def retry_load_books(n_clicks):
        """Retry loading books data."""
        if n_clicks:
            try:
                response = requests.get(f"{API_BASE_URL}/books")
                if response.status_code == 200:
                    return response.json()
                else:
                    return {"error": f"Failed to load books: {response.status_code}"}
            except Exception as e:
                return {"error": f"Error fetching books: {str(e)}"}

def register_book_detail_callbacks(app):
    """Register callbacks related to the book detail page."""
    @app.callback(
        Output("book-details-content", "children"),
        [Input("load-book-details", "n_intervals")],
        [State("book-id-store", "data")]
    )
    def load_book_details(n_intervals, book_id):
        """Fetch and display a specific book's details."""
        if not book_id:
            return html.Div("Book ID not provided", className="text-center py-12")
        
        try:
            response = requests.get(f"{API_BASE_URL}/book/{book_id}")
            if response.status_code != 200:
                return html.Div([
                    html.P(f"Error loading book: {response.status_code}", className="text-center py-12"),
                    dcc.Link(html.Button("Return to Books", className="btn btn-primary"), href="/books")
                ])
            
            book = response.json()
            if not book:
                return html.Div("Book not found", className="text-center py-12")
            
            return html.Div([
                # Back Button
                html.Div([
                    dcc.Link([html.I(className="fas fa-arrow-left mr-2"), "Back to Books"], href="/books", className="btn btn-ghost hover:scale-105 transition-transform"),
                ], className="container mx-auto px-4 py-4"),
                # Book Information
                html.Div([
                    # Book Image
                    html.Div([
                        html.Img(src=book.get("picture_url", "/api/placeholder/400/600"), alt="Book Cover", className="w-full h-auto rounded-lg shadow-lg"),
                    ], className="w-full md:w-1/3 lg:w-1/4 mb-8 md:mb-0"),
                    # Book Details
                    html.Div([
                        html.H2([html.I(className="fas fa-book mr-2"), book.get("book_name", "Book Title")], className="text-4xl font-bold mb-4 flex items-center"),
                        html.P([html.I(className="fas fa-user mr-2"), f"Author: {book.get('author_name', 'Unknown')}"], className="text-xl text-base-content/80 mb-4 flex items-center"),
                        html.P([html.I(className="fas fa-tag mr-2"), f"Category: {book.get('category', 'Uncategorized')}"], className="text-xl text-base-content/80 mb-4 flex items-center"),
                        html.Div([create_rating_stars(book.get("ratings", 0)), html.Span(f"{book.get('ratings', 0)}/5", className="ml-2 text-xl font-bold")], className="flex items-center mb-4"),
                        html.P([html.I(className="fas fa-info-circle mr-2"), f"Description: {book.get('description', 'No description available.')}"], className="text-lg text-base-content/80 mb-8 flex items-start"),
                        html.Div([
                            dbc.Button([html.I(className="fas fa-download mr-2"), "Download"], href=book.get("download_url", "#"), external_link=True, className="btn btn-primary mr-4 hover:scale-105 transition-transform") if book.get("download_url") else html.Div(),
                            html.Button([html.I(className="fas fa-eye mr-2"), "Preview"], className="btn btn-secondary hover:scale-105 transition-transform"),
                        ], className="flex flex-wrap gap-4 mb-8"),
                    ], className="w-full md:w-2/3 lg:w-3/4 md:pl-8"),
                ], className="flex flex-col md:flex-row container mx-auto px=4 py-12"),
                # Comment Section
                html.Div([
                    html.H2("Comments", className="text-3xl font-bold mb=6"),
                    html.Div([
                        html.Textarea(id="comment-input", placeholder="Write your comment here...", className="textarea textarea-bordered w-full mb=4"),
                        html.Button([html.I(className="fas fa-paper-plane mr=2"), "Submit Comment"], id="submit-comment", className="btn btn-primary hover:scale=105 transition-transform"),
                    ], className="mb=8"),
                    html.Div(id="comments-list", className="space=y=4"),
                ], className="container mx=auto px=4 py=12 bg=base=100"),
            ])
        except Exception as e:
            print(f"Error loading book details: {str(e)}")  # Log the error
            return html.Div([
                html.P(f"Error: {str(e)}", className="text-center py=12"),
                dcc.Link(html.Button("Return to Books", className="btn btn-primary"), href="/books")
            ])
