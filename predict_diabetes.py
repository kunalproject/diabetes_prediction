import sys
import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm

# Use absolute path for CSV file
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'diabetes.csv')

try:
    diabetes_dataset = pd.read_csv(csv_path)
except FileNotFoundError:
    print("Error: diabetes.csv not found at", csv_path)
    sys.exit(1)

X = diabetes_dataset.drop(columns='Outcome', axis=1)
Y = diabetes_dataset['Outcome']

scaler = StandardScaler()
scaler.fit(X)

# Take input data from command-line arguments
try:
    input_data = [float(arg) for arg in sys.argv[1:]]
    input_data_as_numpy_array = np.asarray(input_data).reshape(1, -1)
    std_data = scaler.transform(input_data_as_numpy_array)
    
    # Load model (consider pickle for production)
    classifier = svm.SVC(kernel='linear')
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)
    classifier.fit(X_train, Y_train)
    
    prediction = classifier.predict(std_data)
    print('The person might have diabetes' if prediction[0] == 1 else 'The person might not have diabetes')
except Exception as e:
    print("Prediction error:", str(e))
    sys.exit(1)