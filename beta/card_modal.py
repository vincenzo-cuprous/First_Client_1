# card_modal.py
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

def serve_card_modal(book):
    # Fetch comments for this book
    comments = fetch_book_comments(book['book_id'])
    
    # Generate comments HTML
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

    javascript_code = """
        async function initiateCommentPost(bookId) {
            const commentText = document.getElementById(`comment-text-${bookId}`).value;
            if (!commentText.trim()) return;

            // Show username modal
            document.getElementById(`username-modal-${bookId}`).showModal();
        }

        async function postComment(bookId) {
            const commentText = document.getElementById(`comment-text-${bookId}`).value;
            const username = document.getElementById(`username-input-${bookId}`).value;
            
            if (!username.trim()) {
                showError('Please enter a username');
                return;
            }

            try {
                const response = await fetch(`http://127.0.0.1:5000/book/${bookId}/comment`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        user_id: 1, // Replace with actual user ID from authentication
                        user_name: username,
                        comment: commentText
                    })
                });

                if (response.ok) {
                    await refreshComments(bookId);
                    document.getElementById(`comment-text-${bookId}`).value = '';
                    document.getElementById(`username-input-${bookId}`).value = '';
                    document.getElementById(`username-modal-${bookId}`).close();
                }
            } catch (error) {
                console.error('Error posting comment:', error);
                showError('Failed to post comment. Please try again.');
            }
        }

        async function editComment(commentId, currentText) {
            const newText = prompt('Edit your comment:', currentText);
            if (!newText || newText === currentText) return;

            try {
                const response = await fetch(`http://127.0.0.1:5000/comment/${commentId}`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        comment: newText
                    })
                });

                if (response.ok) {
                    const commentElement = document.getElementById(`comment-${commentId}`);
                    const bookId = commentElement.closest('.modal').id.replace('book-modal-', '');
                    await refreshComments(bookId);
                }
            } catch (error) {
                console.error('Error updating comment:', error);
                showError('Failed to update comment. Please try again.');
            }
        }

        async function deleteComment(commentId) {
            if (!confirm('Are you sure you want to delete this comment?')) return;

            try {
                const response = await fetch(`http://127.0.0.1:5000/comment/${commentId}`, {
                    method: 'DELETE'
                });

                if (response.ok) {
                    const commentElement = document.getElementById(`comment-${commentId}`);
                    const bookId = commentElement.closest('.modal').id.replace('book-modal-', '');
                    await refreshComments(bookId);
                }
            } catch (error) {
                console.error('Error deleting comment:', error);
                showError('Failed to delete comment. Please try again.');
            }
        }

        async function refreshComments(bookId) {
            try {
                const response = await fetch(`http://127.0.0.1:5000/book/${bookId}/comments`);
                const comments = await response.json();
                
                const container = document.getElementById(`comments-container-${bookId}`);
                container.innerHTML = comments.length ? comments.map(comment => {
                    const adminReplyHtml = comment.reply_from_admin ? `
                        <div class="bg-primary/10 p-3 mt-2 rounded-lg">
                            <div class="flex items-center gap-2 mb-1">
                                <i class="fas fa-shield-alt text-primary"></i>
                                <span class="font-semibold text-primary">Admin Reply</span>
                            </div>
                            <p>${comment.reply_from_admin}</p>
                        </div>
                    ` : '';

                    return `
                        <div class="bg-base-200 p-4 rounded-lg" id="comment-${comment.comment_id}">
                            <div class="flex items-center gap-2 mb-2">
                                <i class="fas fa-user-circle text-2xl"></i>
                                <span class="font-semibold">${comment.user_name}</span>
                                <span class="text-sm text-gray-500">${formatDate(comment.created_at)}</span>
                            </div>
                            <p>${comment.comment}</p>
                            ${adminReplyHtml}
                            <div class="flex gap-2 mt-2">
                                <button onclick="editComment(${comment.comment_id}, '${comment.comment}')" 
                                        class="btn btn-xs btn-ghost">
                                    <i class="fas fa-edit"></i>
                                </button>
                                <button onclick="deleteComment(${comment.comment_id})" 
                                        class="btn btn-xs btn-ghost text-error">
                                    <i class="fas fa-trash"></i>
                                </button>
                            </div>
                        </div>
                    `;
                }).join('') : `
                    <div class="text-center text-gray-500 py-4">
                        <p>No comments yet. Be the first to comment!</p>
                    </div>
                `;
            } catch (error) {
                console.error('Error refreshing comments:', error);
                showError('Failed to refresh comments. Please try again.');
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

        function showError(message) {
            const toast = document.createElement('div');
            toast.className = 'toast toast-error';
            toast.textContent = message;
            document.body.appendChild(toast);
            setTimeout(() => toast.remove(), 3000);
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
                            <button onclick="initiateCommentPost({book['book_id']})" class="btn btn-primary">
                                <i class="fas fa-paper-plane mr-2"></i>Post Comment
                            </button>
                        </div>
                        
                        <!-- Username Modal -->
                        <dialog id="username-modal-{book['book_id']}" class="modal">
                            <div class="modal-box">
                                <h3 class="font-bold text-lg mb-4">Enter Your Username</h3>
                                <input type="text" 
                                       id="username-input-{book['book_id']}"
                                       class="input input-bordered w-full"
                                       placeholder="Enter your username"
                                       onkeypress="if(event.key === 'Enter') postComment({book['book_id']})" />
                                <div class="modal-action">
                                    <button class="btn btn-ghost" onclick="document.getElementById('username-modal-{book['book_id']}').close()">
                                        Cancel
                                    </button>
                                    <button class="btn btn-primary" onclick="postComment({book['book_id']})">
                                        Submit
                                    </button>
                                </div>
                            </div>
                        </dialog>
                        
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
