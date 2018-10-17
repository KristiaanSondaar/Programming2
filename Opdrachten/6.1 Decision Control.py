maand = int(input('Geef maand nummer: '))


def seizoen(maand):
    if (maand in (3 , 4 , 5)):
        season = ('Lente')
    elif (maand in (6, 7, 8)):
        season =  ('Zomer')
    elif (maand in (9, 10, 11)):
        season = ('Herfst')
    else:
        season =  ('Winter')
    return season


print(seizoen(maand))