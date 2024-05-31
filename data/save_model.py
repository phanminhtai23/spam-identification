# import csv
from joblib import dump
import pandas as pd
import openml
from sklearn.ensemble import RandomForestClassifier
# from sklearn.datasets import load_iris, load_wine,load_digits, load_breast_cancer
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

import matplotlib.pyplot as plt

dataset = openml.datasets.get_dataset(
    44, download_data=bool, download_qualities=bool, download_features_meta_data=bool)

X, y, _, _ = dataset.get_data(target=dataset.default_target_attribute)

X_encoded = pd.get_dummies(X)

X_Train, X_Test, Y_Train, Y_Test = train_test_split(
            X, y, test_size=1/3, random_state=20)

rf_model = RandomForestClassifier(n_estimators = 100, max_features ='log2', max_depth = 17, random_state=42)

rf_model.fit(X_Train, Y_Train)
print("X", X.columns)
dump(rf_model, 'Random_Forest.joblib')
Y_Pred = rf_model.predict(X_Test)

# report = classification_report(Y_Test, Y_Pred, zero_division=0.0)

Acc = accuracy_score(Y_Pred, Y_Test)*100
P = precision_score(Y_Pred, Y_Test, average="weighted")*100
R = recall_score(Y_Pred, Y_Test, average="weighted")*100
F1 = f1_score(Y_Pred, Y_Test, average="weighted")*100

print("------------------------")
print("Accuracy: ", Acc)
print("F1:    ", F1)
print("Precision:  ", P)
print("Recall:     ", R)

print("len Y_test: ", len(Y_Test))

#in 10 dòng dữ liệu test để thử mô hình trên web
print("First 10 rows of Y_Test:")
print(Y_Test.head(10))
print("First 10 rows of X_Test:")
print(X_Test.head(10))

