from flask import Flask, jsonify, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the model
def load_model():
    global rf
    rf = joblib.load('model.h5')

# Predict function
def make_predictions(data):
    # Define the feature names used in model training
    feature_names = ['age', 'sex', 'motor_UPDRS', 'Jitter(Abs)', 'Shimmer:APQ11', 'Shimmer:DDA', 'HNR', 'RPDE', 'PPE', 'ratio']
    
    # Reorder the columns of the DataFrame based on feature names
    data = data[feature_names]

    predictions = rf.predict(data)
    return predictions

# Load the model on app startup
load_model()

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')


# Route for model prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the request
    form_data = request.form.to_dict(flat=False)

    # Convert the data from JSON to a numpy array
    data = pd.DataFrame(form_data)

    # Make predictions
    predictions = make_predictions(data)

    # Perform severity classification based on total_UPDRS
    total_updrs = predictions[0]
    if total_updrs >= 0 and total_updrs <= 25:
        severity = "Mild severity Parkinson's. The patient is facing minimal functional impairment."
    elif total_updrs > 25 and total_updrs <= 50:
        severity = "Moderate severity Parkinson's. The patient is facing noticeable functional impairment."
    else:
        severity = "Severe detection found. The patient is facing significant impairment in motor function."
    print(form_data)

    form_data['shimmer_dda'] = form_data.pop('Shimmer:DDA')
    form_data['shimmer_apq11'] = form_data.pop('Shimmer:APQ11')
    form_data['jitter_abs'] = form_data.pop('Jitter(Abs)')
    form_data['motor_updrs'] = form_data.pop('motor_UPDRS')
    form_data['hnr'] = form_data.pop('HNR')
    form_data['rpde'] = form_data.pop('RPDE')
    form_data['ppe'] = form_data.pop('PPE')
    form_data['ratio'] = form_data.pop('ratio')
    
    return render_template('index.html', prediction=predictions[0], severity=severity, data= form_data)

if __name__ == '__main__':
    app.run(debug=True)


# if total_updrs is  between 0-25 
# 'mild severity parkinson. patient is facing minimal functional impairment '
# if total_updrs is  between 26-50:
# 'moderate severity parkinson. The patient is facing noticeable functional impairment '
# if total_updrs is  >50 :
# 'severe detection found. patient is facing significant impairment in motor function'