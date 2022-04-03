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
    mark = 0
    poz = 0
    if N == 0:
        return ''
    if N < 0:
        return None
    if N == 1:
        return alphabet[0]
    for i in range(0, N*N):

        if i == ((N*N)-1):
            result += alphabet[mark]
        elif (i+1) % N == 0:
            result += alphabet[mark]+'\n'
            mark = poz
            if poz >= 25:
                poz = 0
            else:
                poz += 1
            if mark >= N:
                mark = 0
        else:
            result += alphabet[mark] + ' '
        mark += 1
        if mark >= 26:
            mark = 0
    return result


print(grid(89))
