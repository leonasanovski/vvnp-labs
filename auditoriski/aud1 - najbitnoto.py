import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

lista = np.arange(1, 101)
matrix = lista.reshape(10, 10)
# print(matrix)
df = pd.DataFrame(matrix, columns=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
# sea dadovme naziv na kolonite na matricata
print(df)

df = pd.DataFrame({'input': [1, 2, 1, 3], 'output': [1, 0, 1, 1]})
# zadavame na dataframe inputs i soodvetni outputs za niv (ne smee brojot na inputs da e razlicen od outputs)
print(df)

print(df.groupby('input').count)  # gi grupirame inputite vo unikati i broime

# matplotlib

mpl = np.linspace(0, 10, 100)
print(mpl)
figure = plt.figure()
plt.plot(mpl, np.sin(mpl), '-', 'a')
plt.plot(mpl, np.cos(mpl), '--', 'b')
plt.show()
# ova e nacinot na koj sto crtame grafici
# prvo kreirame soodvetno tocki koi se vo range od 0 do 10 i gi ima 100
# potoa pravime scheme za pretstavuvanje na grafik
# prviot grafik e sinusna funkcija koja ke bide so NEisprekinata linija i ke pocnuva od tocka a
# vtoriot grafik e kosinusna funkcija koja ke bide so isprekinata linija i ke pocnuva od tockata b
# na kraj go pretstavuvame grafikot so pomos na plt.show()


func = interpolate.interp1d(mpl, np.sin(mpl), kind='cubic')
plt.figure()
plt.plot(mpl, func(mpl), '--')
