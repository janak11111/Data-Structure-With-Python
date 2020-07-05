from collections import Counter

ls = [1, 2, 2, 4, 2, 5, 2, 6, 2, 3, 2]
c = Counter(ls)
print(c)
x = c.most_common(1)
if x[0][1] > len(ls) // 2:
    for i in x:
        print(i[0])
else:
    print('No Majority Element Present In Array')

