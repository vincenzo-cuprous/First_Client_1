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
    reply_from_admin = db.Column(db.Text, nullable=True)  # New field for admin replies
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'comment_id': self.comment_id,
            'book_id': self.book_id,
            'user_id': self.user_id,
            'user_name': self.user_name,
            'comment': self.comment,
            'reply_from_admin': self.reply_from_admin,  # Include admin reply in response
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
        
        # Allow updating both comment text and admin reply
        if 'comment' in data:
            comment.comment = data['comment']
        if 'reply_from_admin' in data:
            comment.reply_from_admin = data['reply_from_admin']
        
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

# New functions for admin replies
def add_admin_reply(comment_id):
    try:
        comment = Comment.query.get_or_404(comment_id)
        data = request.json
        
        comment.reply_from_admin = data['reply_from_admin']
        db.session.commit()
        return jsonify({'message': 'Admin reply added successfully', 'comment': comment.to_dict()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

def delete_admin_reply(comment_id):
    try:
        comment = Comment.query.get_or_404(comment_id)
        comment.reply_from_admin = None
        db.session.commit()
        return jsonify({'message': 'Admin reply deleted successfully', 'comment': comment.to_dict()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

def get_comments_with_admin_replies():
    comments = Comment.query.filter(Comment.reply_from_admin.isnot(None)).all()
    return jsonify([comment.to_dict() for comment in comments])

def get_comments_without_admin_replies():
    comments = Comment.query.filter(Comment.reply_from_admin.is_(None)).all()
    return jsonify([comment.to_dict() for comment in comments])
