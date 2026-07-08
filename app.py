import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
NOTES_DIR = os.path.join(os.path.dirname(__file__), 'notes')

if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/notes', methods=['GET'])
def list_notes():
    notes = [f for f in os.listdir(NOTES_DIR) if f.endswith('.md')]
    return jsonify(notes)

@app.route('/api/notes/<filename>', methods=['GET'])
def get_note(filename):
    path = os.path.join(NOTES_DIR, filename)
    if not os.path.exists(path):
        return jsonify({'error': 'Note not found'}), 404
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    return jsonify({'filename': filename, 'content': content})

@app.route('/api/notes', methods=['POST'])
def save_note():
    data = request.json
    filename = data.get('filename')
    content = data.get('content')
    if not filename or content is None:
        return jsonify({'error': 'Invalid data'}), 400
    
    # Validation
    if not filename.endswith('.md'):
        filename += '.md'
    
    path = os.path.join(NOTES_DIR, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    return jsonify({'message': 'Note saved', 'filename': filename})

@app.route('/api/notes/<filename>', methods=['DELETE'])
def delete_note(filename):
    path = os.path.join(NOTES_DIR, filename)
    if os.path.exists(path):
        os.remove(path)
        return jsonify({'message': 'Note deleted'})
    return jsonify({'error': 'Note not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
