
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import numpy as np
import cv2
from skimage.feature import graycomatrix, graycoprops
from sklearn.ensemble import RandomForestClassifier
import joblib

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load or re-train model (this example assumes model is trained within the script)
def extract_glcm_features(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (128, 128))
    glcm = graycomatrix(image, distances=[1], angles=[0], levels=256, symmetric=True, normed=True)
    contrast = graycoprops(glcm, 'contrast')[0, 0]
    correlation = graycoprops(glcm, 'correlation')[0, 0]
    energy = graycoprops(glcm, 'energy')[0, 0]
    homogeneity = graycoprops(glcm, 'homogeneity')[0, 0]
    return [contrast, correlation, energy, homogeneity]

# Dummy training for demo (in production, load from file)
def train_dummy_model():
    # This simulates training from data
    X = np.random.rand(100, 4)
    y = np.random.randint(2, size=100)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

# model = train_dummy_model()

model = joblib.load('modelNEW.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        if 'image' not in request.files:
            return "No file part"
        file = request.files['image']
        if file.filename == '':
            return "No selected file"
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            features = extract_glcm_features(filepath)
            prediction = model.predict([features])[0]
            result = "TUMOR" if prediction == 1 else "TIDAK TUMOR"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
