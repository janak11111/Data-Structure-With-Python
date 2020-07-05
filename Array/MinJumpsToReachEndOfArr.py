arr = [2, 1, 3, 1, 1, 4, 5, 2, 8]

def minJumps(arr, n):
    jumps = [0 for i in range(n)]

    if (n == 0) or (arr[0] == 0):
        return float('inf')

    jumps[0] = 0

    # Find the minimum number of
    # jumps to reach arr[i] from
    # arr[0] and assign this
    # value to jumps[i]
    for i in range(1, n):
        jumps[i] = float('inf')
        for j in range(i):
            if (j + arr[j] >= i) and (jumps[j] != float('inf'))  :
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break
    return jumps[n - 1]
print(minJumps(arr,len(arr)))