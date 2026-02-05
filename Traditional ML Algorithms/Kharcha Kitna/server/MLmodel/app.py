from flask import Flask, request, jsonify, send_from_directory
import numpy as np
import pickle

# Load the model
loaded_model = pickle.load(open('static/trained_models.sav', 'rb'))

app = Flask(__name__)

def monthlyexp_prediction(input_data):
    new_data = np.array(input_data).reshape(1, -1)
    pred = loaded_model.predict(new_data)
    return str(pred[0])  # Return the prediction as a string

@app.route('/')
def home():
    try:
        return send_from_directory('static', 'server.js')  # Serve static file
    except FileNotFoundError:
        return "File not found", 404

@app.route('/', methods=['POST'])
def submit():
    try:
        # Retrieve and convert form data to float
        data1 = float(request.form['a'])
        data2 = float(request.form['b'])
        data3 = float(request.form['c'])
        data4 = float(request.form['d'])
        data5 = float(request.form['e'])
    except (KeyError, ValueError) as e:
        return jsonify(error=str(e)), 400

    # Prepare the data array
    arr = [data1, data2, data3, data4, data5]
    
    # Get the prediction
    prediction = monthlyexp_prediction(arr)
    
    # Return the prediction as a JSON response
    return jsonify(prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True) 