def standaardprijs(afstandKM):
    if afstandKM > 0 and afstandKM <= 50:
        return afstandKM * 0.80
    if afstandKM < 0:
        return afstandKM == 0
    else:
        return (afstandKM * 0.60) + 15


aftstandKM = int(input('Geef de afstand van uw rit: '))


def ritprijs(leeftijd, weekendrit, afstandKM):
    if weekendrit == 'nee' and leeftijd >= 65 or leeftijd < 12:
        return standaardprijs(aftstandKM) * 0.70
    if weekendrit == 'ja' and leeftijd >= 65 or leeftijd < 12:
        return standaardprijs(aftstandKM) * 0.65
    if weekendrit == 'nee' and (leeftijd < 65 and leeftijd > 12):
        return standaardprijs(aftstandKM)
    if weekendrit == 'ja' and (leeftijd < 65 and leeftijd > 12):
        return standaardprijs(aftstandKM) * 0.60


weekendrit = str(input('Rijs je in het weekend? ja of nee: '))

leeftijd = int(input('Geef uw leeftijd: '))


prijs = ritprijs(leeftijd, weekendrit, aftstandKM)

print(prijs)