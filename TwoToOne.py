def longest(a1, a2):
    result = ''
    lista = list(set(a1 + a2))
    lista.sort()
    for i in lista:
        result += i
    return result


print(longest("aretheyhere", "yestheyarehere"))
print(longest("loopingisfunbutdangerous", "lessdangerousthancoding"))
