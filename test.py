import joblib
import pandas as pd

# Load the model
rf = joblib.load('model.h5')

# Prepare the new data for prediction
new_data = pd.DataFrame({
    'age': [60],
    'sex': [1],
    'motor_UPDRS': [23.5],
    'Jitter(Abs)': [0.03],
    'Shimmer:APQ11': [0.012],
    'Shimmer:DDA': [0.045],
    'HNR': [21.3],
    'RPDE': [0.58],
    'PPE': [0.28],
    'ratio': [0.9]
})

# Make predictions on the new data
predictions = rf.predict(new_data)

# Print the predictions
print(predictions)
