import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow import keras
import pickle

df = pd.read_csv(r'ANN\Diabetes Prediction\diabetes.csv')

X = df.drop("Outcome", axis = 1)
y = df.Outcome

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

model = keras.Sequential([
    keras.layers.Dense(8, input_shape = (8, ), activation='relu'),
    keras.layers.Dense(4, activation='relu'),
    keras.layers.Dense(2, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

model.compile(
    optimizer = 'adam',
    loss = 'binary_crossentropy',
    metrics = ['accuracy']
)

model.fit(X_train, y_train, epochs = 100)

pickle.dump(model, open('ANN\Diabetes Prediction\diabetes_file.pkl', 'wb'))