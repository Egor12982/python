def my_pow_func(x, y):
    try:
        ans = x ** y
    except TypeError:
        return 'Enter float'
    return ans

print(my_pow_func(5, -3))