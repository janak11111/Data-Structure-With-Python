arr = [101, 103, 106, 109, 2, 3, 32, 57]
n = 57

def SearchElement(arr, n):
    first = 0
    last = len(arr) - 1

    while(first <= last):
        mid = (first + last) // 2

        if arr[mid] == n:
            return mid

        elif arr[first] < arr[mid]:
            if n >= arr[first] and n < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1

        else:
            if n > arr[mid] and n <= arr[last]:
                first = mid + 1
            else:
                last = mid - 1

    return 'Wrong Number Searching --> not found'


print(SearchElement(arr, n))