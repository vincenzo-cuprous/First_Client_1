# admin_callbacks.py
"""Callbacks for the admin interface."""
from dash import callback, Input, Output, State, html
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import dash

from admin_data import (
    load_books_data, add_book, update_book, 
    delete_book, filter_books
)

# Global variable to store the books DataFrame
books_df = load_books_data()

def register_callbacks(app):
    """Register all callbacks for the admin page functionality."""
    
    @app.callback(
        [Output('edit-book-button', 'disabled'),
         Output('delete-book-button', 'disabled')],
        [Input('books-table', 'selected_rows')]
    )
    def update_buttons_state(selected_rows):
        """Enable/disable edit and delete buttons based on selection."""
        disabled = len(selected_rows) == 0
        return disabled, disabled
    
    @app.callback(
        [Output('editing-book-id', 'data'),
         Output('book-name', 'value'),
         Output('author-name', 'value'),
         Output('book-category', 'value'),
         Output('book-rating', 'value'),
         Output('book-description', 'value'),
         Output('book-image', 'value'),
         Output('book-download', 'value'),
         Output('add-book-button', 'className'),
         Output('update-book-button', 'className'),
         Output('cancel-edit-button', 'className'),
         Output('image-preview', 'children')],
        [Input('edit-book-button', 'n_clicks'),
         Input('cancel-edit-button', 'n_clicks')],
        [State('books-table', 'selected_rows'),
         State('books-table', 'data')]
    )
    def handle_edit_book(edit_clicks, cancel_clicks, selected_rows, table_data):
        """Handle editing of a book."""
        ctx = dash.callback_context
        
        # Default output for all fields
        default_output = [
            None, "", "", None, None, "", "", "",
            "w-100 mb-2", "w-100 mb-2 d-none", "w-100 mb-2 d-none", None
        ]
        
        # If the callback was not triggered or cancel was clicked
        if not ctx.triggered or ctx.triggered[0]['prop_id'] == 'cancel-edit-button.n_clicks':
            return default_output
        
        # If edit button was clicked and a row is selected
        if ctx.triggered[0]['prop_id'] == 'edit-book-button.n_clicks' and selected_rows:
            book = table_data[selected_rows[0]]
            
            # Prepare image preview if image URL exists
            image_preview = None
            if book.get('image_url'):
                image_preview = html.Img(
                    src=book['image_url'],
                    style={'maxHeight': '100px', 'maxWidth': '100%'}
                )
            
            return [
                book.get('id', ''),
                book.get('name', ''),
                book.get('author', ''),
                book.get('category', ''),
                book.get('ratings', ''),
                book.get('description', ''),
                book.get('image_url', ''),
                book.get('download_url', ''),
                "w-100 mb-2 d-none",  # Add button hidden
                "w-100 mb-2",  # Update button visible
                "w-100 mb-2",  # Cancel button visible
                image_preview
            ]
        
        # Default
        return default_output
    
    @app.callback(
        Output('image-preview', 'children', allow_duplicate=True),
        [Input('upload-image', 'contents')],
        prevent_initial_call=True
    )
    def update_image_preview(contents):
        """Update image preview when an image is uploaded."""
        if contents is None:
            return None
        
        # Display the uploaded image
        return html.Img(
            src=contents,
            style={'maxHeight': '100px', 'maxWidth': '100%'}
        )
    
    @app.callback(
        [Output('books-table', 'data'),
         Output('form-feedback', 'children'),
         Output('book-name', 'value', allow_duplicate=True),
         Output('author-name', 'value', allow_duplicate=True),
         Output('book-category', 'value', allow_duplicate=True),
         Output('book-rating', 'value', allow_duplicate=True),
         Output('book-description', 'value', allow_duplicate=True),
         Output('book-image', 'value', allow_duplicate=True),
         Output('book-download', 'value', allow_duplicate=True),
         Output('editing-book-id', 'data', allow_duplicate=True),
         Output('add-book-button', 'className', allow_duplicate=True),
         Output('update-book-button', 'className', allow_duplicate=True),
         Output('cancel-edit-button', 'className', allow_duplicate=True),
         Output('image-preview', 'children', allow_duplicate=True)],
        [Input('add-book-button', 'n_clicks'), 
         Input('update-book-button', 'n_clicks')],
        [State('book-name', 'value'),
         State('author-name', 'value'),
         State('book-category', 'value'),
         State('book-rating', 'value'),
         State('book-description', 'value'),
         State('book-image', 'value'),
         State('book-download', 'value'),
         State('upload-image', 'contents'),
         State('editing-book-id', 'data'),
         State('books-table', 'data')],
        prevent_initial_call=True
    )
    def handle_book_submission(add_clicks, update_clicks, name, author, category, 
                               rating, description, image_url, download_url, 
                               uploaded_image, editing_id, current_data):
        """Add or update a book."""
        global books_df
        ctx = dash.callback_context
        
        # Default values for resetting the form
        empty_values = ["", "", None, None, "", "", ""]
        default_button_classes = ["w-100 mb-2", "w-100 mb-2 d-none", "w-100 mb-2 d-none"]
        
        # Validation
        if not name or not author:
            return [
                current_data,
                dbc.Alert("Book name and author are required", color="danger"),
                *empty_values,
                None,
                *default_button_classes,
                None
            ]
        
        # Prepare book data
        book_data = {
            'name': name,
            'author': author,
            'category': category,
            'ratings': rating,
            'description': description,
            'image_url': image_url,
            'download_url': download_url
        }
        
        feedback = None
        
        # Add new book
        if ctx.triggered[0]['prop_id'] == 'add-book-button.n_clicks':
            books_df = add_book(books_df, book_data, uploaded_image)
            feedback = dbc.Alert("Book added successfully!", color="success", dismissable=True)
        
        # Update existing book
        elif ctx.triggered[0]['prop_id'] == 'update-book-button.n_clicks' and editing_id:
            books_df = update_book(books_df, editing_id, book_data, uploaded_image)
            feedback = dbc.Alert("Book updated successfully!", color="success", dismissable=True)
        
        return [
            books_df.to_dict('records'),
            feedback,
            *empty_values,
            None,
            *default_button_classes,
            None
        ]
    
    @app.callback(
        Output('delete-modal', 'is_open'),
        [Input('delete-book-button', 'n_clicks'),
         Input('cancel-delete', 'n_clicks'),
         Input('confirm-delete', 'n_clicks')],
        [State('delete-modal', 'is_open')]
    )
    def toggle_delete_modal(delete_click, cancel_click, confirm_click, is_open):
        """Toggle the delete confirmation modal."""
        ctx = dash.callback_context
        
        if not ctx.triggered:
            return is_open
        
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        
        if button_id == "delete-book-button":
            return True
        elif button_id in ["cancel-delete", "confirm-delete"]:
            return False
        
        return is_open
    
    @app.callback(
        [Output('books-table', 'data', allow_duplicate=True),
         Output('books-table', 'selected_rows')],
        [Input('confirm-delete', 'n_clicks')],
        [State('books-table', 'selected_rows'),
         State('books-table', 'data')],
        prevent_initial_call=True
    )
    def delete_selected_book(confirm_click, selected_rows, table_data):
        """Delete the selected book."""
        global books_df
        
        if not confirm_click or not selected_rows:
            raise PreventUpdate
        
        # Get the ID of the book to delete
        book_id = table_data[selected_rows[0]]['id']
        
        # Update the DataFrame
        books_df = delete_book(books_df, book_id)
        
        return books_df.to_dict('records'), []
    
    @app.callback(
        Output('books-table', 'data', allow_duplicate=True),
        [Input('search-books', 'value'),
         Input('filter-category', 'value')],
        [State('books-table', 'data')],
        prevent_initial_call=True
    )
    def filter_books_table(search_term, category, table_data):
        """Filter books based on search term and category."""
        filtered_df = filter_books(books_df, search_term, category)
        return filtered_df.to_dict('records')
