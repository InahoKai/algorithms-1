def fib(n: int):
    if n < 3:
        return 1
    a = b = 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return a
