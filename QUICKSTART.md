# Quick Reference Guide

## Daily Workflow

### 1. Create a new day
```bash
python create_day.py <day_number>
```

### 2. Add your input
Copy your puzzle input to `dayXX/input.txt`

### 3. Implement solution
Edit `dayXX/solution.py`:
- Update the puzzle title in the docstring
- Implement `parse_input()` to parse the input
- Implement `part1()` for part 1 solution
- Implement `part2()` for part 2 solution

### 4. Run your solution
```bash
python -m dayXX.solution
```

## Available Utility Functions

### Input Reading
```python
from utils import read_input_lines, read_input, read_input_numbers, read_input_grid

# Read as list of strings
lines = read_input_lines(1)

# Read as single string
text = read_input(1)

# Read as list of integers
numbers = read_input_numbers(1)

# Read as 2D grid
grid = read_input_grid(1)
```

### Common Helpers
```python
from utils import chunks, manhattan_distance, neighbors_4, neighbors_8

# Split list into chunks
for chunk in chunks(data, 3):
    print(chunk)

# Calculate Manhattan distance
dist = manhattan_distance((0, 0), (3, 4))  # Returns 7

# Get orthogonal neighbors
neighbors = neighbors_4(x, y)  # Returns [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]

# Get all 8 neighbors (including diagonals)
all_neighbors = neighbors_8(x, y)
```

## Development Commands

### Run tests
```bash
pytest              # Run all tests
pytest -v           # Verbose mode
pytest tests/test_helpers.py  # Run specific test file
```

### Format code
```bash
black .             # Format all files
black dayXX/        # Format specific day
```

### Lint code
```bash
flake8              # Lint all files
flake8 dayXX/       # Lint specific day
```

## Tips

- Use `example.txt` for testing with example inputs from the puzzle description
- To read from example.txt instead of input.txt:
  ```python
  lines = read_input_lines(1, "example.txt")
  ```
- Add print statements to debug your solution
- Use Python's built-in debugging with `breakpoint()` for interactive debugging
