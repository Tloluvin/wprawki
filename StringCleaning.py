# Your boss decided to save money by purchasing some cut-rate optical character recognition software for scanning in the text of old novels to your database. At first it seems to capture words okay, but you quickly notice that it throws in a lot of numbers at random places in the text.
# Examples (input -> output)
# '! !'                 -> '! !'
# '123456789'           -> ''
# 'This looks5 grea8t!' -> 'This looks great!'
# Your harried co-workers are looking to you for a solution to take this garbled text and remove all of the numbers. Your program will take in a string and clean out all numeric characters, and return a string with spacing and special characters ~#$%^&!@*():;"'.,? all intact.

def string_clean(s):
    result = ''
    for c in s:
        if c.isnumeric():
            continue
        else:
            result += c
    return result


print(string_clean("123456789"))
print(string_clean("(E3at m2e2!!)"))
print(string_clean("Dsa32 cdsc34232 csa!!! 1I 4Am cool!"))
print(string_clean("A1 A1! AAA   3J4K5L@!!!"))
print(string_clean("Adgre2321 A1sad! A2A3A4 fv3fdv3J544K5L@"))
