from random import *

def monopolyworp():
    x = randint(1, 6)
    y = randint(1, 6)
    x2 = randint(1, 6)
    y2 = randint(1, 6)
    x3 = randint(1, 6)
    y3 = randint(1, 6)
    rol = x + y
    rol2 = x2 + y2
    rol3 = x3 + y3
    for i in range(0,3):
        if x == y:
            print(x,"+", y,"=", rol, "(dubbel)")
            print(x2,"+", y2,"=", rol2)
            break
        elif x == y and x2 == y2:
            print(x, "+", y, "=", rol, "(dubbel")
            print(x2, "+", y2, "=", rol2, "dubbel")
            print(x3, "+", y3, "=", rol3)
            break
        elif x == y and x2 == y2 and x3 == y3:
            print(x, "+", y, "=", rol, "(dubbel")
            print(x2, "+", y2, "=", rol2, "(dubbel)")
            print(x3, "+", y3, "=", rol3, "(direct naar de gevangenis")
            break
        else:
            print(x,"+", y,"=", rol)
            break

monopolyworp()