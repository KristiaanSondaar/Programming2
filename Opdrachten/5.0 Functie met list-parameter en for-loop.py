def kwadraten_som(grondgetallen):
    return sum(grondgetallen)


grondgetallen = []

for even in range(0, 5):
    nummers = int((input('Geef nummers: ')))
    if nummers % 2 == 0:
        grondgetallen.append(nummers**2)


print(grondgetallen)
print(kwadraten_som(grondgetallen))



