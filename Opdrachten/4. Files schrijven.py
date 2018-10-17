import datetime
def strftime():
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%a %d %b %Y %H:%M:%S")
    return (s)

datum = strftime()
naam = input("Naam hardloper: ")
runners = open("Hardlopers.txt", "a+")
runners.write(datum + " " + naam + " " + "\n")
runners.close()