import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pickle

dataIris = load_iris()

df = pd.DataFrame(
    dataIris['data'],
    columns= ['SL', 'SW', 'PL', 'PW']
)
df['target'] = dataIris['target']
df['spesies'] = df['target'].apply(
    lambda x: dataIris['target_names'][x]
)

xtr, xts, ytr, yts = train_test_split(df[['SL', 'SW', 'PL', 'PW']], df['spesies'], test_size=.1)

model = LogisticRegression(solver='lbfgs', multi_class='auto', max_iter=10000)
model.fit(xtr, ytr)

with open('modelPickle', 'wb') as modelku:
    pickle.dump(model, modelku)