import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import os

imagini = []

headers = {"Accept-Language": "en-US,en;q=0.5"}
pages = np.arange(1, 10, 1)
for page in pages:
    # print(page)
    page = requests.get("https://www.filarmonicabanatul.ro/index.php/component/jem/event/" + str(page) + "-concert",
                        headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    imagini_spectacol = soup.find('div', class_='jem-description event_desc')
    try:
        imagini = imagini_spectacol.find_all('img')
        for imagine in imagini:
            nume = imagine['alt']
            link = imagine['src']
            link_complet = ("https://www.filarmonicabanatul.ro" + link)
            print(nume, "https://www.filarmonicabanatul.ro" + link)
            with open (nume.replace(' ', '-').replace('/' ,' ' ) + '.jpg', 'wb') as f:
                im = requests.get(link_complet)
                f.write(im.content)

    except AttributeError:
        print("")
