import ctypes

class DynamicArray(object):

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def __len__(self):
        return self._n
    #     use when we need the length of object ---> len(arr)

    def __str__(self):
        temp = ""
        for i in range(self._n):
            temp += str(self._A[i]) + ','
        temp = temp[:-1]
        return  '[' + temp + ']'

    #   use when we write print -- >print(arr)

    def __getitem__(self, index):
        if  0 <= index <= self._n:
            return self._A[index]
        else:
            return 'Index Error'

    #  used when we access the index --> arr[index]


    def __delitem__(self, index):
        if 0 <= index <= self._n:
            for i in range(index, self._n -1):
                self._A[i] = self._A[i+1]
            self._n -= 1
        else:
            print('Index Error')
            return
    #  used when we delete using del -- > del arr[index]


    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c



    def insert(self, index, value):
        if 0<=index<=self._n:
            if self._n == self._capacity:
                self._resize(2 * self._capacity)
            for j in range(self._n - 1, index - 1 , -1):
                self._A[j + 1] = self._A[j]
            self._A[index] = value
            self._n += 1
        else:
            print('Index Error')

    def remove(self, value):
        flag = 0
        for i in range(self._n):
            if self._A[i] == value:
                flag = 1
                for j in range(i, self._n - 1 ):
                    self._A[j] = self._A[j + 1]
                self._n -= 1
                break
        if flag == 0:
            print('Value Not Found')

    def pop(self):
        self._n -= 1

    def clear(self):
        self._n = 0
        self._capacity  =1

    def search(self, item):
        flag = 0
        for i in range(self._n):
            if self._A[i] == item:
                flag = 1
                break
        if flag == 1:
            print(i)
        else:
            print('Item Not Found')


arr = DynamicArray()

arr.append(10)
arr.append(20)
arr.append(30)
arr.append(40)
arr.append(50)
arr.append(60)
print(len(arr))
print(arr)
print(arr[0])
print(arr[2])
print(arr[10])
print(arr)
del arr[0]
print(arr)
del arr[0]
print(arr)
del arr[100]
print(arr)
arr.insert(2,200)
print(arr)
arr.insert(200,200)
print(arr)
arr.remove(200)
print(arr)
arr.remove(30)
print(arr)
arr.remove(300)
arr.search(60)
arr.search(30)
arr.search(40)
arr.pop()
print(arr)
arr.pop()
print(arr)
arr.clear()
print(arr)
print(len(arr))



















