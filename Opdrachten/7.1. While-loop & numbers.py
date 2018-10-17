aantalNummers = 0
som = 0
while True:
    getal = int(input("Geef een getal: "))
    if getal == 0:
        break
    som += getal
    aantalNummers += 1

print("Er zijn",aantalNummers, "nummers ingevoerd, de som is: ", som)