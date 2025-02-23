# comments.py
import requests
from datetime import datetime

def fetch_book_comments(book_id):
    """Fetch comments for a specific book including admin replies"""
    try:
        response = requests.get(f'http://127.0.0.1:5000/book/{book_id}/comments')
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching comments: {e}")
        return []

def format_date(date_str):
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        delta = datetime.utcnow() - date
        if delta.days == 0:
            return "Today"
        elif delta.days == 1:
            return "Yesterday"
        else:
            return f"{delta.days} days ago"
    except Exception as e:
        print(f"Error formatting date: {e}")
        return date_str

def generate_comments_html(comments):
    """Generate HTML for comments"""
    comments_html = ""
    for comment in comments:
        admin_reply_html = ""
        if comment.get('reply_from_admin'):
            admin_reply_html = f"""
                <div class="bg-primary/10 p-3 mt-2 rounded-lg">
                    <div class="flex items-center gap-2 mb-1">
                        <i class="fas fa-shield-alt text-primary"></i>
                        <span class="font-semibold text-primary">Admin Reply</span>
                    </div>
                    <p>{comment['reply_from_admin']}</p>
                </div>
            """

        comments_html += f"""
            <div class="bg-base-200 p-4 rounded-lg" id="comment-{comment['comment_id']}">
                <div class="flex items-center gap-2 mb-2">
                    <i class="fas fa-user-circle text-2xl"></i>
                    <span class="font-semibold">{comment['user_name']}</span>
                    <span class="text-sm text-gray-500">{format_date(comment['created_at'])}</span>
                </div>
                <p>{comment['comment']}</p>
                {admin_reply_html}
                <div class="flex gap-2 mt-2">
                    <button onclick="editComment({comment['comment_id']}, '{comment['comment']}')" 
                            class="btn btn-xs btn-ghost">
                        <i class="fas fa-edit"></i>
                    </button>
                    <button onclick="deleteComment({comment['comment_id']})" 
                            class="btn btn-xs btn-ghost text-error">
                        <i class="fas fa-trash"></i>
                    </button>
                </div>
            </div>
        """

    # If no comments, show a message
    if not comments:
        comments_html = """
            <div class="text-center text-gray-500 py-4">
                <p>No comments yet. Be the first to comment!</p>
            </div>
        """

    return comments_html
