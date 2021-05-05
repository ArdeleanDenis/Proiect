from random import randint
from time import sleep
import requests
from requests import get
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
    print(page)
    page = requests.get("https://www.filarmonicabanatul.ro/index.php/component/jem/event/" + str(page) + "-concert",
                        headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    spectacol = soup.find('dl', class='jem-dl')
    titlu = spectacol.find('dd', class='jem-title')
    print(titlu.text)
    data = spectacol.find('dd', class='jem-when')
    print(data.text)
    locul = spectacol.find('dd', class='jem-where')
    print(locul.text)
    categoria = spectacol.find('dd', class='jem-category')
    print(categoria.text)
    hits = spectacol.find('dd', class='jem-hits')
    print(hits.text)
