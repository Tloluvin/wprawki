# Task:
# You need to write a function grid that returns an alphabetical grid of size NxN, where a = 0, b = 1, c = 2....
# Examples:
# grid(4)

# a b c d
# b c d e
# c d e f
# d e f g


import string
alphabet = list(string.ascii_lowercase) #26

def grid(N):    
    result = ''
    mark = N*N
    row = N
    column = N
    poz = 0
    if N < 0:
        return None
    if N == 1:
        return alphabet[poz]
    for i in range(0,mark): 
        if mark == 0:
            return result
        else:
            if (column)%N != 1:
                result += alphabet[poz] + ' '
            else:
                result += (alphabet[poz])
            if (column)%N ==1:
                if row == 0:
                    continue
                else:
                    if mark == 1:
                        return result
                    result += '\n'
                    poz -= N-1
                row -= 1
            poz += 1
            mark -= 1 
            column -= 1
    return result

print(grid(13))