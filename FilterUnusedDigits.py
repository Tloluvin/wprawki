# Given a varying number of integer arguments, return the digits that are not present in any of them.
# Example:
# [12, 34, 56, 78] = >  "09"
# [2015, 8, 26] = >  "3479"
# Note: the digits in the resulting string should be sorted.

def unused_digits(*args):
    numbers = str(args)
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for n in numbers:
        if n.isdigit() and int(n) in digits:
            digits.remove(int(n))
    return digits

print(unused_digits(12, 34, 56, 78))    # 09
print(unused_digits(2015, 8, 26))       # 3479
print(unused_digits(276, 575))          # 013489
print(unused_digits(643))               # 0125789
print(unused_digits(864, 896, 744))     # 01235

