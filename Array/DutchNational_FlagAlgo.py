colors = ['red', 'white', 'blue', 'white', 'blue', 'red', 'white']

def DutchNationFalgProblem(colors):
    reds = 0
    whites = 0
    blues = 0

    for color in colors:
        c = color.lower().strip()
        if c == 'red':
            reds += 1
        elif c == 'white':
            whites += 1
        elif c == 'blue':
            blues += 1

    flag = []

    for i in range(0, reds):
        flag.append('red')
    for j in range(0, whites):
        flag.append('white')
    for k in range(0, blues):
        flag.append('blue')
    return flag

print(DutchNationFalgProblem(colors))