def find_next_smaller_element(arr):
    ls = [-1 for i in arr]
    stack = []
    for i, x in enumerate(arr):
        print(i, x)
        while len(stack) > 0 and x < arr[stack[-1]]:
            ls[stack.pop()] = x
        stack.append(i)
        print(stack[-1])
    return  ls

print(find_next_smaller_element([4,2,1,5,3]))
