arr = [3,9,8,4,5,7,10]
arr.sort()
Sum = 15

def allSumAPair(arr, Sum):
    l = 0
    r = len(arr) - 1
    while l < r:
        if (arr[l] + arr[r]) > Sum:
            r = r -1
        elif (arr[l] + arr[r]) < Sum:
            l = l + 1
        else:
            print(arr[l], arr[r])
            l = l + 1


allSumAPair(arr, Sum)