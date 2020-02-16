import pickle

with open('modelPickle', 'rb') as modelku:
    model = pickle.load(modelku)

# prediksi SL SW PL PW
print(model.predict([[10, 10, 10, 10]])[0])