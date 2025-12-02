"""Tests for utility functions."""

from utils.helpers import chunks, manhattan_distance, neighbors_4, neighbors_8


def test_chunks():
    """Test chunks function."""
    data = [1, 2, 3, 4, 5, 6, 7]
    result = list(chunks(data, 3))
    assert result == [[1, 2, 3], [4, 5, 6], [7]]


def test_chunks_exact():
    """Test chunks with exact division."""
    data = [1, 2, 3, 4, 5, 6]
    result = list(chunks(data, 2))
    assert result == [[1, 2], [3, 4], [5, 6]]


def test_manhattan_distance():
    """Test Manhattan distance calculation."""
    assert manhattan_distance((0, 0), (3, 4)) == 7
    assert manhattan_distance((1, 1), (1, 1)) == 0
    assert manhattan_distance((-2, -3), (2, 3)) == 10


def test_neighbors_4():
    """Test 4-directional neighbors."""
    result = neighbors_4(5, 5)
    assert len(result) == 4
    assert (5, 4) in result  # up
    assert (5, 6) in result  # down
    assert (4, 5) in result  # left
    assert (6, 5) in result  # right


def test_neighbors_8():
    """Test 8-directional neighbors."""
    result = neighbors_8(5, 5)
    assert len(result) == 8
    assert (4, 4) in result  # top-left
    assert (5, 4) in result  # top
    assert (6, 4) in result  # top-right
    assert (4, 5) in result  # left
    assert (6, 5) in result  # right
    assert (4, 6) in result  # bottom-left
    assert (5, 6) in result  # bottom
    assert (6, 6) in result  # bottom-right
