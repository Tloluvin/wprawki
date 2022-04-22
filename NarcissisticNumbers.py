# A Narcissistic Number is a number of length n in which the sum of its digits to the power of n is equal to the original number. 
# If this seems confusing, refer to the example below.
# Ex: 153, where n = 3 (number of digits in 153)
# 13 + 53 + 33 = 153
# Write a method is_narcissistic(i) (in Haskell: isNarcissistic :: Integer -> Bool) which returns whether or not i is a Narcissistic Number.

def is_narcissistic(i):
    string = str(i)
    pow_str = len(string)
    result = 0
    for n in string:
        result += int(n)**pow_str
    if result == i:
        return True
    else:
        return False

print(is_narcissistic(153))     # True
print(is_narcissistic(201))     # False
print(is_narcissistic(259))     # False
print(is_narcissistic(371))     # True
print(is_narcissistic(407))     # True
print(is_narcissistic(595))     # False
print(is_narcissistic(825))     # False
print(is_narcissistic(1634))    # True
