import numpy as np 
import pickle
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

model = pickle.load(open('ANN\Bank_TurnOver_Churn_Prediction\ModelBank.pkl', 'rb'))

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict")
def predict():
    features = np.array(request.form.values)
    

if __name__ == "__main__":
    app.run()