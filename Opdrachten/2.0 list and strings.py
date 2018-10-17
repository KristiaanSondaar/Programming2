lijst = eval(input('Geef lijst met minimaal 10 strings: '))
lijst2 = []
for char in lijst:
    if len(char) == 4:
        lijst2.append(char)


print("De nieuw-gemaakte lijst met alle vier-letter strings is: ", lijst2)
