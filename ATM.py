# An ATM has banknotes of nominal values 10, 20, 50, 100, 200 and 500 dollars. You can consider that there is a large enough supply of each of these banknotes.
# You have to write the ATM's function that determines the minimal number of banknotes needed to honor a withdrawal of n dollars, with 1 <= n <= 1500.
# Return that number, or -1 if it is impossible.

def solve(n):
    banknotes = 0
    a = 0
    if n < 0:
        return -1
    if (n % 10 == 0):
        while n > 0:       
            if n >= 500:
                banknotes += 1
                n -= 500
                continue
            if n >= 200:
                banknotes += 1
                n -= 200
                continue
            if n >= 100:
                banknotes += 1
                n -= 100
                continue
            if n >= 50:
                banknotes += 1
                n -= 50
                continue
            if n >= 20:
                banknotes += 1
                n -= 20
                continue
            if n >= 10:
                banknotes += 1
                n -= 10
                continue
    else:
        return -1
    return banknotes

print('770', solve(770))     # 4
print('550', solve(550))     # 2
print('10',solve(10))        # 1
print('1250',solve(1250))    # 4
print('1500',solve(1500))    # 3
print('125',solve(125))      # -1
print('666',solve(666))      # -1
print('42', solve(42))       # -1
