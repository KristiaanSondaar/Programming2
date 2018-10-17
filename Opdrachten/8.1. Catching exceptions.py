

try:
    aantal = 0
    hotel = 4356
    kosten = 4356 / aantal
    if aantal < 0:
        print("Negatieve getallen zijn niet toegestaan!")
    else:
        print(kosten)
except TypeError:
    print("Gebruik cijfers voor het invoeren van het aantal!")
except ZeroDivisionError:
    print("Delen door nul kan niet!")
except:
    "Onjuiste invoer!"


    
    
    
    
