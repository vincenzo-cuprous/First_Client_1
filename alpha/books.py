from dash import html, dcc, callback_context
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import requests
import json

# API base URL
API_BASE_URL = "http://localhost:5000"

def serve_books_list_page():
    """
    Returns content for the books listing page that fetches books from the API.
    """
    return html.Div([
        # Hero Section
        html.Section(
            html.Div([
                html.Div([
                    html.H1(
                        "Islamic Books",
                        className="text-6xl font-bold mb-6 text-center"
                    ),
                    html.P(
                        "Explore our collection of Islamic books and resources.",
                        className="text-xl text-center text-base-content/80 mb-8"
                    ),
                ], className="max-w-4xl mx-auto px-4"),
            ], className="hero min-h-[30vh] bg-base-200"),
            className="bg-gradient-to-br from-base-100 to-base-200"
        ),
        
        # Books Grid Section with Loading State
        html.Div([
            html.Div(id="books-loading", children=[
                html.Div(className="loading loading-spinner loading-lg mx-auto")
            ], className="py-8 text-center"),
            html.Div(id="books-list", className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 container mx-auto px-4 py-8"),
        ], className="bg-base-100"),
        
        # Store for book data
        dcc.Store(id="books-data-store"),
        
        # Interval for initial load
        dcc.Interval(id="initial-books-load", interval=100, max_intervals=1)
    ])

def register_book_callbacks(app):
    """
    Register callbacks related to the books page.
    This function should be called in your main app.py
    """
    @app.callback(
        Output("books-data-store", "data"),
        Input("initial-books-load", "n_intervals")
    )
    def load_books_data(_):
        """Fetches books data from the API"""
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
        """Renders the books grid from the fetched data"""
        if not data:
            return [], html.Div(className="loading loading-spinner loading-lg")
        
        if "error" in data:
            return html.Div([
                html.P(f"Error: {data['error']}"),
                html.Button("Retry", id="retry-load", className="btn btn-primary mt-4")
            ], className="text-center py-8"), []
            
        books = data
        book_cards = []
        
        for book in books:
            book_cards.append(create_book_card(book))
            
        return book_cards, []
    
    @app.callback(
        Output("books-data-store", "data", allow_duplicate=True),
        Input("retry-load", "n_clicks"),
        prevent_initial_call=True
    )
    def retry_load_books(n_clicks):
        """Retry loading books data"""
        if n_clicks:
            try:
                response = requests.get(f"{API_BASE_URL}/books")
                if response.status_code == 200:
                    return response.json()
                else:
                    return {"error": f"Failed to load books: {response.status_code}"}
            except Exception as e:
                return {"error": f"Error fetching books: {str(e)}"}
    
    @app.callback(
        [Output("comments-list", "children"),
         Output("comment-status", "children")],
        [Input("submit-comment", "n_clicks"),
         Input("load-comments", "n_intervals")],
        [State("comment-input", "value"),
         State("book-id-store", "data")]
    )
    def handle_comments(n_clicks, n_intervals, comment_text, book_id):
        """Handle comment submission and loading"""
        ctx = callback_context
        triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
        
        if triggered_id == "submit-comment" and n_clicks and comment_text and book_id:
            # Submit new comment
            try:
                payload = {
                    "user_id": 1,  # Replace with actual user ID from auth system
                    "user_name": "Anonymous User",  # Replace with actual username
                    "comment": comment_text
                }
                response = requests.post(
                    f"{API_BASE_URL}/book/{book_id}/comment",
                    headers={"Content-Type": "application/json"},
                    data=json.dumps(payload)
                )
                
                if response.status_code == 200:
                    return load_comments_for_book(book_id), html.Div("Comment submitted successfully!", className="alert alert-success")
                else:
                    return load_comments_for_book(book_id), html.Div(f"Error submitting comment: {response.status_code}", className="alert alert-error")
            except Exception as e:
                return load_comments_for_book(book_id), html.Div(f"Error: {str(e)}", className="alert alert-error")
        
        # Just load comments
        if book_id:
            return load_comments_for_book(book_id), html.Div()
        
        return [], html.Div()

def load_comments_for_book(book_id):
    """Fetch and format comments for a book"""
    try:
        response = requests.get(f"{API_BASE_URL}/book/{book_id}/comments")
        if response.status_code == 200:
            comments_data = response.json()
            comment_elements = []
            
            for comment in comments_data:
                comment_el = html.Div([
                    html.P(comment.get("comment", ""), className="text-base-content/80"),
                    html.P(f"By: {comment.get('user_name', 'Anonymous')}", className="text-sm text-base-content/60"),
                    
                    # Display admin reply if it exists
                    html.Div([
                        html.Hr(className="my-2"),
                        html.P([
                            html.Span("Admin: ", className="font-bold"),
                            comment.get("reply_from_admin", "")
                        ], className="text-base-content/80 italic")
                    ]) if comment.get("reply_from_admin") else html.Div()
                ], className="bg-base-200 p-4 rounded-lg")
                
                comment_elements.append(comment_el)
            
            if not comment_elements:
                return [html.P("No comments yet. Be the first to comment!", className="text-center py-4")]
                
            return comment_elements
        else:
            return [html.P(f"Error loading comments: {response.status_code}", className="text-center py-4")]
    except Exception as e:
        return [html.P(f"Error: {str(e)}", className="text-center py-4")]

def create_book_card(book):
    """Create a card for a book in the grid"""
    return html.Div([
        # Book Card
        html.Div([
            # Book Image
            html.Img(
                src=book.get("picture_url", "/api/placeholder/400/600"),
                alt=book.get("book_name", "Book Cover"),
                className="h-64 w-full object-cover rounded-t-lg"
            ),
            
            # Book Info
            html.Div([
                html.H3(book.get("book_name", "Book Title"), className="text-xl font-bold mb-2"),
                html.P(f"Author: {book.get('author_name', 'Unknown')}", className="text-sm mb-2"),
                html.P(f"Category: {book.get('category', 'Uncategorized')}", className="text-sm mb-2"),
                
                # Rating Stars
                create_rating_stars(book.get("ratings", 0)),
                
                # View Details Button
                dcc.Link(
                    html.Button([
                        html.I(className="fas fa-info-circle mr-2"),
                        "View Details"
                    ], className="btn btn-primary btn-sm w-full mt-4"),
                    href=f"/books/{book.get('book_id', '')}"
                )
            ], className="p-4")
        ], className="bg-base-200 rounded-lg shadow-lg h-full transition-all hover:shadow-xl hover:scale-[1.02]")
    ], className="books-grid-item")

def serve_book_page(book_id):
    """
    Returns the content for the book details page using DaisyUI and Font Awesome.
    Now accepts a book_id parameter to fetch specific book details.
    """
    return html.Div([
        # Hero Section
        html.Section(
            html.Div([
                html.Div([
                    html.H1(
                        "Book Details",
                        className="text-6xl font-bold mb-6 text-center"
                    ),
                    html.P(
                        "Explore detailed information about the book, including reviews and download options.",
                        className="text-xl text-center text-base-content/80 mb-8"
                    ),
                ], className="max-w-4xl mx-auto px-4"),
            ], className="hero min-h-[30vh] bg-base-200"),
            className="bg-gradient-to-br from-base-100 to-base-200"
        ),

        # Book Details Section with Loading State
        html.Div(id="book-details-content", className="container mx-auto px-4"),
        
        # Store the book ID for callback use
        dcc.Store(id="book-id-store", data=book_id),
        
        # Interval for initial load
        dcc.Interval(id="load-book-details", interval=100, max_intervals=1),
        
        # Interval for refreshing comments periodically
        dcc.Interval(id="load-comments", interval=30000),  # Refresh comments every 30 seconds
        
        # Comment status message area
        html.Div(id="comment-status", className="container mx-auto px-4 py-2")
    ])

def register_book_detail_callbacks(app):
    """
    Register callbacks related to book detail page.
    This function should be called in your main app.py
    """
    @app.callback(
        Output("book-details-content", "children"),
        [Input("load-book-details", "n_intervals")],
        [State("book-id-store", "data")]
    )
    def load_book_details(n_intervals, book_id):
        """Fetch and display a specific book's details"""
        if not book_id:
            return html.Div("Book ID not provided", className="text-center py-12")
        
        try:
            # Fetch book details from API
            response = requests.get(f"{API_BASE_URL}/book/{book_id}")
            
            if response.status_code != 200:
                return html.Div([
                    html.P(f"Error loading book: {response.status_code}", className="text-center py-12"),
                    dcc.Link(
                        html.Button("Return to Books", className="btn btn-primary"),
                        href="/books"
                    )
                ])
            
            book = response.json()
            
            return html.Div([
                # Back Button
                html.Div([
                    dcc.Link(
                        [html.I(className="fas fa-arrow-left mr-2"), "Back to Books"],
                        href="/books",  # Link back to books listing
                        className="btn btn-ghost hover:scale-105 transition-transform"
                    ),
                ], className="container mx-auto px-4 py-4"),

                # Book Information
                html.Div([
                    # Book Image
                    html.Div([
                        html.Img(
                            src=book.get("picture_url", "/api/placeholder/400/600"),
                            alt="Book Cover",
                            className="w-full h-auto rounded-lg shadow-lg"
                        ),
                    ], className="w-full md:w-1/3 lg:w-1/4 mb-8 md:mb-0"),

                    # Book Details
                    html.Div([
                        # Book Name with Icon
                        html.H2(
                            [html.I(className="fas fa-book mr-2"), book.get("book_name", "Book Title")],
                            className="text-4xl font-bold mb-4 flex items-center"
                        ),
                        # Author Name with Icon
                        html.P(
                            [html.I(className="fas fa-user mr-2"), f"Author: {book.get('author_name', 'Unknown')}"],
                            className="text-xl text-base-content/80 mb-4 flex items-center"
                        ),
                        # Category with Icon
                        html.P(
                            [html.I(className="fas fa-tag mr-2"), f"Category: {book.get('category', 'Uncategorized')}"],
                            className="text-xl text-base-content/80 mb-4 flex items-center"
                        ),
                        # Rating with Icon
                        html.Div([
                            create_rating_stars(book.get("ratings", 0)),
                            html.Span(
                                f"{book.get('ratings', 0)}/5",
                                className="ml-2 text-xl font-bold"
                            )
                        ], className="flex items-center mb-4"),
                        # Description with Icon
                        html.P(
                            [html.I(className="fas fa-info-circle mr-2"), 
                             f"Description: {book.get('description', 'No description available.')}"
                            ],
                            className="text-lg text-base-content/80 mb-8 flex items-start"
                        ),
                        # Buttons for Download and Preview
                        html.Div([
                            dbc.Button(
                                [html.I(className="fas fa-download mr-2"), "Download"],
                                href=book.get("download_url", "#"),
                                external_link=True,
                                className="btn btn-primary mr-4 hover:scale-105 transition-transform"
                            ) if book.get("download_url") else html.Div(),
                            html.Button(
                                [html.I(className="fas fa-eye mr-2"), "Preview"],
                                className="btn btn-secondary hover:scale-105 transition-transform"
                            ),
                        ], className="flex flex-wrap gap-4 mb-8"),
                    ], className="w-full md:w-2/3 lg:w-3/4 md:pl-8"),
                ], className="flex flex-col md:flex-row container mx-auto px-4 py-12"),

                # Comment Section
                html.Div([
                    html.H2(
                        "Comments",
                        className="text-3xl font-bold mb-6"
                    ),
                    # Comment Input Form
                    html.Div([
                        html.Textarea(
                            id="comment-input",
                            placeholder="Write your comment here...",
                            className="textarea textarea-bordered w-full mb-4"
                        ),
                        html.Button(
                            [html.I(className="fas fa-paper-plane mr-2"), "Submit Comment"],
                            id="submit-comment",
                            className="btn btn-primary hover:scale-105 transition-transform"
                        ),
                    ], className="mb-8"),
                    # Display Comments
                    html.Div(id="comments-list", className="space-y-4"),
                ], className="container mx-auto px-4 py-12 bg-base-100"),
            ])
            
        except Exception as e:
            return html.Div([
                html.P(f"Error: {str(e)}", className="text-center py-12"),
                dcc.Link(
                    html.Button("Return to Books", className="btn btn-primary"),
                    href="/books"
                )
            ])

def create_rating_stars(rating):
    """
    Creates a star rating display using Font Awesome icons.
    """
    if not rating:
        rating = 0
    
    try:
        rating = float(rating)
    except (ValueError, TypeError):
        rating = 0
    
    full_stars = int(rating)
    has_half_star = rating % 1 >= 0.5
    empty_stars = 5 - full_stars - (1 if has_half_star else 0)
    
    stars = []
    
    # Add full stars
    for _ in range(full_stars):
        stars.append(html.I(className="fas fa-star text-yellow-400"))
    
    # Add half star if applicable
    if has_half_star:
        stars.append(html.I(className="fas fa-star-half-alt text-yellow-400"))
    
    # Add empty stars
    for _ in range(empty_stars):
        stars.append(html.I(className="far fa-star text-yellow-400"))
    
    return html.Div(stars, className="flex gap-1")
