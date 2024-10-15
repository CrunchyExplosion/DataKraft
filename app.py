from flask import Flask, render_template, request, send_file, redirect, url_for
import encode
import decode
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hide', methods=['POST'])
def hide_data():
    zip_file = request.files['zip_file']
    
    if zip_file:
        zip_path = os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded.zip')
        zip_file.save(zip_path)

        # Call encoding function from encode.py
        output_image, key = encode.encode(zip_path)
        output_image_path = os.path.join(app.config['UPLOAD_FOLDER'], output_image)

        return render_template('index.html', key=key)
    return 'No file uploaded', 400

@app.route('/decrypt', methods=['POST'])
def decrypt_data():
    image_file = request.files['image_file'] 
    key = request.form['key']
    
    if image_file and key.isdigit():
        key = int(key)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded_image.png')
        image_file.save(image_path)

        # Call decoding function from decode.py
        decode.decode(image_path, key)
        decrypted_path = os.path.join(app.config['UPLOAD_FOLDER'], 'decrypted.zip')

        return send_file(decrypted_path, as_attachment=True)
    return 'Invalid input', 400



if __name__ == '__main__':
    app.run(debug=True)

