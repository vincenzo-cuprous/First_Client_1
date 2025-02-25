import dash
from dash import dcc, html, Input, Output, State
import requests
import json

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Book API Tester"),
    
    html.Div([
        html.H3("Add Book"),
        dcc.Input(id='book-name', type='text', placeholder='Book Name'),
        dcc.Input(id='author-name', type='text', placeholder='Author Name'),
        dcc.Input(id='ratings', type='number', placeholder='Ratings'),
        dcc.Input(id='category', type='text', placeholder='Category'),
        dcc.Input(id='description', type='text', placeholder='Description'),
        dcc.Input(id='picture-url', type='text', placeholder='Picture URL'),
        dcc.Input(id='download-url', type='text', placeholder='Download URL'),
        html.Button('Add Book', id='add-button', n_clicks=0),
    ]),
    
    html.Div(id='add-response'),

    html.Div([
        html.H3("Get Book by ID"),
        dcc.Input(id='get-book-id', type='number', placeholder='Book ID'),
        html.Button('Get Book', id='get-button', n_clicks=0),
        html.Div(id='get-response'),
    ]),
    
    html.Div([
        html.H3("Get All Books"),
        html.Button('Get All Books', id='get-all-button', n_clicks=0),
        html.Div(id='get-all-response'),
    ]),

    html.Div([
        html.H3("Update Book"),
        dcc.Input(id='update-book-id', type='number', placeholder='Book ID', required=True),
        dcc.Input(id='update-book-name', type='text', placeholder='New Book Name'),
        dcc.Input(id='update-author-name', type='text', placeholder='New Author Name'),
        dcc.Input(id='update-ratings', type='number', placeholder='New Ratings'),
        dcc.Input(id='update-category', type='text', placeholder='New Category'),
        dcc.Input(id='update-description', type='text', placeholder='New Description'),
        dcc.Input(id='update-picture-url', type='text', placeholder='New Picture URL'),
        dcc.Input(id='update-download-url', type='text', placeholder='New Download URL'),
        html.Button('Update Book', id='update-button', n_clicks=0),
        html.Div(id='update-response'),
    ]),

    html.Div([
        html.H3("Delete Book"),
        dcc.Input(id='delete-book-id', type='number', placeholder='Book ID'),
        html.Button('Delete Book', id='delete-button', n_clicks=0),
        html.Div(id='delete-response'),
    ]),
])

@app.callback(Output('add-response', 'children'),
              Input('add-button', 'n_clicks'),
              [State('book-name', 'value'),
               State('author-name', 'value'),
               State('ratings', 'value'),
               State('category', 'value'),
               State('description', 'value'),
               State('picture-url', 'value'),
               State('download-url', 'value')])
def add_book(n_clicks, book_name, author_name, ratings, category, description, picture_url, download_url):
    if n_clicks > 0:
        payload = {
            "book_name": book_name,
            "ratings": ratings,
            "author_name": author_name,
            "category": category,
            "description": description,
            "picture_url": picture_url,
            "download_url": download_url
        }
        response = requests.post("http://127.0.0.1:5000/book", json=payload)
        return f'Response: {response.text}'

@app.callback(Output('get-response', 'children'),
              Input('get-button', 'n_clicks'),
              State('get-book-id', 'value'))
def get_book(n_clicks, book_id):
    if n_clicks > 0:
        response = requests.get(f"http://127.0.0.1:5000/book/{book_id}")
        return f'Response: {response.text}'

@app.callback(Output('get-all-response', 'children'),
              Input('get-all-button', 'n_clicks'))
def get_all_books(n_clicks):
    if n_clicks > 0:
        response = requests.get("http://127.0.0.1:5000/books")
        return f'Response: {response.text}'

@app.callback(Output('update-response', 'children'),
              Input('update-button', 'n_clicks'),
              [State('update-book-id', 'value'),
               State('update-book-name', 'value'),
               State('update-author-name', 'value'),
               State('update-ratings', 'value'),
               State('update-category', 'value'),
               State('update-description', 'value'),
               State('update-picture-url', 'value'),
               State('update-download-url', 'value')])
def update_book(n_clicks, book_id, book_name, author_name, ratings, category, description, picture_url, download_url):
    if n_clicks > 0:
        payload = {}
        if book_name:
            payload["book_name"] = book_name
        if author_name:
            payload["author_name"] = author_name
        if ratings is not None:
            payload["ratings"] = ratings
        if category:
            payload["category"] = category
        if description:
            payload["description"] = description
        if picture_url:
            payload["picture_url"] = picture_url
        if download_url:
            payload["download_url"] = download_url
        
        if not payload:  # If no fields are provided
            return "No fields to update."

        response = requests.put(f"http://127.0.0.1:5000/book/{book_id}", json=payload)
        return f'Response: {response.text}'

@app.callback(Output('delete-response', 'children'),
              Input('delete-button', 'n_clicks'),
              State('delete-book-id', 'value'))
def delete_book(n_clicks, book_id):
    if n_clicks > 0:
        response = requests.delete(f"http://127.0.0.1:5000/book/{book_id}")
        return f'Response: {response.text}'

if __name__ == '__main__':
    app.run_server(debug=True)
