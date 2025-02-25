import dash
from dash import dcc, html, Input, Output, State
import requests

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "Book Management"

# Layout of the app
app.layout = html.Div([
    html.H1("Book Management"),
    
    # Section for managing books
    html.H2("Manage Books"),
    dcc.Input(id='book-id-input', type='number', placeholder='Book ID'),
    dcc.Input(id='book-name-input', placeholder='Book Name'),
    dcc.Input(id='ratings-input', type='number', placeholder='Ratings'),
    dcc.Input(id='author-name-input', placeholder='Author Name'),
    dcc.Input(id='category-input', placeholder='Category'),
    dcc.Input(id='description-input', placeholder='Description'),
    dcc.Input(id='picture-url-input', placeholder='Picture URL'),
    dcc.Input(id='download-url-input', placeholder='Download URL'),
    html.Button('Add Book', id='add-book-button'),
    html.Button('Update Book', id='update-book-button'),
    html.Button('Delete Book', id='delete-book-button'),
    html.Div(id='book-message'),
    
    # Section for viewing all books
    html.H2("View All Books"),
    html.Button('Refresh Books', id='refresh-books-button'),
    html.Div(id='all-books-display'),
])

# Function to generate a new book ID
def generate_book_id():
    response = requests.get('http://localhost:5000/books')
    if response.status_code == 200:
        books = response.json()
        if books:
            max_id = max(book['book_id'] for book in books)
            return max_id + 1
        else:
            return 1
    else:
        return None

# Callback for managing books
@app.callback(
    Output('book-message', 'children'),
    [Input('add-book-button', 'n_clicks'),
     Input('update-book-button', 'n_clicks'),
     Input('delete-book-button', 'n_clicks')],
    [State('book-id-input', 'value'),
     State('book-name-input', 'value'),
     State('ratings-input', 'value'),
     State('author-name-input', 'value'),
     State('category-input', 'value'),
     State('description-input', 'value'),
     State('picture-url-input', 'value'),
     State('download-url-input', 'value')]
)
def manage_books(add_clicks, update_clicks, delete_clicks, book_id, book_name, ratings, author_name, category, description, picture_url, download_url):
    ctx = dash.callback_context
    if not ctx.triggered:
        return ""
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        
        if button_id == 'add-book-button':
            if not book_id:
                book_id = generate_book_id()
                if not book_id:
                    return "Failed to generate a new book ID."
            
            response = requests.post('http://localhost:5000/book', json={
                'book_id': book_id,
                'book_name': book_name,
                'ratings': ratings,
                'author_name': author_name,
                'category': category,
                'description': description,
                'picture_url': picture_url,
                'download_url': download_url
            })
            return f"Book added with ID: {response.json().get('book_id')}"
        
        elif button_id == 'update-book-button':
            response = requests.put(f'http://localhost:5000/book/{book_id}', json={
                'book_name': book_name,
                'ratings': ratings
            })
            return f"Book updated: {response.status_code}"
        
        elif button_id == 'delete-book-button':
            response = requests.delete(f'http://localhost:5000/book/{book_id}')
            return f"Book deleted: {response.status_code}"

# Callback for viewing all books
@app.callback(
    Output('all-books-display', 'children'),
    [Input('refresh-books-button', 'n_clicks')]
)
def view_all_books(refresh_clicks):
    if refresh_clicks is None:
        return "Click 'Refresh Books' to load all books."
    
    response = requests.get('http://localhost:5000/books')
    if response.status_code == 200:
        books = response.json()
        book_list = []
        for book in books:
            book_list.append(html.Div([
                html.H3(f"Book ID: {book['book_id']}"),
                html.P(f"Name: {book['book_name']}"),
                html.P(f"Author: {book['author_name']}"),
                html.P(f"Category: {book['category']}"),
                html.P(f"Ratings: {book['ratings']}"),
                html.P(f"Description: {book['description']}"),
                html.Hr()
            ]))
        return book_list
    else:
        return "Failed to fetch books."

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
