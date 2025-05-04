import os
import uuid
import cv2
import base64
from flask import Flask, render_template, request, redirect, url_for, flash
from face_recognition import faceRecognitionPipeline

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max
UPLOAD_FOLDER = 'static/uploads'
RESULT_FOLDER = 'static/results'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'mp4', 'avi'}

# Ensure necessary folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Index route (homepage)
@app.route('/')
def index():
    return render_template('index.html')

# Gender recognition route
@app.route('/gender', methods=['GET', 'POST'])
def gender():
    result = None
    predictions = None

    if request.method == 'POST':
        # Process webcam capture form submission
        if 'image_data' in request.form and request.form['image_data']:
            data_url = request.form['image_data']
            # Data URL format: "data:image/png;base64,..."
            header, encoded = data_url.split(',', 1)
            image_data = base64.b64decode(encoded)
            filename = f"{uuid.uuid4()}.png"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            with open(filepath, 'wb') as f:
                f.write(image_data)
            # Process the captured image
            processed_img, predictions = faceRecognitionPipeline(filepath, path=True)
            result_filename = f"result_{filename}"
            result_filepath = os.path.join(app.config['RESULT_FOLDER'], result_filename)
            cv2.imwrite(result_filepath, processed_img)
            result = result_filename

        # Process file upload form submission
        elif 'file' in request.files:
            file = request.files['file']
            if file.filename == '':
                flash('No file selected.')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                ext = file.filename.rsplit('.', 1)[1].lower()
                filename = f"{uuid.uuid4()}.{ext}"
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                if ext in ['png', 'jpg', 'jpeg']:
                    processed_img, predictions = faceRecognitionPipeline(filepath, path=True)
                    result_filename = f"result_{filename}"
                    result_filepath = os.path.join(app.config['RESULT_FOLDER'], result_filename)
                    cv2.imwrite(result_filepath, processed_img)
                    result = result_filename
                elif ext in ['mp4', 'avi']:
                    cap = cv2.VideoCapture(filepath)
                    ret, frame = cap.read()
                    cap.release()
                    if ret:
                        temp_img_path = os.path.join(app.config['UPLOAD_FOLDER'], f"temp_{filename}.jpg")
                        cv2.imwrite(temp_img_path, frame)
                        processed_img, predictions = faceRecognitionPipeline(temp_img_path, path=True)
                        result_filename = f"result_{filename}.jpg"
                        result_filepath = os.path.join(app.config['RESULT_FOLDER'], result_filename)
                        cv2.imwrite(result_filepath, processed_img)
                        result = result_filename
                        os.remove(temp_img_path)
                    else:
                        flash('Could not read the video file.')
                        return redirect(request.url)
    return render_template('gender.html', result=result, predictions=predictions)

if __name__ == '__main__':
    app.run(debug=True)
