from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods = ['POST', 'GET'])
def predict():
    if request.method == 'POST':
        input = request.form
        # print(input)    # ImmutableMultiDict([('sl', '1'), ('sw', '2'), ('pl', '3'), ('pw', '4')])
        prediksi = model.predict([[
            float(input['sl']), float(input['sw']),
            float(input['pl']), float(input['pw'])
        ]])[0]
        return render_template('predict.html',
            data=input, pred=prediksi)

if __name__ == '__main__':
    model = joblib.load('modelJoblib')
    app.run(debug=True)