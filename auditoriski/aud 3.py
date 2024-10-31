from datetime import date
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from IPython.display import HTML
import matplotlib.pyplot as plt

url = "https://www.setec.mk/"

response = requests.get(url)
raw_html = response.text
soup = BeautifulSoup(raw_html, "html.parser")

codes = []  # sifri
regular_prices = []
happy_prices = []

shifra = soup.select(".shifra")
print(len(shifra))
for i in range(len(shifra)):
    codes.append(shifra[i].text.strip().split()[1])
regular = soup.select(".price-old-new")
for i in range(len(regular)):
    regular_prices.append(regular[i].text.strip().split()[0].replace(',', ''))
regular_prices.append("1000")
new_prices = soup.select(".price-new-new")

for i in range(len(new_prices)):
    happy_prices.append(new_prices[i].text.strip().split()[0].replace(',', ''))
happy_prices.append("700")

final_product = []
for i in range(len(happy_prices)):
    tmp = {"Shifra": codes[i], "Regularna cena": regular_prices[i], "Happy cena": happy_prices[i]}
    final_product.append(tmp)

df = pd.DataFrame(final_product)
df.to_csv("C:/Users/User/Downloads/samo-brojki-setec.csv")
# deka sakam da mi gi gleda kako broevi gi pretvaram vo integeri

df['Shifra'] = pd.to_numeric(df['Shifra'], errors='coerce')
df['Regularna cena'] = pd.to_numeric(df['Regularna cena'], errors='coerce')
df['Happy cena'] = pd.to_numeric(df['Happy cena'], errors='coerce')
print(df.head())
print(df.describe())
print(df.mean())
print(df.min())
print(df.max())
print(df.std())  # standardna devijacija
print("Kvantili")
print(df.quantile([1.00, .25, .5, .75]))
print(df['Regularna cena'].value_counts())  # na value counts mora da mu navedeme sto saka da broi vrednosti

#histogram
df['Shifra'].hist(bins=5)
plt.title("Histogram of 'SHIFRA'")
plt.show()

df.plot.bar()
plt.title("Bar of everything")
plt.show()

df.plot.area()
plt.title("Area of everything")
plt.show()

df.plot.scatter(x='Happy cena', y='Regularna cena')#mora da specificirame x i y
plt.title("Scatter of everything")
plt.show()

plt.plot(df.groupby('Regularna cena').count(),'-b')#gi iscrtuva site ceni kolku pati gi ima
plt.xticks(rotation=90)# gi rotiram vrednostite na oskata
plt.show()

df.boxplot(column='Shifra')
plt.title("Boxplot of Shifra")
plt.show()