"""
Classification predicts categorical label or class
Regression predict numerical values
"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.tree import DecisionTreeClassifier
# LINEAR REGRESSION

df = pd.read_csv("advertising.csv")
print(df.head())

sns.pairplot(df)
# plt.show()

print(df.isnull().sum())
# no null values

X = df.iloc[:, :-1]  # Features
Y = df["Sales"]  # Target valuable
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
"""
As X set it selects all the rows and all the columns except the last one. Actually it selects TV Radio Newspaper all rows, without selecting the column Sales
As Y it selects the target column, that is Sales
Test size = 20%
Train test = 80%
"""
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)  # here from the train we are fitting the scaler
x_test = scaler.transform(x_test)  # we transform the test values too based on the fitting
# With the scaler we are achieving getting only values between 0 and 1
# , but only for the training set. We don't want to transform the test set,
# because it won't get us the right calculations

model = LinearRegression()
model.fit(x_train, y_train)

print(f"Koeficientite dobieni od klasite - {model.coef_}")
# sales_formula = model.coef_[0]*TV + model.coef_[1]*Radio + model.coef_[2]*Newspaper + model.intercept_

y_pred = model.predict(x_test)
print(y_pred)
# r-squared shows how well the data fit the regression model
print(f"R-squared = {r2_score(y_test, y_pred)}")
print(f"Mean absolute error = {mean_absolute_error(y_test, y_pred)}")
