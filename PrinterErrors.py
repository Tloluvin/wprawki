import string
alphabet = list(string.ascii_lowercase)


def printer_error(s):
    result = 0
    for l in s:
        if l in alphabet:
            if alphabet.index(l) > 12:
                result += 1
    return f"{result}/{len(s)}"


print(printer_error('aaaaaaaaaaaabbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmxyz'))
print(printer_error('kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz'))
print(printer_error('kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu'))
