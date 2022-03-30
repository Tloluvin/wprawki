def reverse_letter(string):
    result = ''
    for l in string:
        if l.isalpha():
            result += l
    return result[::-1]


print(reverse_letter("krishan"))
print(reverse_letter("ultr53o?n"))
print(reverse_letter("ab23c"))
print(reverse_letter("krish21an"))
