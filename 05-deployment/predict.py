import pickle
from flask import Flask, request, jsonify

with open('model1.bin', 'rb') as model_file:
    model = pickle.load(model_file)

with open('dv.bin', 'rb') as dv_file:
    dv = pickle.load(dv_file)

app = Flask('Predict')

@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()

    X = dv.transform(client)
    y_probability = model.predict_proba(X)[0, 1]

    y_prediction = y_probability >= 0.5

    result = {
        "probability": float(y_probability),
        "prediction": bool(y_prediction)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=9696)
