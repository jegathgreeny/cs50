import timeit
import math

global n

n = 547637264874365847356893465743685746587423658743658743658734658743658437564738654387566767389


def is_prime():
    """Checks if a number is prime."""
    for i in range(2, int(math.sqrt(n) + 1)):
        if n < 2:
            return False
        if n % i == 0:
            print(i)
            return False
    return True


def is_it_prime():
    """Checks if a number is prime."""
    for i in range(2, n):
        if n < 2:
            return False
        if n % i == 0:
            print(i)
            return False
    return True


print(f"with the math module\t\t{timeit.timeit(is_prime, number=1)}")
print(f"without the math module\t\t{timeit.timeit(is_it_prime, number=1)}")
