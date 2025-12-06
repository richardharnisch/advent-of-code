from typing import Any, List, Literal, Tuple, Iterable
import inspect


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


def get_neighborhood(
    grid: Iterable[Iterable[Any]],
    coord: Tuple[int, int],
    use_diagonal: bool = True,
    pad_value: Any = None,
) -> List[List[Any]]:
    """
    Return a 3x3 neighborhood around coord in grid.

    - grid: list of lists with arbitrary contents
    - coord: (row, col) in grid
    - use_diagonal: if False, diagonal positions are filled with pad_value
    - pad_value: used for out-of-bounds positions and (optionally) diagonals

    Handles ragged rows (rows of different lengths).
    """
    row, col = coord
    neighborhood: List[List[Any]] = []

    for dr in (-1, 0, 1):
        row_vals: List[Any] = []
        for dc in (-1, 0, 1):
            r = row + dr
            c = col + dc

            # If diagonals are disabled and this is a diagonal cell, pad it.
            if not use_diagonal and dr != 0 and dc != 0:
                row_vals.append(pad_value)
                continue

            # Check bounds (including ragged rows)
            if 0 <= r < len(grid) and 0 <= c < len(grid[r]):
                row_vals.append(grid[r][c])
            else:
                row_vals.append(pad_value)

        neighborhood.append(row_vals)

    return neighborhood


def count_nested(list: Iterable, value: Any) -> int:
    """
    Counts occurrences of value in a nested list.

    Parameters:
    list (list): The nested list to search.
    value (Any): The value to count.

    Returns:
    int: The count of occurrences of value in the nested list.
    """
    count = 0
    for item in list:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            count += count_nested(item, value)
        elif item == value:
            count += 1
    return count


def dprint(
    *values: object,
    level: int | None = None,
    **print_kwargs: Any,
) -> None:
    """
    Debug print function that uses the DEBUG variable from the caller's module.
    Works like print(*values, **print_kwargs), with an extra 'level' kwarg.
    """
    frame = inspect.currentframe()
    if frame is None:
        raise RuntimeError("Could not get caller frame for dprint")

    try:
        caller_frame = frame.f_back
        if caller_frame is None:
            raise RuntimeError("Could not get caller frame for dprint")

        DEBUG = caller_frame.f_globals.get("DEBUG", False)

        if (level is None and DEBUG) or (level is not None and DEBUG >= level):
            print(*values, **print_kwargs)
    finally:
        # avoid reference cycles with frames
        del frame


if __name__ == "__main__":
    assert divisors(28) == [1, 2, 4, 7, 14]
    assert split_str("abcdefgh", 2) == ["ab", "cd", "ef", "gh"]
    assert all_equal([1, 1, 1])
    assert not all_equal([1, 2, 1])
    array = [
        [1, 2, 3],
        [4, None, 6],
        [7, 8, 9],
    ]
    assert get_neighborhood(array, (0, 0), use_diagonal=True, pad_value=None) == [
        [None, None, None],
        [None, 1, 2],
        [None, 4, None],
    ]
