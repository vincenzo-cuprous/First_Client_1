from settings import app, db
from books import (
    Book, add_book, get_book, get_all_books, update_book, delete_book
)
from flask import send_from_directory, render_template_string, abort, request, jsonify
import os
from werkzeug.utils import secure_filename
from datetime import datetime

# Configuration for file serving and uploads
SERVE_DIRECTORY = "db"  # Directory to serve files from
UPLOAD_FOLDER = 'uploads/books'
PICTURES_FOLDER = os.path.join(UPLOAD_FOLDER, 'pictures')
DOCUMENTS_FOLDER = os.path.join(UPLOAD_FOLDER, 'documents')

ALLOWED_PICTURE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
ALLOWED_DOCUMENT_EXTENSIONS = {'txt', 'pdf'}

# Ensure the upload folders exist
os.makedirs(PICTURES_FOLDER, exist_ok=True)
os.makedirs(DOCUMENTS_FOLDER, exist_ok=True)

# HTML template for directory listing
DIRECTORY_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>File Directory</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .file-list { list-style: none; padding: 0; }
        .file-item { padding: 10px; border-bottom: 1px solid #eee; }
        .file-item:hover { background-color: #f5f5f5; }
        .file-link { text-decoration: none; color: #333; }
        .file-link:hover { color: #007bff; }
        .directory { font-weight: bold; }
    </style>
</head>
<body>
    <h1>File Directory</h1>
    <ul class="file-list">
        {% if path != '' %}
        <li class="file-item">
            <a href="../" class="file-link">..</a>
        </li>
        {% endif %}
        {% for item in items %}
        <li class="file-item">
            <a href="{{ item.path }}" class="file-link {% if item.is_dir %}directory{% endif %}">
                {{ item.name }}{% if item.is_dir %}/{% endif %}
            </a>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
'''

# Create the database and tables
with app.app_context():
    db.create_all()

# Book routes
app.route('/book', methods=['POST'])(add_book)
app.route('/book/<int:book_id>', methods=['GET'])(get_book)
app.route('/books', methods=['GET'])(get_all_books)
app.route('/book/<int:book_id>', methods=['PUT'])(update_book)
app.route('/book/<int:book_id>', methods=['DELETE'])(delete_book)

# File upload functionality
def allowed_picture_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_PICTURE_EXTENSIONS

def allowed_document_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_DOCUMENT_EXTENSIONS

@app.route('/db/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_picture_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(PICTURES_FOLDER, filename))
        return jsonify({"message": f"Picture '{filename}' uploaded successfully!"}), 200

    if file and allowed_document_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(DOCUMENTS_FOLDER, filename))
        return jsonify({"message": f"Document '{filename}' uploaded successfully!"}), 200

    return jsonify({"error": "File type not allowed"}), 400

@app.route('/db/pictures/<path:filename>', methods=['GET'])
def get_picture(filename):
    return send_from_directory(PICTURES_FOLDER, filename)

@app.route('/db/documents/<path:filename>', methods=['GET'])
def get_document(filename):
    return send_from_directory(DOCUMENTS_FOLDER, filename)

# File serving routes
@app.route('/db/')
@app.route('/db/<path:path>')
def serve_files(path=''):
    try:
        # Get absolute path
        abs_path = os.path.join(SERVE_DIRECTORY, path)

        # Ensure the path is within the serve directory
        if not os.path.abspath(abs_path).startswith(os.path.abspath(SERVE_DIRECTORY)):
            abort(403)  # Forbidden

        # If path is a directory, show directory listing
        if os.path.isdir(abs_path):
            items = []
            for item in os.listdir(abs_path):
                item_path = os.path.join(path, item)
                items.append({
                    'name': item,
                    'path': item_path,
                    'is_dir': os.path.isdir(os.path.join(abs_path, item))
                })
            # Sort items: directories first, then files, both alphabetically
            items.sort(key=lambda x: (not x['is_dir'], x['name'].lower()))
            return render_template_string(DIRECTORY_TEMPLATE, items=items, path=path)

        # If path is a file, serve it
        directory = os.path.dirname(abs_path)
        filename = os.path.basename(abs_path)
        return send_from_directory(directory, filename)

    except Exception as e:
        app.logger.error(f"Error serving file: {str(e)}")
        abort(404)

@app.errorhandler(404)
def not_found_error(error):
    return "File or directory not found", 404

@app.errorhandler(403)
def forbidden_error(error):
    return "Access forbidden", 403

if __name__ == '__main__':
    app.run(debug=True)
