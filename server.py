from flask import Flask, request, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        uploaded_file = request.files['file']

        if uploaded_file:
            file_path = os.path.join('uploads', uploaded_file.filename)
            uploaded_file.save(file_path)
            return jsonify({'success': True, 'message': 'File uploaded successfully'})

        return jsonify({'success': False, 'message': 'No file uploaded'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')

    app.run(debug=True)
