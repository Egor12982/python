from itertools import count
from itertools import cycle

def count_func(start_number, stop_number):
    for x in count(start_number):
        if x > stop_number:
            break
        else:
            print(x)
def cycle_func(my_list, iteration):
    i = 0
    a = cycle(my_list)
    while i < iteration:
        print(next(a))
        i+=1
count_func(start_number = int(input("start number: ")), stop_number = int(input("stop number: ")))
cycle_func(my_list = [1, 2], iteration = int(input("enter iteration: ")))