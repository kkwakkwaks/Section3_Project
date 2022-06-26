import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from category_encoders import TargetEncoder
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

df = pd.read_csv('cat_data.csv')
df = df.drop(['Unnamed: 0'],axis=1)
df['Sex_Upon_Outcome'] = df['Sex upon Outcome']
df = df.drop(['Sex upon Outcome'],axis=1)
df = df.drop(['Age_days'],axis=1)
df = df.drop(['coat_pattern'],axis=1)
train, test = train_test_split(df, test_size=0.2, random_state=2)

target = 'Adopt'
features = train.columns.drop([target])

X_train = train[features]
y_train = train[target]

X_test = test[features]
y_test = test[target]


pipe = make_pipeline(
    TargetEncoder(),
    RandomForestClassifier(random_state=2))

pipe.fit(X_train, y_train)
y_pred = pipe.predict(X_test)
# print(accuracy_score(y_pred,y_test))

with open('model.pkl','wb') as pickle_file:
    pickle.dump(pipe, pickle_file)
