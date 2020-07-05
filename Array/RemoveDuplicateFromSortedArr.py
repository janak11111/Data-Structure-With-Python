from itertools import groupby

# method 1

ls = [1, 2, 3, 3,4, 5, 6, 6, 7, 7, 8, 9, 10, 10]
print(ls)
s = set(ls)
print(sorted(s))

# method 2

ls = [1, 2, 3, 3,4, 5, 6, 6, 7, 7, 8, 9, 10, 10]
print([k for k,v in groupby(ls)])