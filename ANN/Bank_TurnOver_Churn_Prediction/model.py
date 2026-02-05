import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
import pickle

df = pd.read_csv(r'ANN/Bank_TurnOver_Churn_Prediction/Churn_Modelling.csv')

df.drop(columns=['RowNumber', 'CustomerId', 'Surname'], inplace = True)
df['Gender'] = df['Gender'].map({'Female': 0, 'Male': 1})

df1 = pd.get_dummies(data=df, columns=['Geography'], drop_first=True)

X = df1.drop(['Exited'], axis='columns')
y = df1['Exited']

scaler = MinMaxScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

model = keras.Sequential([
    keras.layers.Dense(12, input_shape=(X_train.shape[1],), activation='relu'),
    keras.layers.Dense(6, activation='relu'),
    keras.layers.Dense(3, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', 
              loss='binary_crossentropy', 
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=50, batch_size=32, verbose=1)

pickle.dump(model, open('ANN\Bank_TurnOver_Churn_Prediction\ModelBank.pkl', 'wb'))