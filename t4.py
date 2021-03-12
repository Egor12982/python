usr = str(input('type words'))
usr_wrds = usr.split()
for x, word in enumerate(usr_wrds, start = 1):
    print(x, word[:10])