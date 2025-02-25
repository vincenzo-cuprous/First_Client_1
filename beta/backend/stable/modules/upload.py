from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# Configure upload folders and allowed extensions
BASE_UPLOAD_FOLDER = 'uploads/books'
PICTURES_FOLDER = os.path.join(BASE_UPLOAD_FOLDER, 'pictures')
DOCUMENTS_FOLDER = os.path.join(BASE_UPLOAD_FOLDER, 'documents')

ALLOWED_PICTURE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
ALLOWED_DOCUMENT_EXTENSIONS = {'txt', 'pdf'}

# Ensure the upload folders exist
os.makedirs(PICTURES_FOLDER, exist_ok=True)
os.makedirs(DOCUMENTS_FOLDER, exist_ok=True)

app.config['PICTURES_FOLDER'] = PICTURES_FOLDER
app.config['DOCUMENTS_FOLDER'] = DOCUMENTS_FOLDER

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
        filename = file.filename
        file.save(os.path.join(app.config['PICTURES_FOLDER'], filename))
        return jsonify({"message": f"Picture '{filename}' uploaded successfully!"}), 200
    
    if file and allowed_document_file(file.filename):
        filename = file.filename
        file.save(os.path.join(app.config['DOCUMENTS_FOLDER'], filename))
        return jsonify({"message": f"Document '{filename}' uploaded successfully!"}), 200
    
    return jsonify({"error": "File type not allowed"}), 400

@app.route('/db/pictures/<path:filename>', methods=['GET'])
def get_picture(filename):
    return send_from_directory(app.config['PICTURES_FOLDER'], filename)

@app.route('/db/documents/<path:filename>', methods=['GET'])
def get_document(filename):
    return send_from_directory(app.config['DOCUMENTS_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
