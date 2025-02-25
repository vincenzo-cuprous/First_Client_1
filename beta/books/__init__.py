# books/__init__.py
from .book_views import serve_books_list_page, serve_book_page
from .book_callbacks import register_book_callbacks, register_book_detail_callbacks
from .comments import register_comment_callbacks  # Export if needed
