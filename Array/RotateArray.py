#  method 1

arr = [1, 2, 3, 4, 5]
print(arr[2:] + arr[:2])


# method 2

from collections import deque

ls = [1, 2, 3, 4, 5]
d = deque(ls)
d.rotate(2)
print(d)
d.rotate(-2)
print(d)

# method 3

def rotation(rotateBy, arr):
    for i in range(rotateBy):
        rotate(arr)
    return arr

def rotate(arr):
    for i in range(len(arr) - 1):
        arr[i] , arr[i + 1] = arr[i + 1], arr[i]

#  upper rotate function for rotate 1 item at a time

print('arr before rotate :', arr)
rotate_arr = rotation(3, arr)
print('arr after rotate:', rotate_arr)


