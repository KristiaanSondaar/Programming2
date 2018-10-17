def lang_genoeg(lengte):
    if lengte >= str('120'):
        print('Je bent lang genoeg voor de attractie!')
    else:
        print('Sorry, je bent te klein')


geefLengte = lang_genoeg (input('Geef je lengte: '))


