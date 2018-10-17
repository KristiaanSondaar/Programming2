for rij in range(1, 11):
    for col in range(1, 11):
        num = rij * col
        if num < 10: blank = '  '
        else:
            if num < 100: blank  = ' '
        print(blank, num, end = '')
    print()