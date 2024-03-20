
def test_1(*args):
    print(args)

def factorial(n):
    if n == 1:
        return 1
    factorial_n_minus_1 = factorial(n = n - 1)
    return n * factorial_n_minus_1

test_1(1, '2', True, [4])
print(factorial(9))