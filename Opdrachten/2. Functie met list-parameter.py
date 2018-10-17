def som(getallenLijst):
    return sum(getallenLijst)

getallenLijst = []


for i in range(0,5):
    nummers = int((input('Geef nummers: ')))
    getallenLijst.append(nummers)

print(som(getallenLijst))
