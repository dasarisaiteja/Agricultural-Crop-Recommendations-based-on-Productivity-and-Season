# Importing essential libraries
from flask import Flask, render_template, request
import numpy as np
import os
import pickle

# Initialize Flask app
app = Flask(__name__)

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load ML model (correct way)
model_path = os.path.join(BASE_DIR, 'models', 'RandomForest.pkl')
crop_recommendation_model = pickle.load(open(model_path, 'rb'))

# ================= ROUTES ================= #

# Home page
@app.route('/')
@app.route('/index')
def home():
    title = 'Crop Recommendation'
    return render_template('index.html', title=title)

# Crop recommendation form page
@app.route('/crop-recommend')
def crop_recommend():
    title = 'Crop Recommendation'
    return render_template('crop.html', title=title)

# Crop prediction
@app.route('/crop-predict', methods=['POST'])
def crop_prediction():
    title = 'Crop Recommendation'

    if request.method == 'POST':
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['pottasium'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        # Prepare data
        data = np.array([[N, P, K, (N+P), (N+K), ph, rainfall]])

        # Prediction
        prediction = crop_recommendation_model.predict(data)[0]

        return render_template(
            'crop-result.html',
            prediction=prediction,
            title=title
        )

# ================= RUN APP ================= #

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)