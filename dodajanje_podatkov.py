import csv
import random

menjalniki = ["rocni", "avtomatski"]
pogoni = ["elektricni", "bencin", "dizel", "hibridni", "zemeljski plin"]

#with open('podatki/avto.csv', "r+", newline = '') as inputf:
    with open('podatki/avtomobili.csv', "w+", newline = '') as outputf:
        #registrska_tablica,starost,model,barva,menjalnik,pogon,stevilo_sedezev
        reader = csv.reader(inputf)
        writer = csv.writer(outputf)
        for row in reader:
            menjalnik = random.choice(menjalniki)
            pogon = random.choice(pogoni)
            st_sedezev = random.randint(1, 7)
            row.append(menjalnik)
            row.append(pogon)
            row.append(st_sedezev)
            writer.writerow(row)

nov = ["da", "ne"]
barva = ["svetel", "temen", "vseeno"]
model = ["Chrysler", "Dodge", "Chevrolet", "Buick", "Volkswagen", "vseeno"]
pogon = ["elektricni", "bencin", "dizel", "hibridni", "zemeljski plin", "vseeno"]
menjalnik = ["rocni", "avtomatski", "vseeno"]
   
with open('podatki/stranka.csv', "r+", newline = '') as inputf:
    with open('podatki/osebe.csv', "w+", newline = '') as outputf:
        #emso,drzava,starost,barva,najmanjse_st_sedezev,pogon,menjalnik,model
        reader = csv.reader(inputf)
        writer = csv.writer(outputf)
        for row in reader:
            row = row[0:2]
            row.append(random.choice(nov))
            row.append(random.choice(barva))
            row.append(random.randint(1,7)) # najmanjše zahtevano število sedežev
            row.append(random.choices(pogon, weights=[1,1,1,1,1,10], k=1)[0])
            row.append(random.choice(menjalnik))
            row.append(random.choices(model, weights=[1,1,1,1,1,10], k=1)[0])
            writer.writerow(row)
