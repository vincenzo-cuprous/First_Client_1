# routes.py
from dash.dependencies import Input, Output
from home import serve_home
from about import serve_about
from islamic_content import serve_islamic_content
from contact import serve_contact
from layout import create_navbar
from books import serve_book_page, serve_books_list_page
import re

def register_callbacks(app):
    """
    Register all route-related callbacks for the app.
    
    Args:
        app: The Dash application instance
    """
    
    @app.callback(
        [Output('navbar-container', 'children'),
         Output('page-content', 'children')],
        [Input('url', 'pathname')]
    )
    def update_layout(pathname):
        """Updates the navbar and page content based on the current pathname."""
        # Basic routes
        routes = {
            '/': 'home',
            '/about': 'about',
            '/islamic_content': 'islamic_content',
            '/books': 'books',
            '/contact': 'contact'
        }
        
        # Check for book detail route with ID parameter
        book_detail_match = re.match(r'/books/(\d+)', pathname)
        
        if book_detail_match:
            # Extract book_id from the URL
            book_id = book_detail_match.group(1)
            active_section = 'books'
            page_content = serve_book_page(book_id)
        else:
            # Default routing for other pages
            active_section = routes.get(pathname, 'home')
            
            # Define the page content based on the URL
            page_content = {
                '/': serve_home(),
                '/about': serve_about(),
                '/islamic_content': serve_islamic_content(),
                '/books': serve_books_list_page(),  # Changed to list all books
                '/contact': serve_contact()
            }.get(pathname, '404 Page Not Found')

        # Re-render the navbar with the correct active section
        navbar = create_navbar(active_section=active_section)

        return navbar, page_content
