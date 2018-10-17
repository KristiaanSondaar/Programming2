print("1: Ik wil weten hoeveel kluizen nog vrij zijn \n2: Ik wil een nieuwe kluis \n3: Ik wil even iets uit mijn kluis halen ")

keuze = (int((input("Kies uit optie 1, 2 of 3: "))))


file = open("kluizen.txt","r+")

def toon_aantal_kluizen_vrij():
    lines = sum(1 for line in file)
    linesRemaining = 12 - lines
    print("Er zijn nog:", linesRemaining, "kluizen vrij")


def nieuwe_kluis():
    kluisnummers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for lines in file:
        deKluisnummers = int(lines.split(";")[0])
        if deKluisnummers in kluisnummers:
                kluisnummers.remove(deKluisnummers)
    if len(kluisnummers) > 0:
        wachtwoord = (input("Geef een code voor uw kluisje: "))
        file.write((str(kluisnummers[0]) + ";" +  str(wachtwoord) + "\n"))
        print("u heeft kluisnummer: " + str(kluisnummers[0]))
    elif len(kluisnummers) == 0:
        print("Er zijn geen kluisjes meer beschikbaar")

def kluis_openen():
    geefKluisnummer = input("Geef uw kluisnummer: ")
    geefWachtwoord = input("Geef uw wachtwoord: ")
    for lines in file:
        jeKluisnummer = lines.split(";")[0]
        jeWachtwoord = lines.split(";")[1]
        if geefKluisnummer in jeKluisnummer and geefWachtwoord in jeWachtwoord:
            print("Uw kluisje is geopent")
            break
    else:
        print("combinatie incorrect")



if keuze == 1:
    toon_aantal_kluizen_vrij()
elif keuze == 2:
    nieuwe_kluis()
elif keuze == 3:
    kluis_openen()
else:
    print("ERROR Deze optie is niet beschikbaar")


file.close()