#  method 1

arr = [1, 2, 3, 4, 5, 6]

print(arr[::-1])


#  method 2

def reversedArry(start, end, arr):
    while start < end:
        arr[start], arr[end - 1] = arr[end - 1], arr[start]
        start += 1
        end -= 1
    return arr

arr = [1, 2, 3, 4, 5, 6]
print(arr)
print(reversedArry(0, len(arr), arr))


