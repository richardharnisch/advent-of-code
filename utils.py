def divisors(n: int) -> list[int]:
    """
    Returns a list of integer divisors of a number n, excluding n.

    Parameters:
    n (int): The number to find divisors for.

    Returns:
    list: A list of divisors of n.
    """
    return [i for i in range(1, n) if n % i == 0]


def split_str(str: str, n: int) -> list[str]:
    """
    Splits a string into parts of length n.

    Params:
    str (str): The string to split.
    n (int): The length of each part.

    Returns:
    list: A list of string parts.

    Raises:
    ValueError: If the length of the string is not divisible by n.
    """
    if len(str) % n != 0:
        raise ValueError("String length is not divisible by n")
    return [str[i : i + n] for i in range(0, len(str), n)]


def all_equal(list: list) -> bool:
    """
    Checks if all elements in a list are equal.

    Parameters:
    list (list): The list to check.

    Returns:
    bool: True if all elements are equal, False otherwise.
    """
    return all(x == list[0] for x in list)
