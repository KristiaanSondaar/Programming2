stations = ["Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam",
            "Amsterdam" "Sloterdijk", "Amsterdam Centraal", "Amsterdam Amstel", "Utrecht Centraal",
            "’s-Hertogenbosch", "Eindhoven", "Weert", "Roermond", "Sittard", "Maastricht"]


def inlezen_beginstation(stations):
    while True:
        beginstation = input("Wat is je beginstation?: ")
        if beginstation in stations:
            break
    return beginstation

def inlezen_eindstation(stations, beginstation):
    while True:
        eindstation = input("Wat is je eindstation?: ")
        eindIndex = stations.index(eindstation)
        beginIndex = stations.index(beginstation)
        if eindstation in stations and eindIndex > beginIndex:
            break
        else:
            print("Dit station ligt niet op de route")
    return eindstation


def omroepen_reis(stations, beginstation, eindstation):
    beginRangnummer = stations.index(beginstation) + 1
    eindRangnummer = stations.index(eindstation) + 1
    print("Het beginstation", beginstation, "is het", beginRangnummer,"e station in het traject.", )
    print("Het eindstation", eindstation,"is het", eindRangnummer, "e station in het traject.")
    print("De afstand bedraagt",eindRangnummer - beginRangnummer ,"station(s).")
    print("De prijs van het kaartje is",(eindRangnummer - beginRangnummer)*5,"euro.\n")
    print("Jij stapt in de trein in:", beginstation,)
    for x in stations[beginRangnummer:stations.index(eindstation)]:
        print("-",x)
    print("Jij stapt uit in:", eindstation)
    return




beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
