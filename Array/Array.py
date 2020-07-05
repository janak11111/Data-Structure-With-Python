class Array:
    def __init__(self):
        self.item = []

    def is_empty(self):
        if len(self.item) == 0:
            print("Array is Empty")
        else:
            print("Not empty")

    def insert(self, index, value):
        self.item.insert(index, value)

    def delete(self,value):
        self.item.remove(value)

    def size(self):
        print(len(self.item))

    def view(self):
        print(self.item)



arr = Array()

arr.is_empty()
arr.size()
arr.view()
arr.insert(0,10)
arr.view()
arr.insert(1,20)
arr.view()
arr.insert(2,30)
arr.view()
arr.delete(30)
arr.view()
arr.size()
arr.is_empty()
arr.view()