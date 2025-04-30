import sys
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

diabetes_dataset = pd.read_csv('diabetes.csv')

X = diabetes_dataset.drop(columns='Outcome', axis=1)
Y = diabetes_dataset['Outcome']

scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

classifier = svm.SVC(kernel='linear')
classifier.fit(X_train, Y_train)

# Take input data from command-line arguments
input_data = [float(arg) for arg in sys.argv[1:]]
input_data_as_numpy_array = np.asarray(input_data).reshape(1, -1)
std_data = scaler.transform(input_data_as_numpy_array)
prediction = classifier.predict(std_data)
if prediction[0] == 0:
    print('The person might not have diabetes')
else:
    print('The person might have  diabetes')
