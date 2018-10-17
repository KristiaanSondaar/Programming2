woorden = []

def gemiddelde():
    zin = input("Geef een willekeurige zin: ")
    woorden = zin.split()
    for lengte in woorden:
        print(len(lengte))

gemiddelde()
print(gemiddelde())

