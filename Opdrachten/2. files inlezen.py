infile = open("kaartnummers", "r")



for line in infile:
    info = line.split(",")
    nummer = info[0]
    naam = info[1]
    print(naam, end=' ')
    print(('{:5}{0:5}{0:5}'.format(nummer),("heeft kaartnummer: ")))


infile.close()