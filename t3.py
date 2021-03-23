with open('NEM') as key:
    lines = key.readlines()

salaries = []
for x in lines:
    name, salary = x.split(' - ')
    salaries.append(int(salary))
    if int(salary) < 20000:
        print(x, end = '')
print('\nСредняя зп:', sum(salaries) / len(salaries))