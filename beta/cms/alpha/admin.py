from dash import html, dcc, callback, Input, Output, State, dash_table
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import pandas as pd
import base64
import io
import uuid
import os

# Initialize an empty DataFrame to store books
# In a real application, this would be a database
try:
    books_df = pd.read_csv('assets/books_data.csv')
except:
    books_df = pd.DataFrame(columns=[
        'id', 'name', 'author', 'description', 'category', 'ratings', 'image_url', 'download_url'
    ])

def serve_admin():
    """
    Returns the admin page content for managing books with CRUD operations.
    """
    return html.Div([
        # Admin Header
        html.Section(
            dbc.Container([
                dbc.Row([
                    dbc.Col([
                        html.H1("Book Management Dashboard", 
                                className="text-4xl font-bold mb-6 text-center pt-8"),
                        html.P("Add, remove, or update books in your collection",
                               className="text-xl text-center text-base-content/80 mb-8")
                    ], md=10, className="mx-auto")
                ])
            ], fluid=True),
            className="bg-base-200"
        ),
        
        # Book Management Section
        html.Section(
            dbc.Container([
                dbc.Row([
                    # Left Column - Add/Edit Book Form
                    dbc.Col([
                        html.Div([
                            html.H2("Add/Edit Book", className="text-2xl font-bold mb-4"),
                            
                            # Hidden book ID for editing
                            dcc.Store(id="editing-book-id", data=None),
                            
                            # Book Details Form
                            dbc.Form([
                                dbc.Row([
                                    dbc.Col([
                                        dbc.Label("Book Name", html_for="book-name"),
                                        dbc.Input(id="book-name", type="text", placeholder="Enter book name", className="mb-3"),
                                    ], md=6),
                                    dbc.Col([
                                        dbc.Label("Author Name", html_for="author-name"),
                                        dbc.Input(id="author-name", type="text", placeholder="Enter author name", className="mb-3"),
                                    ], md=6)
                                ]),
                                
                                dbc.Row([
                                    dbc.Col([
                                        dbc.Label("Category", html_for="book-category"),
                                        dbc.Select(
                                            id="book-category",
                                            options=[
                                                {"label": "Fiction", "value": "Fiction"},
                                                {"label": "Non-Fiction", "value": "Non-Fiction"},
                                                {"label": "Science", "value": "Science"},
                                                {"label": "Technology", "value": "Technology"},
                                                {"label": "Business", "value": "Business"},
                                                {"label": "Self-Help", "value": "Self-Help"},
                                                {"label": "Other", "value": "Other"}
                                            ],
                                            className="mb-3"
                                        ),
                                    ], md=6),
                                    dbc.Col([
                                        dbc.Label("Rating (1-5)", html_for="book-rating"),
                                        dbc.Input(id="book-rating", type="number", min=1, max=5, step=0.1, 
                                                 placeholder="Rating (1-5)", className="mb-3"),
                                    ], md=6)
                                ]),
                                
                                dbc.Label("Description", html_for="book-description"),
                                dbc.Textarea(
                                    id="book-description",
                                    placeholder="Enter book description",
                                    style={"height": "120px"},
                                    className="mb-3"
                                ),
                                
                                dbc.Row([
                                    dbc.Col([
                                        dbc.Label("Book Cover Image URL", html_for="book-image"),
                                        dbc.Input(id="book-image", type="text", placeholder="Enter image URL", className="mb-3"),
                                    ], md=6),
                                    dbc.Col([
                                        dbc.Label("Download URL", html_for="book-download"),
                                        dbc.Input(id="book-download", type="text", placeholder="Enter download URL", className="mb-3"),
                                    ], md=6)
                                ]),
                                
                                # Upload image option
                                dbc.Label("Or Upload Book Cover Image"),
                                dcc.Upload(
                                    id='upload-image',
                                    children=html.Div([
                                        'Drag and Drop or ',
                                        html.A('Select an Image', className="text-primary")
                                    ]),
                                    style={
                                        'width': '100%',
                                        'height': '60px',
                                        'lineHeight': '60px',
                                        'borderWidth': '1px',
                                        'borderStyle': 'dashed',
                                        'borderRadius': '5px',
                                        'textAlign': 'center',
                                        'margin': '10px 0'
                                    },
                                    className="mb-3"
                                ),
                                
                                # Uploaded image preview
                                html.Div(id='image-preview', className="mb-3"),
                                
                                # Submit buttons
                                dbc.Row([
                                    dbc.Col([
                                        dbc.Button("Add Book", id="add-book-button", color="primary", className="w-100 mb-2"),
                                        dbc.Button("Update Book", id="update-book-button", color="success", className="w-100 mb-2 d-none"),
                                        dbc.Button("Cancel Editing", id="cancel-edit-button", color="secondary", className="w-100 mb-2 d-none"),
                                    ])
                                ]),
                                
                                # Feedback alert
                                html.Div(id="form-feedback")
                            ])
                        ], className="bg-base-100 p-4 rounded-lg shadow-lg")
                    ], md=5),
                    
                    # Right Column - Books List/Table
                    dbc.Col([
                        html.Div([
                            html.H2("Book Collection", className="text-2xl font-bold mb-4"),
                            
                            # Search and Filter Row
                            dbc.Row([
                                dbc.Col([
                                    dbc.Input(id="search-books", type="text", placeholder="Search books...", className="mb-3"),
                                ], md=8),
                                dbc.Col([
                                    dbc.Select(
                                        id="filter-category",
                                        options=[
                                            {"label": "All Categories", "value": "all"},
                                            {"label": "Fiction", "value": "Fiction"},
                                            {"label": "Non-Fiction", "value": "Non-Fiction"},
                                            {"label": "Science", "value": "Science"},
                                            {"label": "Technology", "value": "Technology"},
                                            {"label": "Business", "value": "Business"},
                                            {"label": "Self-Help", "value": "Self-Help"},
                                            {"label": "Other", "value": "Other"}
                                        ],
                                        value="all",
                                        className="mb-3"
                                    ),
                                ], md=4)
                            ]),
                            
                            # Books Data Table
                            dash_table.DataTable(
                                id='books-table',
                                columns=[
                                    {'name': 'Name', 'id': 'name'},
                                    {'name': 'Author', 'id': 'author'},
                                    {'name': 'Category', 'id': 'category'},
                                    {'name': 'Rating', 'id': 'ratings'},
                                ],
                                data=books_df.to_dict('records'),
                                style_table={'overflowX': 'auto'},
                                style_cell={
                                    'textAlign': 'left',
                                    'padding': '10px',
                                    'fontFamily': 'system-ui'
                                },
                                style_header={
                                    'backgroundColor': 'rgb(230, 230, 230)',
                                    'fontWeight': 'bold'
                                },
                                style_data_conditional=[
                                    {
                                        'if': {'row_index': 'odd'},
                                        'backgroundColor': 'rgb(248, 248, 248)'
                                    }
                                ],
                                page_size=8,
                                row_selectable='single',
                                selected_rows=[],
                            ),
                            
                            # Action Buttons
                            dbc.Row([
                                dbc.Col([
                                    dbc.Button([
                                        html.I(className="fas fa-edit mr-2"),
                                        "Edit Selected"
                                    ], id="edit-book-button", color="warning", className="w-100 mb-2", disabled=True),
                                ], md=6),
                                dbc.Col([
                                    dbc.Button([
                                        html.I(className="fas fa-trash-alt mr-2"),
                                        "Delete Selected"
                                    ], id="delete-book-button", color="danger", className="w-100 mb-2", disabled=True),
                                ], md=6)
                            ], className="mt-3")
                        ], className="bg-base-100 p-4 rounded-lg shadow-lg")
                    ], md=7)
                ], className="py-5 gap-4")
            ], fluid=True),
            className="bg-base-100 min-h-screen"
        ),
        
        # Confirmation Modal for Delete
        dbc.Modal(
            [
                dbc.ModalHeader("Confirm Deletion"),
                dbc.ModalBody("Are you sure you want to delete this book?"),
                dbc.ModalFooter([
                    dbc.Button(
                        "Cancel", id="cancel-delete", className="ml-auto"
                    ),
                    dbc.Button(
                        "Delete", id="confirm-delete", color="danger"
                    ),
                ]),
            ],
            id="delete-modal",
            is_open=False,
        ),
    ])

# Define callbacks for Admin page functionality
def register_callbacks(app):
    """
    Register all callbacks for the admin page functionality.
    """
    
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
        
        # Handle the uploaded image if available
        if uploaded_image and not image_url:
            # In a real app, save the image to a server/cloud storage
            # For this example, we'll just use the data URL
            image_url = uploaded_image
            
            # In a real app, you would do something like:
            # file_name = f"book_cover_{uuid.uuid4()}.jpg"
            # save_path = os.path.join('assets', 'images', file_name)
            # with open(save_path, 'wb') as f:
            #     f.write(base64.b64decode(uploaded_image.split(',')[1]))
            # image_url = f"/assets/images/{file_name}"
        
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
            book_data['id'] = str(uuid.uuid4())
            
            # Update the DataFrame
            books_df = pd.concat([books_df, pd.DataFrame([book_data])], ignore_index=True)
            
            # Save to CSV (in a real app, this would be a database operation)
            os.makedirs('assets', exist_ok=True)
            books_df.to_csv('assets/books_data.csv', index=False)
            
            feedback = dbc.Alert("Book added successfully!", color="success", dismissable=True)
        
        # Update existing book
        elif ctx.triggered[0]['prop_id'] == 'update-book-button.n_clicks' and editing_id:
            book_data['id'] = editing_id
            
            # Update the DataFrame
            books_df = books_df[books_df['id'] != editing_id]
            books_df = pd.concat([books_df, pd.DataFrame([book_data])], ignore_index=True)
            
            # Save to CSV
            books_df.to_csv('assets/books_data.csv', index=False)
            
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
    def delete_book(confirm_click, selected_rows, table_data):
        """Delete the selected book."""
        global books_df
        
        if not confirm_click or not selected_rows:
            raise PreventUpdate
        
        # Get the ID of the book to delete
        book_id = table_data[selected_rows[0]]['id']
        
        # Update the DataFrame
        books_df = books_df[books_df['id'] != book_id]
        
        # Save to CSV
        books_df.to_csv('assets/books_data.csv', index=False)
        
        return books_df.to_dict('records'), []
    
    @app.callback(
        Output('books-table', 'data', allow_duplicate=True),
        [Input('search-books', 'value'),
         Input('filter-category', 'value')],
        [State('books-table', 'data')],
        prevent_initial_call=True
    )
    def filter_books(search_term, category, table_data):
        """Filter books based on search term and category."""
        filtered_df = books_df.copy()
        
        # Apply search filter
        if search_term:
            search_term = search_term.lower()
            filtered_df = filtered_df[
                filtered_df['name'].str.lower().str.contains(search_term, na=False) |
                filtered_df['author'].str.lower().str.contains(search_term, na=False) |
                filtered_df['description'].str.lower().str.contains(search_term, na=False)
            ]
        
        # Apply category filter
        if category and category != 'all':
            filtered_df = filtered_df[filtered_df['category'] == category]
        
        return filtered_df.to_dict('records')
