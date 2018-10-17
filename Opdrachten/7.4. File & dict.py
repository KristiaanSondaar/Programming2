file = open("ticker.txt","r")

dict = {}

def ticker():
    for lines in file:
        bedrijf = str(lines.split(":")[0])
        symbool = str(lines.split(":")[1])
        dict[bedrijf] = symbool

ticker()

while True:
    enterCompany = input("Enter company name: ")
    company = dict[enterCompany]
    print("Ticker symbool:", company)
    break



enterSymbool = input("Enter Ticker Symbool: ")
if enterSymbool in dict.values():
    print("Check")


