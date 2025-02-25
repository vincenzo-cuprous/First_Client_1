# admin_data.py
"""Data handling functions for the admin interface."""
import pandas as pd
import uuid
import os
import base64
import io

# Initialize an empty DataFrame to store books
# In a real application, this would be a database
def load_books_data():
    """Load books data from CSV file or create empty DataFrame if file doesn't exist."""
    try:
        books_df = pd.read_csv('assets/books_data.csv')
    except:
        books_df = pd.DataFrame(columns=[
            'id', 'name', 'author', 'description', 'category', 'ratings', 'image_url', 'download_url'
        ])
    return books_df

def save_books_data(books_df):
    """Save books data to CSV file."""
    os.makedirs('assets', exist_ok=True)
    books_df.to_csv('assets/books_data.csv', index=False)

def add_book(books_df, book_data, uploaded_image=None):
    """Add a new book to the DataFrame."""
    # Handle the uploaded image if available
    if uploaded_image and not book_data.get('image_url'):
        # In a real app, save the image to a server/cloud storage
        # For this example, we'll just use the data URL
        book_data['image_url'] = uploaded_image
    
    # Add unique ID
    book_data['id'] = str(uuid.uuid4())
    
    # Update the DataFrame
    updated_df = pd.concat([books_df, pd.DataFrame([book_data])], ignore_index=True)
    
    # Save to CSV
    save_books_data(updated_df)
    
    return updated_df

def update_book(books_df, book_id, book_data, uploaded_image=None):
    """Update an existing book in the DataFrame."""
    # Handle the uploaded image if available
    if uploaded_image and not book_data.get('image_url'):
        book_data['image_url'] = uploaded_image
    
    # Add book ID to data
    book_data['id'] = book_id
    
    # Update the DataFrame
    updated_df = books_df[books_df['id'] != book_id]
    updated_df = pd.concat([updated_df, pd.DataFrame([book_data])], ignore_index=True)
    
    # Save to CSV
    save_books_data(updated_df)
    
    return updated_df

def delete_book(books_df, book_id):
    """Delete a book from the DataFrame."""
    updated_df = books_df[books_df['id'] != book_id]
    
    # Save to CSV
    save_books_data(updated_df)
    
    return updated_df

def filter_books(books_df, search_term=None, category=None):
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
    
    return filtered_df
