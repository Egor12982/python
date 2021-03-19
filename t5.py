from functools import reduce
my_list = [x for x in range(100, 1001) if x % 2 == 0]

def my_func(prev_x, x):
    return prev_x * x

print(reduce(my_func, my_list)) 