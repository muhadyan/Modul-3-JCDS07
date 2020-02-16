from flask import Flask, jsonify, request
import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome Home'

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        body = request.json     # sl sw pl pw
        sl = body['sl']; sw = body['sw']
        pl = body['pl']; pw = body['pw']
        data = {
            'sl': sl, 'sw': sw, 'pl': pl, 'pw': pw,
            'zprediksi': model.predict([[sl, sw, pl, pw]])[0]
        }
        return jsonify(data)
    else:
        return 'Mustinya Anda nge-POST'

if __name__ == '__main__':
    model = joblib.load('modelJoblib')
    app.run(debug=True, port=2020)