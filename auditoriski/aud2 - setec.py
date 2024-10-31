import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from IPython.display import HTML

url = "https://www.setec.mk/"

response = requests.get(url)
print(response)
if response.status_code == 200:
    print("Successfully opened the web page")
else:
    print("Failed opening!")
# do tuka sme sigurni deka ja otvara stranicata
# print(response.text)
raw_html = response.text
soup = BeautifulSoup(raw_html, "html.parser")
products_for_test = soup.select('.product')
#ova dole e test za mojot format so sakam da si go postignam
name = soup.select_one('.name').text.strip()
regular_price = soup.select_one('.price-old-new').text
new_price = soup.select_one('.price-new-new').text
code = soup.select_one('.shifra').text.strip().split()[1]
sale = soup.select_one('.sale').text
link = soup.select_one('.image a').get('href')

sorted_out = []
for product in products_for_test:
    name = product.select_one('.name').text.strip()

    regular_price = product.select_one('.price-old-new')
    regular_price = regular_price.text if regular_price else 'N/A'

    new_price = product.select_one('.price-new-new')
    new_price = new_price.text if new_price else 'N/A'

    code = product.select_one('.shifra').text.strip().split()[1]

    sale = product.select_one('.sale')
    sale = sale.text if sale else 'nema popust'

    link = product.select_one('.image a').get('href')
    product_dict = {
        "ProductName": name,
        "ProductCode": code,
        "RegularPrice": regular_price,
        "HappyPrice": new_price,
        "DiscountPercent": sale,
        "PageLink": link,
    }
    sorted_out.append(product_dict)
df = pd.DataFrame(sorted_out)
df.to_csv('C:/Users/User/Downloads/produkti-setec.csv')
print("Minimumot e " + df.min())
print("Maksimumot e " + df.max())

#OVERALL:::
#
#so e celata rabota ustvari
#Znaci prvo barame po klasa so sakame da zimame, posle toa gledame sto tocno ni treba od toj oddel na izdvoeni elementi
#vo nasiot slucaj vlecevme produkti od setec koi bea na soodvetno edna stranica sto ja vklucivme
#Posle toa gi sreduvame produktite, da vidime kakov format sakame da napraime
# i na kraj sekoj od tie produkti go dodavame vo edna lista
#taa lista so DataFrame ja predavame i dobivame kako tabela od produktite so soodvetnite atributi
#na kraj ja zacuvuvam tabelata vo soodvetnata pateka pod soodvetno napisanoto ime kako .csv file odnosno excel tabela
