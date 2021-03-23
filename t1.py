with open('fairy', 'x+') as key:
    while True:
        usr = input('write smth')
        if usr == '':
            break
        else:
            key.write(usr + '\n')