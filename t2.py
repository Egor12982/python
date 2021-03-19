a = [int(i) for i in input().split()]
for x in range(1, len(a)):
    if a[x] > a[x - 1]:
        print(a[x])