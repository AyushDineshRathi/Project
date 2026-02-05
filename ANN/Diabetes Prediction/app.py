import numpy as np 
from flask import Flask, jsonify, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('ANN\Diabetes Prediction\diabetes_file.pkl', 'rb'))

@app.route("/")
def home():
    return "<h1>hi</h1>"

@app.route("/predict", methods = ['POST'])
def predict():
    features = np.array(request.form.values)
    Outcome = np.round(model.predict(features))
    # return render_template("after.html", prediction_text = "Outcome is {}".format(Outcome))
    return render_template("after.html")

if __name__ == "__main__":
    app.run()