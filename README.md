# Advent of Code 2025

Python solutions for [Advent of Code 2025](https://adventofcode.com/2025).

## Project Structure

```
aoc25/
├── day01/              # Solution for day 1
│   ├── solution.py     # Main solution code
│   ├── input.txt       # Puzzle input
│   └── example.txt     # Example input from puzzle
├── day02/              # Solution for day 2
│   └── ...
├── utils/              # Shared utility functions
│   ├── input_reader.py # Input reading helpers
│   └── helpers.py      # Common helper functions
├── tests/              # Unit tests
└── create_day.py       # Script to create new day folders
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## Usage

### Creating a New Day

Use the `create_day.py` script to scaffold a new day:

```bash
python create_day.py <day_number>
```

Example:
```bash
python create_day.py 5  # Creates day05/ folder with template files
```

### Solving a Puzzle

1. Navigate to the day folder (e.g., `day01/`)
2. Add your puzzle input to `input.txt`
3. Optionally add example input to `example.txt`
4. Implement the solution in `solution.py`
5. Run the solution:

```bash
python -m day01.solution
```

### Running Tests

Run all tests:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=utils --cov=day01
```

## Utility Functions

The `utils` module provides common helper functions:

### Input Reading
- `read_input(day, filename)` - Read entire input as string
- `read_input_lines(day, filename)` - Read input as list of lines
- `read_input_numbers(day, filename)` - Read input as list of integers
- `read_input_grid(day, filename)` - Read input as 2D grid

### Helpers
- `chunks(iterable, n)` - Split iterable into chunks
- `manhattan_distance(p1, p2)` - Calculate Manhattan distance
- `neighbors_4(x, y)` - Get 4 orthogonal neighbors
- `neighbors_8(x, y)` - Get 8 neighbors including diagonals

## Example Solution

```python
from utils import read_input_lines

def parse_input(data: list[str]):
    return [int(x) for x in data]

def part1(data):
    return sum(data)

def part2(data):
    return sum(x * 2 for x in data)

def main():
    lines = read_input_lines(1)
    data = parse_input(lines)
    
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")

if __name__ == "__main__":
    main()
```

## Development

### Code Formatting
```bash
black .
```

### Linting
```bash
flake8 .
```
