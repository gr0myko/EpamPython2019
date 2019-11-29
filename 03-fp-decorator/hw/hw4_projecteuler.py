from functools import reduce
s = ''
for i in range(0, 1000000):
    s = s + str(i)
list_from_s = [int(value) for pos, value in enumerate(s) if pos in {1, 10, 100, 1000, 10000, 100000, 1000000}]
b = reduce(lambda x, y: x*y, list_from_s)
print(b)
