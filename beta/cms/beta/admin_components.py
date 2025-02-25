# admin_components.py
"""Components for the admin interface."""
from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc

def create_admin_header():
    """Create the admin page header section."""
    return html.Section(
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
    )

def create_book_form():
    """Create the book add/edit form."""
    return html.Div([
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

def create_books_table(books_data):
    """Create the books data table."""
    return html.Div([
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
            data=books_data,
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

def create_delete_modal():
    """Create the delete confirmation modal."""
    return dbc.Modal(
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
    )
