def code():
    invoerstring = input("Geef string: ").strip()
    for c in invoerstring:
        cope = ord(c) + 3
        print(chr(cope),end="")

code()




