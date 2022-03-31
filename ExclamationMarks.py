# Remove an exclamation marks from the end of string
def remove(s):
    if len(s) > 0 and (s[-1] == '!'):
        s = s[:-1]
        return remove(s)
    return s

print(remove('Hi'))
print(remove('Hi!!!'))
print(remove('!Hi!'))
print(remove('Hi! Hi'))
print(remove(''))