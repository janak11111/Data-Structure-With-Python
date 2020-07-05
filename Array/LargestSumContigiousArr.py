ls = [-2, 4, 5, 10, -8, 4, 6]

def KadanesAlgo(arr):
    max_sum = 0
    a = 0
    for i in ls:
        a += i
        a = max(a, 0)
        max_sum = max(a, max_sum)
    print(max_sum)

KadanesAlgo(ls)