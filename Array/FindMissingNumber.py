#  method 1 using sum(n) - sum(given list)

a = [1, 2, 3, 5 ,6 ,7 ,8 ,9, 10]
n = len(a) + 1
missing_num = (n*(n+1))//2 - sum(a)
print(missing_num)


#  method 2 using XOR opeation is set use by ^ opearator

def f():
    a = [1, 2, 3, 5, 6, 7, 8, 9, 10]
    b = { x for x in range(1, len(a)+2)}
    a = set(a)
    c = a ^ b
    print(c.pop())
f()

