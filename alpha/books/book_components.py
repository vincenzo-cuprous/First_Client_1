# books/book_components.py
from dash import html, dcc
import dash_bootstrap_components as dbc

def create_book_card(book):
    """Create a card for a book in the grid."""
    return html.Div([
        html.Div([
            html.Img(src=book.get("picture_url", "/api/placeholder/400/600"), alt=book.get("book_name", "Book Cover"), className="h-64 w-full object-cover rounded-t-lg"),
            html.Div([
                html.H3(book.get("book_name", "Book Title"), className="text-xl font-bold mb-2"),
                html.P(f"Author: {book.get('author_name', 'Unknown')}", className="text-sm mb-2"),
                html.P(f"Category: {book.get('category', 'Uncategorized')}", className="text-sm mb-2"),
                create_rating_stars(book.get("ratings", 0)),
                dcc.Link(html.Button([html.I(className="fas fa-info-circle mr-2"), "View Details"], className="btn btn-primary btn-sm w-full mt-4"), href=f"/books/{book.get('book_id', '')}")
            ], className="p-4")
        ], className="bg-base-200 rounded-lg shadow-lg h-full transition-all hover:shadow-xl hover:scale-[1.02]")
    ], className="books-grid-item")

def create_rating_stars(rating):
    """Creates a star rating display using Font Awesome icons."""
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
