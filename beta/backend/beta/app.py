# app.py
from settings import app, db
from books import Book, add_book, get_book, get_all_books, update_book, delete_book
from comment import Comment, add_comment, get_book_comments, update_comment, delete_comment, get_user_comments

# Create the database and tables
with app.app_context():
    db.create_all()

# Book routes
app.route('/book', methods=['POST'])(add_book)
app.route('/book/<int:book_id>', methods=['GET'])(get_book)
app.route('/books', methods=['GET'])(get_all_books)
app.route('/book/<int:book_id>', methods=['PUT'])(update_book)
app.route('/book/<int:book_id>', methods=['DELETE'])(delete_book)

# Comment routes
app.route('/book/<int:book_id>/comment', methods=['POST'])(add_comment)
app.route('/book/<int:book_id>/comments', methods=['GET'])(get_book_comments)
app.route('/comment/<int:comment_id>', methods=['PUT'])(update_comment)
app.route('/comment/<int:comment_id>', methods=['DELETE'])(delete_comment)
app.route('/user/<int:user_id>/comments', methods=['GET'])(get_user_comments)

if __name__ == '__main__':
    app.run(debug=True)
