#!/usr/bin/env python3
"""Script to create a new day folder for Advent of Code."""

import argparse
from pathlib import Path


SOLUTION_TEMPLATE = '''"""Day {day}: [Puzzle Title]

https://adventofcode.com/2025/day/{day}
"""

from utils import read_input_lines


def parse_input(data: list[str]):
    """Parse the input data."""
    # TODO: Implement input parsing
    return data


def part1(data):
    """Solve part 1 of the puzzle."""
    # TODO: Implement solution for part 1
    pass


def part2(data):
    """Solve part 2 of the puzzle."""
    # TODO: Implement solution for part 2
    pass


def main():
    """Main entry point for the solution."""
    lines = read_input_lines({day})
    data = parse_input(lines)

    result1 = part1(data)
    print(f"Part 1: {{result1}}")

    result2 = part2(data)
    print(f"Part 2: {{result2}}")


if __name__ == "__main__":
    main()
'''


def create_day(day: int):
    """Create a new day folder with template files."""
    day_dir = Path(__file__).parent / f"day{day:02d}"

    if day_dir.exists():
        print(f"Day {day} folder already exists!")
        return

    day_dir.mkdir()

    # Create solution.py
    solution_file = day_dir / "solution.py"
    solution_file.write_text(SOLUTION_TEMPLATE.format(day=day))

    # Create input.txt
    input_file = day_dir / "input.txt"
    input_file.write_text("# Add your puzzle input here\n")

    # Create example.txt
    example_file = day_dir / "example.txt"
    example_file.write_text("# Add example input from puzzle description here\n")

    print(f"Created day{day:02d} folder with template files!")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Create a new Advent of Code day folder")
    parser.add_argument("day", type=int, help="Day number (1-25)")

    args = parser.parse_args()

    if args.day < 1 or args.day > 25:
        print("Error: Day must be between 1 and 25")
        return

    create_day(args.day)


if __name__ == "__main__":
    main()
