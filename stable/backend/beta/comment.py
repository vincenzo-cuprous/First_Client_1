# comment.py
from datetime import datetime
from flask import jsonify, request
from settings import db

class Comment(db.Model):
    __bind_key__ = 'comments'
    
    comment_id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'comment_id': self.comment_id,
            'book_id': self.book_id,
            'user_id': self.user_id,
            'user_name': self.user_name,
            'comment': self.comment,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

def add_comment(book_id):
    try:
        data = request.json
        new_comment = Comment(
            book_id=book_id,
            user_id=data['user_id'],
            user_name=data['user_name'],
            comment=data['comment']
        )
        db.session.add(new_comment)
        db.session.commit()
        return jsonify({'message': 'Comment added successfully', 'comment': new_comment.to_dict()}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

def get_book_comments(book_id):
    comments = Comment.query.filter_by(book_id=book_id).all()
    return jsonify([comment.to_dict() for comment in comments])

def update_comment(comment_id):
    try:
        comment = Comment.query.get_or_404(comment_id)
        data = request.json
        
        # Only allow updating the comment text
        comment.comment = data.get('comment', comment.comment)
        
        db.session.commit()
        return jsonify({'message': 'Comment updated successfully', 'comment': comment.to_dict()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    return jsonify({'message': 'Comment deleted successfully'})

def get_user_comments(user_id):
    comments = Comment.query.filter_by(user_id=user_id).all()
    return jsonify([comment.to_dict() for comment in comments])
