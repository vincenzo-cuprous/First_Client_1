# books/comments.py
import requests
from dash import html, dcc
from dash.dependencies import Input, Output, State

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

def register_comment_callbacks(app):
    """Register callbacks related to comments."""
    @app.callback(
        Output("comments-list", "children"),
        [Input("load-comments", "n_intervals")],
        [State("book-id-store", "data")]
    )
    def load_comments(n_intervals, book_id):
        """Load and display comments for a book."""
        if not book_id:
            return html.Div("Book ID not provided", className="text-center py-12")
        return load_comments_for_book(book_id)
    
    @app.callback(
        Output("comment-status", "children"),
        [Input("submit-comment", "n_clicks")],
        [State("comment-input", "value"),
         State("book-id-store", "data")]
    )
    def submit_comment(n_clicks, comment_text, book_id):
        """Handle submission of a new comment."""
        if not n_clicks or not comment_text or not book_id:
            return html.Div("Please write a comment before submitting.", className="text-center py-2 text-base-content/80")
        
        try:
            response = requests.post(
                f"{API_BASE_URL}/book/{book_id}/comments",
                json={"comment": comment_text}
            )
            if response.status_code == 200:
                return html.Div("Comment submitted successfully!", className="text-center py-2 text-success")
            else:
                return html.Div(f"Error submitting comment: {response.status_code}", className="text-center py-2 text-error")
        except Exception as e:
            return html.Div(f"Error: {str(e)}", className="text-center py-2 text-error")
