import datetime
import csv
mydate = datetime.datetime.now()
with open('inloggers.csv', 'w', newline='') as bestand:
    writer = csv.writer(bestand, delimiter=';')
    writer.writerow(('datum','naam','voorl','gbdatum','email'))


    while True:
        naam = input("Wat is je achternaam? ")
        if naam == "einde":
            break
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")

        writer.writerow((mydate, naam, voorl, gbdatum, email))
