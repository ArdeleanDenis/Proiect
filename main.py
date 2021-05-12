import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

spectacole = []
date = []
locuri = []
categorii = []
hitsuri = []
poze = []
headers = {"Accept-Language": "en-US,en;q=0.5"}
pages = np.arange(1, 29, 1)
for page in pages:
    # print(page)
    page = requests.get("https://www.filarmonicabanatul.ro/index.php/component/jem/event/" + str(page) + "-concert",
                        headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    spectacol = soup.find('dl', class_='jem-dl')
    imagini_spectacol = soup.find('div', class_='jem-description event_desc')
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
        #print(hits.text)
        imagini = imagini_spectacol.find_all('img')
        if imagini:

            for imagine in imagini:
                nume = imagine['alt']
                link = imagine['src']
                link_complet = ("https://www.filarmonicabanatul.ro" + link)
               # print(nume, "https://www.filarmonicabanatul.ro" + link)
                with open (nume.replace(' ', '-').replace('/' ,' ' ) + '.jpg', 'wb') as f:
                    im = requests.get(link_complet)
                    f.write(im.content)
                poze.append(link_complet)
        else:
            poze.append("concertul nu are afis")
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
                   'Poze': poze,
                   })
# print(df)
print(poze)
df.to_csv('Filarmonica Banatulv2.csv', encoding='utf-8-sig')
