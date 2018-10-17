def new_password(newpassword,oldpassword):
    if len(newpassword) >= 6 and newpassword != oldpassword:
        return


oldpassword = str(input('Geef oude wachtwoord: '))
newpassword = str(input('Geef nieuwe wachtwoord: '))

isCorrect = new_password(newpassword,oldpassword)

if isCorrect == True:
    print('Het is gelukt!')
else:
    print('Het password is hetzelfde of niet lang genoeg.')





