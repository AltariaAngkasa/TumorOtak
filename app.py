from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from PIL import Image
import numpy as np
import joblib
import cv2
from skimage.feature import graycomatrix, graycoprops

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Muat model
model = joblib.load('modelNEW.pkl')

# Ekstraksi fitur GLCM
def extract_glcm_features(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (128, 128))
    glcm = graycomatrix(image, distances=[1], angles=[0], levels=256, symmetric=True, normed=True)
    contrast = graycoprops(glcm, 'contrast')[0, 0]
    correlation = graycoprops(glcm, 'correlation')[0, 0]
    energy = graycoprops(glcm, 'energy')[0, 0]
    homogeneity = graycoprops(glcm, 'homogeneity')[0, 0]
    return [contrast, correlation, energy, homogeneity]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    print(">>> MENERIMA POST KE /predict <<<")
    if 'image' not in request.files:
        print(">>> Tidak ada 'image' dalam request.files <<<")
        return redirect(url_for('index'))

    file = request.files['image']
    print(">>> File diterima:", file.filename)
    if file.filename == '':
        print(">>> Nama file kosong <<<")
        return redirect(url_for('index'))

    if file:
        print(">>> File valid, lanjut proses GLCM dan prediksi <<<")
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        # Ekstrak fitur dari gambar
        features = extract_glcm_features(filepath)
        prediction = model.predict([features])[0]

        result = "Tumor Terdeteksi" if prediction == 1 else "Tidak Ada Tumor"
        image_url = url_for('static', filename=f'uploads/{filename}')
        return render_template('index.html', result=result, image_url=image_url)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
