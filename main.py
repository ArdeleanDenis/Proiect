import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
from tkinter import *

spectacole = []
date = []
locuri = []
categorii = []
poze = []
headers = {"Accept-Language": "en-US,en;q=0.5"}
pages = 1
ok = 0
k = 0
k2 = 0
while k < 5:
    # print(page)
    page = requests.get("https://www.filarmonicabanatul.ro/index.php/component/jem/event/" + str(pages) + "-concert",
                        headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    spectacol = soup.find('dl', class_='jem-dl')
    imagini_spectacol = soup.find('div', class_='jem-description event_desc')
    try:
        titlu = spectacol.find('dd', class_='jem-title')
        if titlu:
            spectacole.append(titlu.text)
        else:
            spectacole.append("Concertul nu are titlu")
#        print(titlu.text)
        data = spectacol.find('dd', class_='jem-when')
        if data:
            date.append(data.text)
        else:
            date.append("Concertul nu are data")
#        print(data.text)
        locul = spectacol.find('dd', class_='jem-where')
        if locul:
            locuri.append(locul.text)
        else:
            locuri.append("Concertul nu are sala")
#        print(locul.text)
        categoria = spectacol.find('dd', class_='jem-category')
        if categoria:
            categorii.append(categoria.text)
        else:
            categorii.append("Concertul nu are categorie")
#        print(categoria.text)

        k2 += 1
#        print(k2)
        if k2 == 24 or k2 == 25 or k2 == 26:
            poze.append("Concertul nu are afis")

        imagini = imagini_spectacol.find_all('img')

        if imagini:

            for imagine in imagini:
                nume = imagine['alt']
                link = imagine['src']
                link_complet = ("https://www.filarmonicabanatul.ro" + link)
#                print(nume, "https://www.filarmonicabanatul.ro" + link)
                with open(nume.replace(' ', '-').replace('/', ' ') + '.jpg', 'wb') as f:
                    im = requests.get(link_complet)
                    f.write(im.content)
                poze.append(link_complet)

        else:
            poze.append("Concertul nu are afis")
        ok = 0
        k = 0
    except AttributeError:
        #       print(".")
        ok = 1
    if ok == 1:
        k += 1
    #       print(k)
    pages += 1
# print(spectacole)
# print(date)
# print(locuri)
# print(categorii)

df = pd.DataFrame({'Spactacole': spectacole,
                   'Date': date,
                   'Sala': locuri,
                   'Categorii': categorii,
                   'Poze': poze,
                   })

df.to_csv('Filarmonica Banatulv2.csv', encoding='utf-8-sig')

filepath = '/Users/bumba/Desktop/Proiectfin/Filarmonica Banatulv2.csv'

File = open(filepath)
Reader = csv.reader(File)
Data = list(Reader)
del (Data[0])

list_of_entries = []
for x in list(range(0, len(Data))):
    list_of_entries.append(Data[x][2])

root = Tk()
root.geometry('800x500')
var = StringVar(value=list_of_entries)
listbox1 = Listbox(root,width=30, height=20, listvariable=var)
listbox1.grid(row=0, column=0)


def Eveniment():
    index = listbox1.curselection()[0]
    spectacollabel2.config(text=Data[index][1])
    datelabel2.config(text=Data[index][2])
    salalabel2.config(text=Data[index][3])
    categorielabel2.config(text=Data[index][4])
    pozelabel2.config(text=Data[index][5])

    return None

button1 = Button(root, text="Eveniment", command=Eveniment)
button1.grid(row=6, column=0)

spectacollabel = Label(root, text="Spectacole").grid(row=1, column=0, sticky="w")
datelabel = Label(root, text="Date").grid(row=2, column=0, sticky="w")
salalabel = Label(root, text="Sala").grid(row=3, column=0, sticky="w")
categorielabel = Label(root, text="Categorii").grid(row=4, column=0, sticky="w")
pozelabel = Label(root, text="Poze").grid(row=5, column=0, sticky="w")

spectacollabel2 = Label(root, text="")
spectacollabel2.grid(row=1, column=1, sticky="w")
datelabel2 = Label(root, text="")
datelabel2.grid(row=2, column=1, sticky="w")
salalabel2 = Label(root, text="")
salalabel2.grid(row=3, column=1, sticky="w")
categorielabel2 = Label(root, text="")
categorielabel2.grid(row=4, column=1, sticky="w")
pozelabel2 = Label(root, text="")
pozelabel2.grid(row=5, column=1, sticky="w")

root.mainloop()
