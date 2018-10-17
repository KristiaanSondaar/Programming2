import csv


max = 0
naam = ""
datum = ""
with open('gamers.csv', 'r') as gamersFile:
    reader = csv.reader(gamersFile, delimiter=';')
    for row in reader:
        if int(row[2]) > max:
            naam = row[0]
            datum = row[1]
            max = int(row[2])



print("De hoogste score is:", max, "op", datum, "behaald door", naam)