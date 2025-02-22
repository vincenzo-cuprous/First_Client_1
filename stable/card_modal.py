# card_modal.py
import requests
from datetime import datetime

def fetch_book_comments(book_id):
    try:
        response = requests.get(f'http://127.0.0.1:5000/book/{book_id}/comments')
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching comments: {e}")
        return []

def format_date(date_str):
    # Convert backend datetime to "X days ago" format
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

def serve_card_modal(book):
    # Fetch comments for this book
    comments = fetch_book_comments(book['book_id'])
    
    # Generate comments HTML
    comments_html = ""
    for comment in comments:
        comments_html += f"""
            <div class="bg-base-200 p-4 rounded-lg">
                <div class="flex items-center gap-2 mb-2">
                    <i class="fas fa-user-circle text-2xl"></i>
                    <span class="font-semibold">{comment['user_name']}</span>
                    <span class="text-sm text-gray-500">{format_date(comment['created_at'])}</span>
                </div>
                <p>{comment['comment']}</p>
            </div>
        """

    # If no comments, show a message
    if not comments:
        comments_html = """
            <div class="text-center text-gray-500 py-4">
                <p>No comments yet. Be the first to comment!</p>
            </div>
        """

    javascript_code = """
        async function postComment(bookId) {
            const commentText = document.getElementById(`comment-text-${bookId}`).value;
            if (!commentText.trim()) return;

            try {
                const response = await fetch(`http://127.0.0.1:5000/book/${bookId}/comment`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        user_id: 1, // Replace with actual user ID from authentication
                        user_name: 'Guest User', // Replace with actual user name
                        comment: commentText
                    })
                });

                if (response.ok) {
                    // Refresh comments
                    const commentsResponse = await fetch(`http://127.0.0.1:5000/book/${bookId}/comments`);
                    const comments = await commentsResponse.json();
                    
                    // Update comments container
                    const container = document.getElementById(`comments-container-${bookId}`);
                    container.innerHTML = comments.map(comment => `
                        <div class="bg-base-200 p-4 rounded-lg">
                            <div class="flex items-center gap-2 mb-2">
                                <i class="fas fa-user-circle text-2xl"></i>
                                <span class="font-semibold">${comment.user_name}</span>
                                <span class="text-sm text-gray-500">${formatDate(comment.created_at)}</span>
                            </div>
                            <p>${comment.comment}</p>
                        </div>
                    `).join('');

                    // Clear input
                    document.getElementById(`comment-text-${bookId}`).value = '';
                }
            } catch (error) {
                console.error('Error posting comment:', error);
                alert('Failed to post comment. Please try again.');
            }
        }

        function formatDate(dateStr) {
            const date = new Date(dateStr);
            const now = new Date();
            const diffDays = Math.floor((now - date) / (1000 * 60 * 60 * 24));
            
            if (diffDays === 0) return 'Today';
            if (diffDays === 1) return 'Yesterday';
            return `${diffDays} days ago`;
        }

        function previewBook(bookId) {
            // Implement preview functionality
            alert('Preview feature coming soon!');
        }
    """

    return f"""
    <dialog id="book-modal-{book['book_id']}" class="modal">
        <div class="modal-box w-11/12 max-w-4xl">
            <div class="flex flex-col md:flex-row gap-6">
                <div class="md:w-1/3">
                    <img src="{book['picture_url']}" alt="{book['book_name']}" class="w-full rounded-xl shadow" />
                </div>
                <div class="md:w-2/3">
                    <h3 class="text-3xl font-bold mb-2">{book['book_name']}</h3>
                    <div class="badge badge-primary mb-4">
                        <i class="fas fa-book-quran mr-2"></i>{book['category']}
                    </div>
                    <p class="text-lg mb-4">{book['description'][:200]}...</p>
                    <div class="flex items-center gap-2 mb-4">
                        <span class="font-semibold flex items-center">
                            <i class="fas fa-user-pen mr-2"></i>Author:
                        </span>
                        <span>{book['author_name']}</span>
                    </div>
                    <div class="flex flex-wrap gap-4 mb-6">
                        <a href="{book['download_url']}" class="btn btn-primary" target="_blank">
                            <i class="fas fa-download mr-2"></i>Download
                        </a>
                        <button class="btn btn-secondary" onclick="previewBook({book['book_id']})">
                            <i class="fas fa-eye mr-2"></i>Preview
                        </button>
                    </div>
                    
                    <!-- Comments Section -->
                    <div class="border-t pt-6">
                        <h4 class="text-xl font-semibold mb-4 flex items-center">
                            <i class="fas fa-comments mr-2"></i>Comments
                        </h4>
                        
                        <!-- Comment Form -->
                        <div class="mb-6">
                            <textarea id="comment-text-{book['book_id']}" 
                                    class="textarea textarea-bordered w-full mb-2" 
                                    placeholder="Share your thoughts..."></textarea>
                            <button onclick="postComment({book['book_id']})" class="btn btn-primary">
                                <i class="fas fa-paper-plane mr-2"></i>Post Comment
                            </button>
                        </div>
                        
                        <!-- Existing Comments -->
                        <div class="space-y-4" id="comments-container-{book['book_id']}">
                            {comments_html}
                        </div>
                    </div>
                </div>
            </div>
            <div class="modal-action">
                <form method="dialog">
                    <button class="btn btn-circle btn-ghost absolute right-2 top-2">
                        <i class="fas fa-times text-xl"></i>
                    </button>
                </form>
            </div>
        </div>
    </dialog>

    <script>
        {javascript_code}
    </script>
    """
