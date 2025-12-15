from typing import Any, List, Literal, Optional, Set, Tuple, Iterable
import inspect


def divisors(n: int) -> List[int]:
    """
    Returns a list of integer divisors of a number n, excluding n.

    Parameters:
    n (int): The number to find divisors for.

    Returns:
    list: A list of divisors of n.
    """
    return [i for i in range(1, n) if n % i == 0]


def split_str(str: str, n: int) -> List[str]:
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


def all_equal(list: List) -> bool:
    """
    Checks if all elements in a list are equal.

    Parameters:
    list (list): The list to check.

    Returns:
    bool: True if all elements are equal, False otherwise.
    """
    return all(x == list[0] for x in list)


def get_neighborhood(
    grid: List[List[Any]],
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
    level: Optional[int] = None,
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


def dprint_list(
    list: Iterable[Any],
    level: Optional[int] = None,
) -> None:
    """
    Debug print function for iterables, with one item per line.
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
            for item in list:
                print(item)
    finally:
        # avoid reference cycles with frames
        del frame


def dprint_grid(
    grid: Iterable[Iterable[Any]],
    level: Optional[int] = None,
) -> None:
    """
    Debug print function for 2d grids, assuming the same amount of columns in each row
    and the same amount of characters per cell.
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
            for row in grid:
                print("".join(str(cell) for cell in row))
    finally:
        # avoid reference cycles with frames
        del frame


def to_int(num: str) -> int:
    """
    Converts a numeric string or a number word (zero to nine) to an integer.
    """
    if num.isdigit():
        return int(num)
    else:
        word_to_num = {
            "zero": 0,
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }
        return word_to_num[num]


def getitem_safe(
    collection: Any,
    index: int,
    default: Any = None,
) -> Any:
    """
    Safely gets an item from a collection by index, returning a default value if the index is out of bounds.

    Parameters:
    collection (Any): The collection to get the item from.
    index (int): The index of the item to get.
    default (Any): The default value to return if the index is out of bounds.

    Returns:
    Any: The item at the specified index, or the default value if the index is out of bounds.
    """
    try:
        return collection[index]
    except IndexError:
        return default


def distance(
    start: Tuple, end: Tuple, measure: Literal["euclidean", "manhattan"] = "euclidean"
) -> float:
    """
    Calculate the distance between two points in n-dimensional space.
    Can do euclidean or manhattan distance.

    Params:
    start (tuple): The starting point coordinates.
    end (tuple): The ending point coordinates.
    measure (str): The distance measure to use ("euclidean" or "manhattan").
    """
    if measure == "euclidean":
        return sum((s - e) ** 2 for s, e in zip(start, end)) ** 0.5
    elif measure == "manhattan":
        return sum(abs(s - e) for s, e in zip(start, end))
    else:
        raise ValueError(f"Unknown distance measure: {measure}")


def concat_numbers(a: int, b: int) -> int:
    """
    Concatenate two integers and return the result as an integer.
    """
    return int(str(a) + str(b))


def lines_cross(
    line_1: Tuple[Tuple[int, int], Tuple[int, int]],
    line_2: Tuple[Tuple[int, int], Tuple[int, int]],
) -> bool:
    """
    Check if two line segments cross (not just intersect).

    "Cross" here means they intersect strictly inside both segments:
    - Touching at endpoints does NOT count.
    - Colinear overlapping does NOT count.
    """

    (x1, y1), (x2, y2) = line_1
    (x3, y3), (x4, y4) = line_2

    def cross(ax, ay, bx, by, cx, cy) -> int:
        """Cross product of AB x AC (sign only)."""
        return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)

    def sign(v: int) -> int:
        if v > 0:
            return 1
        if v < 0:
            return -1
        return 0

    c1 = cross(x1, y1, x2, y2, x3, y3)
    c2 = cross(x1, y1, x2, y2, x4, y4)
    c3 = cross(x3, y3, x4, y4, x1, y1)
    c4 = cross(x3, y3, x4, y4, x2, y2)

    s1, s2, s3, s4 = map(sign, (c1, c2, c3, c4))

    # If any are colinear (0), then they don't "cross" in the strict sense
    if 0 in (s1, s2, s3, s4):
        return False

    # Proper crossing: each segment straddles the other
    return s1 != s2 and s3 != s4


def combinations(n: int, k: int) -> Set[Tuple[int]]:
    """
    Returns all possible combinations of k elements from a set of n elements (0 to n-1).
    Returns a set of tuples, where each tuple is a combination defined by the indices of the selected elements.
    """
    # bro this shit took me like 20 minutes to think with my head and a piece of paper and then
    # i write the signature and docstring and copilot autocompletes the whole fucking thing fuck my life man omfg
    result = set()
    if k == 1:
        result = {(i,) for i in range(n)}
    else:
        for i in range(n):
            for tail in combinations(n - i - 1, k - 1):
                result.add((i,) + tuple(x + i + 1 for x in tail))
    return result


def stars_and_bars(bins: int, items: int) -> Set[Tuple[int]]:
    """
    Generates all possible stars and bins type combinations for a given number of bins and items.
    Returns a set of combinations, where each combination is represented as a tuple of integers,
    where each integer is how many items are in that bin.
    """
    combos = combinations(bins + items - 1, bins - 1)
    output = set()
    for combo in combos:
        combination = [0 for _ in range(bins)]
        for i, index in enumerate(combo):
            if i == 0:
                combination[0] = index
            else:
                combination[i] = index - combo[i - 1] - 1
        combination[-1] = items - sum(combination[:-1])
        output.add(tuple(combination))
    return output


def number_to_letter(n: int) -> str:
    """
    Converts a number to its corresponding lowercase letter (0 -> 'a', 1 -> 'b', ..., 25 -> 'z').
    """
    if 0 <= n < 26:
        return chr(ord("a") + n)
    else:
        raise ValueError("Input number must be in the range 0-25.")


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
    assert to_int("five") == 5
    assert to_int("3") == 3
    assert getitem_safe([1, 2, 3], 5, default=0) == 0
    assert combinations(4, 2) == {(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)}
    assert stars_and_bars(3, 2) == {
        (0, 0, 2),
        (0, 1, 1),
        (0, 2, 0),
        (1, 0, 1),
        (1, 1, 0),
        (2, 0, 0),
    }
    assert number_to_letter(0) == "a"
    assert number_to_letter(25) == "z"
    print("All tests passed.")
