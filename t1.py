def script():
    x = float(input('Количество отработанных часов : '))
    y = float(input('Сумма оплаты труда за 1 час : '))
    c = float(input('Размер премии - '))
    pay = x * y
    return pay + c
print(f'Размер заработной платы: {script() }')