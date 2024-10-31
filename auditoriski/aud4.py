import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

dataset = pd.read_csv('C:Users/User/Downloads/spaceship_titanic.csv')

print(dataset.head())
print(dataset.info())

print(dataset.isnull().sum())  # ke isprinta brojot na prazni polinja za sekoja klasa
# mozeme i na nekoja klasa posebno
print("Za spa nemaat vrednosti vkupno " + str(dataset['Spa'].isnull().sum()) + " redici!")

print(dataset[['Spa', 'Name']].isnull().sum())  # tuka soodvetno za n kategorii (vo mojot slucaj n=2)

# da ja vidime ratata na falenje na vrednost
missing_rate = dataset.isnull().sum() / len(dataset) * 100
print(missing_rate)

# so stubovi, kade sto vo zavisnost od visinata na stubot - ima ratata na postoenje na vrednost
msno.bar(dataset)
plt.show()

# izglea nesto kako barkodovi, kaj sto belite boi se propustite na vrednosti
msno.matrix(dataset)  # default color
plt.show()
msno.matrix(dataset, color=(0.24, 0.45, 0.87))  # bojata se stava vo torka od 3 vrednosti (r,g,b)
plt.show()

msno.matrix(dataset.sort_values('VIP'))
plt.show()

# sea so heat map
msno.heatmap(dataset)
plt.show()

# dendogram so preklop na kocki - koj e pogolem stolb toj ima najgolema missing rate na informacija
msno.dendrogram(dataset)
plt.show()

# eden od nacinite da se spravime so ova e da go izbriseme toj primerok (dropame red)
new_dataset = dataset.dropna(subset=['Cabin'])
new_missing_rate = (new_dataset.isnull().sum() / len(dataset)) * 100
print("Old missing rate for Cabin: " + str(missing_rate['Cabin']))
print("New missing rate for Cabin: " + str(new_missing_rate['Cabin']))

# moze da se dropne i cela kolona
newest_dataset = dataset.drop(columns='Cabin')
print(newest_dataset.info())  # ke ja nema veke taa kolona Cabin

# Vtoriot nacin osven brisenje na koloni e da se dodava nova vrednost (0 ili sredna vrednost na prazna vrednost)

# NACIN 1 : STAVANJE SEKADE 0
# prvo mora da ja kreirame taa vrednost
constant_imputer = SimpleImputer(strategy='constant',
                                 fill_value=0)  # ke nadopolnuva so konstanta cija vrednost iznesuva 0
print(dataset.head(10))
# 7     0006_02      Earth      True  ...    NaN  Candra Jacostaffey         True, ima NaN za VRDeck
# sea ke staime na toa mesto da ima 0
dataset['VRDeck'] = constant_imputer.fit_transform(dataset[['VRDeck']])
print(dataset.head(10))
# 7     0006_02      Earth      True  ...    0.0  Candra Jacostaffey         True

# NACIN 2 : STAVANJE SEKADE 'MOST FREQUENT VALUE'
print(dataset['HomePlanet'].isnull().sum())
most_freq_imputer = SimpleImputer(strategy='most_frequent')
dataset['HomePlanet'] = most_freq_imputer.fit_transform(
    dataset[['HomePlanet']]).ravel()  # .ravel ke pretvori od 2d arrat vo 1d array
print(dataset.isnull().sum())

# NACIN 3 : STAVANJE SEKADE SREDNA VREDNOST OD KATEGORIJATA (vo mojot primer e Age)
dataset.Age.plot.hist()
plt.show()
age_mean = dataset['Age'].mean()
dataset['Age'] = dataset['Age'].fillna(age_mean)
print(dataset.isnull().sum())

dataset.ShoppingMall.plot.hist()
plt.show()
print(dataset.ShoppingMall.mean())
print(dataset.ShoppingMall.median())
dataset['ShoppingMall'] = dataset['ShoppingMall'].fillna(dataset.ShoppingMall.median())
print(dataset.isnull().sum())

scaler = MinMaxScaler()  # kreirame skaler za podatoci
scaled_data = scaler.fit_transform(
    dataset[['FoodCourt', 'Spa']])  # FoodCourt i Spa podatocite gi skalirame i gi smestuvame vo promenliva
# ustvari, dobivaat vrednosti megju 0 i 1 site podatoci
knn_imputer = KNNImputer(n_neighbors=5)  # knn so n=5
# For each missing value, it calculates the mean (or weighted average) of the nearest 5 neighboring points (rows) based on Euclidean distance.
imputed_data = knn_imputer.fit_transform(scaled_data)  # popolnuvame vrz baza na rezultatite od KNN scaler
print(imputed_data)
imputed_data = scaler.inverse_transform(imputed_data)  # sega ke vrati od [0,1] vo normalni vrednosti
dataset[['FoodCourt', 'Spa']] = imputed_data  # sega se e skalirano
print(dataset.isnull().sum())

# NE ZABORAVAJ LEONE:
# 1.kreirame scaler
# 2.zemame podatoci sto ke gi skalirame
# 3.kreirame knn_imputer koj ke go podesime kolku sosedi da gleda
# 4.novata imputed_data ja pravime taka sto vo knn_imputerot gi fitnuvame podatocite za skaliranje
# 5.ja vrakjame so scalerot nazad vo prvobitna forma, vo normalni broevi, ne samo od 1 do 0
# 6.predavame vrednosti na mnozestvoto soodvetno novite
# sreden problem

dataset1 = pd.read_csv('C:Users/User/Downloads/air_quality_missing.csv')

print(dataset1.isnull().sum())
dataset1['NO2'] = dataset1['NO2'].bfill()  # backtrackfill - vo zavisnost od poslednoto vo nizata
dataset1['CO'] = dataset1['CO'].ffill()  # forwardfill - vo zavisnost od prvoto vo nizata
# For a series like [1, NaN, NaN, 4]:
# ffill would result in [1, 1, 1, 4]
# bfill would result in [1, 4, 4, 4]

print(dataset1.isnull().sum())
dataset1.PM10.plot.line()
plt.show()
dataset1['PM10'] = dataset1['PM10'].interpolate(limit_direction='both')
# so ova ke popolnuva vrednosti linearno opagjacki ili zgolemuvacki
# For aq_data['PM10'] = [10, NaN, 30, NaN, 50], a linear interpolation would give:
# [10, 20, 30, 40, 50]
print(dataset1.isnull().sum())

# sega ke pretvorime tekst vo vrednost
txt_to_numeric_encoder = LabelEncoder()
encoded_data = txt_to_numeric_encoder.fit_transform(dataset['HomePlanet'])
dataset['HomePlanet-Encoded'] = encoded_data
print(dataset.tail(5))

#si pravam moja funkcija koja ke dava vrednosti numericki, novi
def custom_function(x):
    x = pd.to_numeric(x)
    if x % 2 == 0:
        return x / 2 * 0.43
    else:
        return x / 3 * 0.34


dataset['Custom-Age-Encoded'] = dataset['Age'].apply(custom_function)
print(dataset.tail(5))

#OneHot e metoda za kastiranje ama pravi kolona od sekoja vrednost vo kategorijata
one_hot = pd.get_dummies(dataset['Destination'])
dataset = pd.concat([dataset, one_hot])
print(dataset.info())