import bs4
import requests

cere = requests.get('https://www.filarmonicabanatul.ro')        #facem o variabila care face un request catre site pentru a extrage date

supa = bs4.BeautifulSoup(cere.text, 'lxml')     #convertim variabila din request in beautiful soup 
hi = supa.select('.hasTooltip')         #selectam toate obiectele din cadrul clasei
print(hi)
for i in supa.select('.hasTooltip'):        #filtram doar elementele din subclasa a prin care putem afla titlul evenimentului si data(ziua)
    print(i.a)
