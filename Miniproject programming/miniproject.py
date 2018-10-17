import csv

def terugomzettenASCII(omgezetteWaarde):
    lijst = list(omgezetteWaarde)
    i = 0
    omgezetteWaarde = []
    for letter in lijst:
        ASCII = ord(lijst[i]) + 3
        CHAR = chr(ASCII)
        omgezetteWaarde.append(CHAR)
        i += 1
    zin = ''.join(omgezetteWaarde)
    return zin

def omzettenASCII(omzetWaarde):
    lijst = list(omzetWaarde)
    i = 0
    omgezetteWaarde = []
    for letter in lijst:
        ASCII = ord(lijst[i]) - 3
        CHAR = chr(ASCII)
        omgezetteWaarde.append(CHAR)
        i += 1
    zin = ''.join(omgezetteWaarde)
    return zin




def opslaanRegistratienummer():
    with open('stalling.csv', 'r', newline='') as myCSVFile:
        reader = csv.DictReader(myCSVFile, delimiter=',')
        registratienummer = []
        wachtwoorden = []
        for row in reader:
            omgezet = terugomzettenASCII(row['uhjlvwudwlhqxpphu'])
            wachtwoordOmgezet = terugomzettenASCII(row['t^`eqtlloa'])
            registratienummer.append(omgezet)
            wachtwoorden.append(wachtwoordOmgezet)
        return registratienummer, wachtwoorden

def ophalen():
    registratienummers, wachtwoorden = opslaanRegistratienummer()
    while True:
        invoerRegistratienummer = input("Geef alstublieft uw registratienummer: ")
        if invoerRegistratienummer in registratienummers:
            while True:
                indexRegistratienummer = registratienummers.index(invoerRegistratienummer)
                invoerWachtwoord = input("Geef alstublief uw wachtwoord: ")
                if invoerWachtwoord in wachtwoorden[indexRegistratienummer]:
                    print("U kunt uw fiets nu ophalen! heb een prettige dag!")
                    break
                else:
                    print("Dit wachtwoord hoord niet bij het registratienummer dat u heeft gegeven, probeer het opnieuw")
        else:
            print("Dit registratienummer is niet in gebruik, probeer het nog een keer!")
        break

ophalen()


