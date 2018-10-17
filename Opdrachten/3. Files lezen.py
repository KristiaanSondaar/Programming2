file = open("kaartnummers", "r")

count = 0
maxNumber = 0
lineCount = 1

for lines in file:
    count += 1
    number = int(lines.split(",")[0])
    if number > maxNumber:
        maxNumber = number
        maxLine = lineCount
        lineCount += 1

print('Deze file telt', count, "regels")

print("Het grootste kaartnummer is ",maxNumber, " en dat staat op regel: ",lineCount)

file.close()