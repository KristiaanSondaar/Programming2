import csv


artikelPrijs  = 0
artikelNaam = ''
voorraad = 0
productnummer = 0
totalVoorraad = 0
with open('producten.csv','r') as productenFile:
    reader = csv.DictReader(productenFile, delimiter=';')
    for row in reader:
        totalVoorraad += int(row['voorraad'])
        if float(row['prijs']) > float(artikelPrijs):
            artikelPrijs = row['prijs']
            artikelNaam = row['naam']
        elif int(voorraad) < int(row['voorraad']):
            voorraad = int(voorraad) + int(row['voorraad'])
            productnummer = row['artikelnummer']


print("Het duurste artikel is", artikelNaam, 'en die kost', artikelPrijs)
print("Er zijn slechts", voorraad, "exemplaren in voorraad van het product met nummer", productnummer)
print(totalVoorraad)