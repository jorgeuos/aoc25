"""Utility functions for Advent of Code solutions."""

from pathlib import Path


def read_input(day: int, filename: str = "input.txt") -> str:
    """
    Read input file for a given day.

    Args:
        day: The day number (1-25)
        filename: The name of the input file (default: "input.txt")

    Returns:
        The contents of the input file as a string
    """
    day_str = f"day{day:02d}"
    input_path = Path(__file__).parent.parent / day_str / filename
    return input_path.read_text().strip()


def read_input_lines(day: int, filename: str = "input.txt") -> list[str]:
    """
    Read input file for a given day and return as list of lines.

    Args:
        day: The day number (1-25)
        filename: The name of the input file (default: "input.txt")

    Returns:
        List of lines from the input file
    """
    return read_input(day, filename).splitlines()


def read_input_numbers(day: int, filename: str = "input.txt") -> list[int]:
    """
    Read input file for a given day and return as list of integers.

    Args:
        day: The day number (1-25)
        filename: The name of the input file (default: "input.txt")

    Returns:
        List of integers from the input file
    """
    return [int(line) for line in read_input_lines(day, filename)]


def read_input_grid(day: int, filename: str = "input.txt") -> list[list[str]]:
    """
    Read input file for a given day and return as 2D grid.

    Args:
        day: The day number (1-25)
        filename: The name of the input file (default: "input.txt")

    Returns:
        2D list (grid) of characters from the input file
    """
    return [list(line) for line in read_input_lines(day, filename)]
