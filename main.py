import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

spectacole = []
date = []
locuri = []
categorii = []
hitsuri = []
headers = {"Accept-Language": "en-US,en;q=0.5"}
pages = np.arange(1, 50, 1)
for page in pages:
    # print(page)
    page = requests.get("https://www.filarmonicabanatul.ro/index.php/component/jem/event/" + str(page) + "-concert",
                        headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    spectacol = soup.find('dl', class_='jem-dl')
    try:
        titlu = spectacol.find('dd', class_='jem-title')
        spectacole.append(titlu.text)
        # print(titlu.text)
        data = spectacol.find('dd', class_='jem-when')
        date.append(data.text)
        # print(data.text)
        locul = spectacol.find('dd', class_='jem-where')
        locuri.append(locul.text)
        # print(locul.text)
        categoria = spectacol.find('dd', class_='jem-category')
        categorii.append(categoria.text)
        # print(categoria.text)
        hits = spectacol.find('dd', class_='jem-hits')
        hitsuri.append(hits.text)
        # print(hits.text)
    except AttributeError:
        print("")
# print(spectacole)
# print(date)
# print(locuri)
# print(categorii)
# print(hitsuri)
df = pd.DataFrame({'Spactacole': spectacole,
                   'Date': date,
                   'Sala': locuri,
                   'Categorii': categorii,
                   'Hitsuri': hitsuri,
                   })
# print(df)

df.to_csv('Filarmonica Banatulv2.csv', encoding='utf-8-sig')
