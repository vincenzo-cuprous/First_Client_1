# admin.py
"""Main module for the admin interface."""
from admin_layout import serve_admin
from admin_callbacks import register_callbacks

# Export the necessary functions for app.py to use
__all__ = ['serve_admin', 'register_callbacks']
