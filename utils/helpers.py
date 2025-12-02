"""Common helper functions for Advent of Code solutions."""

from typing import TypeVar, Iterable

T = TypeVar("T")


def chunks(iterable: Iterable[T], n: int) -> Iterable[list[T]]:
    """
    Split an iterable into chunks of size n.

    Args:
        iterable: The iterable to split
        n: The size of each chunk

    Yields:
        Lists of size n (last chunk may be smaller)
    """
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == n:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def manhattan_distance(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    """
    Calculate Manhattan distance between two points.

    Args:
        p1: First point (x, y)
        p2: Second point (x, y)

    Returns:
        Manhattan distance between the points
    """
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def neighbors_4(x: int, y: int) -> list[tuple[int, int]]:
    """
    Get 4 orthogonal neighbors of a point.

    Args:
        x: X coordinate
        y: Y coordinate

    Returns:
        List of 4 neighboring coordinates (up, down, left, right)
    """
    return [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]


def neighbors_8(x: int, y: int) -> list[tuple[int, int]]:
    """
    Get 8 neighbors of a point (including diagonals).

    Args:
        x: X coordinate
        y: Y coordinate

    Returns:
        List of 8 neighboring coordinates
    """
    return [
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x - 1, y),
        (x + 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    ]
