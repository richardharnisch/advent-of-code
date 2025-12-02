def divisors(n):
    """
    Returns a list of integer divisors of a number n, excluding n.
    """
    return [i for i in range(1, n) if n % i == 0]


def split_str(str, n):
    """
    Splits a string into parts of length n.
    """
    if len(str) % n != 0:
        raise ValueError("String length is not divisible by n")
    return [str[i : i + n] for i in range(0, len(str), n)]


def all_equal(list):
    """
    Checks if all elements in a list are equal.
    """
    return all(x == list[0] for x in list)
