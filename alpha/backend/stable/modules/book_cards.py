# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(200), nullable=False)
    ratings = db.Column(db.Float, nullable=False)
    author_name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    picture_url = db.Column(db.String(500), nullable=False)
    download_url = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'book_id': self.book_id,
            'book_name': self.book_name,
            'ratings': self.ratings,
            'author_name': self.author_name,
            'category': self.category,
            'description': self.description,
            'picture_url': self.picture_url,
            'download_url': self.download_url,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

# Create the database and tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/book', methods=['POST'])
def add_book():
    try:
        data = request.json
        new_book = Book(
            book_name=data['book_name'],
            ratings=data['ratings'],
            author_name=data['author_name'],
            category=data['category'],
            description=data['description'],
            picture_url=data['picture_url'],
            download_url=data['download_url']
        )
        db.session.add(new_book)
        db.session.commit()
        return jsonify({'message': 'Book added successfully', 'book': new_book.to_dict()}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/book/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify(book.to_dict())

@app.route('/books', methods=['GET'])
def get_all_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

@app.route('/book/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    try:
        book = Book.query.get_or_404(book_id)
        data = request.json
        
        book.book_name = data.get('book_name', book.book_name)
        book.ratings = data.get('ratings', book.ratings)
        book.author_name = data.get('author_name', book.author_name)
        book.category = data.get('category', book.category)
        book.description = data.get('description', book.description)
        book.picture_url = data.get('picture_url', book.picture_url)
        book.download_url = data.get('download_url', book.download_url)
        
        db.session.commit()
        return jsonify({'message': 'Book updated successfully', 'book': book.to_dict()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/book/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
