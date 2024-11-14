"""
Classification predicts categorical label or class
Regression predict numerical values
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from sklearn.naive_bayes import GaussianNB

data = pd.read_csv("user_behavior_dataset.csv")

# E sea deka imame vrednosti koi se tekst, ke gi enkodirame vo numericki vrednosti

encoder = LabelEncoder()
print(data["Gender"][:5])
data["Gender"] = encoder.fit_transform(data["Gender"])
print(data["Gender"][:5])

print(data["Operating System"][:5])
data["Operating System"] = encoder.fit_transform(data["Operating System"])
print(data["Operating System"][:5])

print(data["Device Model"][:5])
data["Device Model"] = encoder.fit_transform(data["Device Model"])
print(data["Device Model"][:5])

x = data.drop(["User Behavior Class"], axis=1)
y = data["User Behavior Class"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
model = GaussianNB()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print(f"f1 score micro - {f1_score(y_test, y_pred, average='micro')}")  # f statistic mikro i makro
print(f"f1 score macro - {f1_score(y_test, y_pred, average='macro')}")
print(f"Accuracy score - {accuracy_score(y_test, y_pred)}")  # rata na tocnost
