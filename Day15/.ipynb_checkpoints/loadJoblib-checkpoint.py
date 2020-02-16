import joblib

model = joblib.load('modelJoblib')

# prediksi SL SW PL PW
print(model.predict([[10, 10, 10, 10]])[0])