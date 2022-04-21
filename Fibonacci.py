# Create function fib that returns n'th element of Fibonacci sequence(classic programming task).

def fibonacci(n: int) -> int:
    """Given a positive argument n, returns the nth term of the Fibonacci Sequence.
    """
    result = 0
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(0))     # 0
print(fibonacci(1))     # 1
print(fibonacci(2))     # 1
print(fibonacci(3))     # 2
print(fibonacci(4))     # 3
print(fibonacci(5))     # 5
print(fibonacci(6))     # 8
print(fibonacci(34))    # 5702887
print(fibonacci(299))   # 137347080577163115432025771710279131845700275212767467264610201

