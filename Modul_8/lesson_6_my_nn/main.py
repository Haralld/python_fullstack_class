from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import os
from PIL import Image
import tensorflow as tf
import numpy as np
import base64
from io import BytesIO

app = Flask(__name__)

model = tf.keras.models.load_model("my_flowers_model.h5")
class_names = ['ромашка', 'одуванчик', 'роза', 'подсолнух', 'тюльпан']

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        img = Image.open(filepath).resize((180, 180))
        img_array = tf.keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)
        predictions = model.predict(img_array)
        score = tf.nn.softmax(predictions[0])

        result = {
            'class': class_names[np.argmax(score)],
            'probability': 100 * np.max(score),
            'image': get_base64_image(img)
        }

        return render_template('index.html', result=result, filename=filename)


def get_base64_image(image):
    buffered = BytesIO()
    image.save(buffered, format='JPEG')
    return base64.b64encode(buffered.getvalue()).decode('utf-8')


if __name__ == '__main__':
    app.run(debug=True)
