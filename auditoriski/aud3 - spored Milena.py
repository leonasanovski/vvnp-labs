import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

data = pd.read_csv('C:Users/User/Downloads/heart.csv')

print(data.head())
print(
    data.describe())  # presmetuva min,max,standardna devijacija,goren dolen kvantil, medijana, sredna vrednost, suma,broj
print(data.info())
print(data['age'].quantile([0.25, 0.5, 0.75, 1.00]))  # kvantilite rabotat samo so brojki

# HISTOGRAMI
plt.figure(figsize=(20, 10))
plt.hist(data['trestbps'], bins=15)
plt.show()

plt.figure(figsize=(20, 10))
plt.hist(data['chol'], bins=15)  # daj mi gi site vrednosti od 100 do 200 vo kategorija chol
plt.show()
# vaka ke gi plotne i dvata na ist histogram
plt.figure(figsize=(20, 10))
plt.hist(data['trestbps'], bins=15)
plt.hist(data['chol'], bins=15)  # daj mi gi site vrednosti od 100 do 200 vo kategorija chol
plt.show()

# Histogram so kriva na nego
sns.displot(data['trestbps'], kde=True, bins=15)  # ke ni dade histogram so prava, ako kde=True
plt.show()

print(data[['cp', 'age', 'trestbps']])  # printam specificni kategorii samo

cp_age_mean = data.groupby('cp')['age'].mean()
# presmetuva prosek na godini za site mozni vrednosti koi se vo kategorijata cp
# Da pojasnam: gleda za cp = 0 kolku godini ima i ke gi sobere i ke gi podeli so broj na godini
# posle gleda za cp = 1, cp = 2 i cp = 3
print(cp_age_mean)
# za da gi izbroi cp = 0/1/2/3
print(data.groupby('cp').size())
print(data.groupby('age').size())
# BAR plotting
plt.bar(data['cp'].value_counts().index, data.groupby('cp').size(), color='violet')
plt.xlabel('vrednosti vo cp-klasata')
plt.ylabel('broj na elementi od vrednost vo cp-klasata')
plt.title('BAR diagram for cp class')
plt.show()

print(data.groupby('restecg').size())
data.restecg.value_counts().plot.bar()  # kratok nacin kako da nacrtas nesto, se vo edna linija
plt.show()

# Box plot

plt.boxplot(data['age'])
plt.show()

sns.boxplot(data=data, x='target', y='chol',
            hue='target')  # ke plotira od data mnozestvoto, x ke zeme target a y chol i bojata ke ja dava spored target
plt.show()

# linii plotiranje
data = data.sort_values('age')
plt.plot(data['age'], data['chol'])
plt.show()

# sega ke grupirame po godini i ke kalkulirame mediana na chol
a = data.groupby('age')['chol'].mean()
plt.plot(a)
plt.show()

# scatter plot - so tocki
sns.scatterplot(data=data, x='cp', y='age', hue='cp')  # ke se orientira spored cp
plt.show()

