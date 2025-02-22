from flask import Flask, send_from_directory, render_template_string, abort
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
SERVE_DIRECTORY = "db"  # Directory to serve files from
ALLOWED_EXTENSIONS = None  # Allow all extensions

# Create the serve directory if it doesn't exist
if not os.path.exists(SERVE_DIRECTORY):
    os.makedirs(SERVE_DIRECTORY)

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
    app.run(debug=True, host='localhost', port=5000)
