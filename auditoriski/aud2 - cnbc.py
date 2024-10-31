from datetime import date
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from IPython.display import HTML

url = "https://www.cnbc.com/finance/"

# prvo ova da go napraam posle toa da ja izgleam 3tata
response = requests.get(url)

raw_html = response.text
soup = BeautifulSoup(raw_html, "html.parser")
# gi zemame naslovite na vestite
card_titles = soup.select(".Card-title")
titles = []
for card_title in card_titles:
    titles.append(card_title.text)
# gi imame naslovite sea

# gi zemame vreminjata koga bile objaveni soodvetnite vesti
card_time = soup.select('.Card-time')
times = []
for card_time in card_time:
    times.append(date.today().strftime("%a, %b %d %Y")) if 'ago' in card_time.text else times.append(card_time.text)
# gi stavame site vo edna lista kade se formatirani soodvetno po datumi

# gi zemame site kategorii na vestite
card_classes = soup.select('.Card-eyebrow')
classes_of_news = []
for i in range(len(times)):
    classes_of_news.append("Top news!") if i < 6 else classes_of_news.append(card_classes[i - 6].select_one('div').text)
    i += 1
# site gi stavame vo listata, kade prvite vesti se top news za da moze da ima ednakov broj na vesti so naslovi i vreminja soodvetno
final_version = []
for i in range(len(titles)):
    tmp = {"Title": titles[i], "Time": times[i], "Class": classes_of_news[i]}
    final_version.append(tmp)
df = pd.DataFrame(final_version)

# print(df[df['Class'] == "Top news!"])
print(df.median)
