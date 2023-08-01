import os
from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("trained_model.pkl")

# Helper function to predict the species
def predict_species(features):
    species_id = model.predict([features])[0]
    return species_id

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    feature_names = ['Length1', 'Length2', 'Length3', 'Height', 'Width']

    # Ensure the input values are being received correctly
    features = [float(request.form.get(name, 0)) for name in feature_names]
    print("Received features:", features)  # Add this line to check the received features

    # Make sure the model is loaded correctly
    loaded_model = joblib.load("trained_model.pkl")

    # Ensure the model is predicting using the correct feature data
    species_id = loaded_model.predict([features])[0]
    print(species_id)

    # Replace the species_id with actual species names from label_encoder
    label_encoder = {0: 'Bream', 1: 'Parkki', 2: 'Perch', 3: 'Pike', 4: 'Roach', 5: 'Smelt', 6: 'Whitefish'}
    #species_name = label_encoder.get(species_id, 'Unknown')
    species_name = species_id

    return render_template('result.html', species=species_name)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
