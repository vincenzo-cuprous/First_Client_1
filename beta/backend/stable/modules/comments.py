from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Comment model
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    comment = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"<Comment(user_id={self.user_id}, user_name='{self.user_name}', comment='{self.comment}')>"

# Create the database and tables
with app.app_context():
    db.create_all()

# Route to add a new comment
@app.route('/add_comment', methods=['POST'])
def add_comment():
    data = request.get_json()
    user_id = data.get('user_id')
    user_name = data.get('user_name')
    comment = data.get('comment')

    if not user_id or not user_name or not comment:
        return jsonify({"error": "Missing required fields"}), 400

    new_comment = Comment(user_id=user_id, user_name=user_name, comment=comment)
    db.session.add(new_comment)
    db.session.commit()

    return jsonify({"message": "Comment added successfully"}), 201

# Route to get all comments
@app.route('/get_comments', methods=['GET'])
def get_comments():
    comments = Comment.query.all()
    comments_list = [{"user_id": comment.user_id, "user_name": comment.user_name, "comment": comment.comment} for comment in comments]
    return jsonify(comments_list), 200

# Route to delete a comment by ID
@app.route('/delete_comment/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    comment = Comment.query.get(comment_id)
    if not comment:
        return jsonify({"error": "Comment not found"}), 404

    db.session.delete(comment)
    db.session.commit()

    return jsonify({"message": "Comment deleted successfully"}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
