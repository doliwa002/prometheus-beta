import pytest
from src.fibonacci_odd_sequence import generate_odd_fibonacci_sequence

def test_generate_odd_fibonacci_sequence_basic():
    """Test basic functionality of the odd Fibonacci sequence generator."""
    result = generate_odd_fibonacci_sequence(5)
    assert result == [1, 1, 3, 5, 13], f"Expected [1, 1, 3, 5, 13], but got {result}"

def test_generate_odd_fibonacci_sequence_zero():
    """Test generating zero-length sequence."""
    assert generate_odd_fibonacci_sequence(0) == [], "Zero-length sequence should return empty list"

def test_generate_odd_fibonacci_sequence_one():
    """Test generating a sequence of length 1."""
    assert generate_odd_fibonacci_sequence(1) == [1], "One-length sequence should return [1]"

def test_generate_odd_fibonacci_sequence_negative_input():
    """Test that negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        generate_odd_fibonacci_sequence(-1)

def test_generate_odd_fibonacci_sequence_non_integer_input():
    """Test that non-integer input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a non-negative integer"):
        generate_odd_fibonacci_sequence("5")
    with pytest.raises(TypeError, match="Input must be a non-negative integer"):
        generate_odd_fibonacci_sequence(5.5)

def test_generate_odd_fibonacci_sequence_odd_only():
    """Verify that all generated numbers are odd."""
    result = generate_odd_fibonacci_sequence(10)
    assert all(num % 2 != 0 for num in result), "All numbers should be odd"