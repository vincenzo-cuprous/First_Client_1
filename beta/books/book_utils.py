# books/book_utils.py
import requests
from dash import html

API_BASE_URL = "http://localhost:5000"

def load_comments_for_book(book_id):
    """Fetch and format comments for a book."""
    try:
        response = requests.get(f"{API_BASE_URL}/book/{book_id}/comments")
        if response.status_code == 200:
            comments_data = response.json()
            comment_elements = []
            
            for comment in comments_data:
                comment_el = html.Div([
                    html.P(comment.get("comment", ""), className="text-base-content/80"),
                    html.P(f"By: {comment.get('user_name', 'Anonymous')}", className="text-sm text-base-content/60"),
                    html.Div([
                        html.Hr(className="my-2"),
                        html.P([
                            html.Span("Admin: ", className="font-bold"),
                            comment.get("reply_from_admin", "")
                        ], className="text-base-content/80 italic")
                    ]) if comment.get("reply_from_admin") else html.Div()
                ], className="bg-base-200 p-4 rounded-lg")
                
                comment_elements.append(comment_el)
            
            if not comment_elements:
                return [html.P("No comments yet. Be the first to comment!", className="text-center py-4")]
                
            return comment_elements
        else:
            print(f"Error loading comments: {response.status_code}")  # Log the error
            return [html.P(f"Error loading comments: {response.status_code}", className="text-center py-4")]
    except Exception as e:
        print(f"Error in load_comments_for_book: {str(e)}")  # Log the error
        return [html.P(f"Error: {str(e)}", className="text-center py-4")]
