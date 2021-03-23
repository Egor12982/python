strings = 0
with open('dragon') as key:
    for x in key:
        strings = strings + 1
    print(strings)
with open('dragon') as key:
    lines = key.readlines()
for num_line, line in enumerate(lines, start = 1):
    print('{} строка содержит - {} слов'.format(num_line, len(line.split())))
