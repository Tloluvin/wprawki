# Create function fib that returns n'th element of Fibonacci sequence(classic programming task).

def fibonacci(n: int) -> int:
    """Given a positive argument n, returns the nth term of the Fibonacci Sequence.
    """
    result = 0
    x = 0
    y = 1
    result = 0
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        for i in range(n-1):
            result = x + y
            x, y = y, x + y     
        return result


print('0 =',fibonacci(0))     # 0
print('1 =',fibonacci(1))     # 1
print('1 =',fibonacci(2))     # 1
print('2 =',fibonacci(3))     # 2
print('3 =',fibonacci(4))     # 3
print('5 =',fibonacci(5))     # 5
print('8 =',fibonacci(6))     # 8
print('5702887 =',fibonacci(34))    # 5702887
print('137347080577163115432025771710279131845700275212767467264610201 =',fibonacci(299))

