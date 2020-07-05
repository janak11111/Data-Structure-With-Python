def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def zigZag(arr):
    flag = True
    for i in range(len(arr) - 1):
        if flag:
            if arr[i] > arr[i + 1]:
                swap(arr, i, i + 1)
        else:
            if arr[i] < arr[i + 1]:
                swap(arr, i, i + 1)
        flag = not flag
    return arr


print(zigZag([4, 3, 7, 8, 6, 2, 1]))
