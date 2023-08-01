# Fish Market Web App

This is a simple Flask web app for predicting the species of a fish based on its features. The app uses a machine learning model trained on the Fish Market dataset to make predictions.

## Getting Started
### Prerequisites
- Python 3.x (3.6 or higher recommended)
- Flask
- scikit-learn
- pandas
- joblib

### Installation

1. Clone the repository:

```
git clone https://github.com/nikhilkoche/ES_Fish_market_dataset.git
```
#### Change directory
```
cd ES_Fish_market_dataset
```

2. Install the required dependencies:

```
pip install requirement.txt
```

## Usage

1. Run the Flask application:

```
python app.py
```


2. Access the application in your web browser at `http://localhost:5000/`.

3. Fill in the features for the fish in the provided form and click "Predict" to get the predicted species.

## Model Training
The machine learning model used in this web app is a Random Forest classifier. It is trained on the Fish Market dataset, which contains features of various fish species.

The training code and data preprocessing can be found in the train_model.ipynb Jupyter Notebook.


# Deployment
This web app is deployed using PythonAnywhere. It is accessible at http://payivel2804.pythonanywhere.com/.

# File Structure
- app.py: Flask web app main script.
- templates/: Folder containing HTML templates for the web app.
- trained_model.pkl: Serialized trained Random Forest classifier.
- fish_market_dataset.csv: Fish Market dataset used for training the model.
- requirements.txt: List of required Python libraries and their versions.
