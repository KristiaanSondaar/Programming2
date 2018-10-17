def convert(celsius):
    return celsius * 1.8 + 32


celsius = 25

print(convert(celsius))

print('  F      C')


for i in range(-30,50,10):
    print('{:5}{:5}'.format(convert(i),i))

