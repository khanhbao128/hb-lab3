from functools import reduce

print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5], 3))
print(sum([3, 1, 2, 3, 4, 5]))