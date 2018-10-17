invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

lijst = invoer.split("-")

lijst2 = list(map(int, lijst))
lijst2.sort()
gemiddelde = sum(lijst2) / len(lijst2)

print("Gesorteerde list van ints: ", lijst2)
print("Grootste getal: ", max(lijst2), " en kleinste getal: ", min(lijst2))
print("aanstal getallen: ", len(lijst2), "en Som van de getallen: ", sum(lijst2))
print("Gemiddelde: ", gemiddelde)