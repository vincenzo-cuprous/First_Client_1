# books_2.py (Second Half)
from dash import html, dcc, callback_context
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import requests
import json

# API base URL
API_BASE_URL = "http://localhost:5000"

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
                return [html.P("No comments yet. Be the first to comment!", className")]
