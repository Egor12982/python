with open('art', 'r', encoding='utf - 8') as f:
    lines = f.readlines()

with open('artw', 'w', encoding='utf - 8') as f:
    for x in lines:
        if '1' in x:
            x = x.replace('One', 'Один')
        elif '2' in x:
            x = x.replace('Two', 'Два')
        elif '3' in x:
            x = x.replace('Three', 'Три')
        elif '4' in x:
            x = x.replace('Four', 'Четыре')
        f.write(x)

