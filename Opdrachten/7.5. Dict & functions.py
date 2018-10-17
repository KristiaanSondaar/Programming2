dict = {}
def namen():
    while True:
        deNamen = input("Volgende naam: ")
        if deNamen == "":
            break
        elif deNamen not in dict:
            dict[deNamen] = 1
        else:
            dict[deNamen] += 1
namen()

for x in dict:
    if dict[x] == 1:
        print("Er is ", dict[x], "student met de naam ", x)
    else:
        print("Er zijn ", dict[x], "studenten met de naam ", x)