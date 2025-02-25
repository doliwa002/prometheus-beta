import pytest
from src.fibonacci_subsequence import generate_fibonacci_subsequence

def test_generate_fibonacci_subsequence_basic():
    """Test basic functionality with a few inputs."""
    # Defined test cases
    assert generate_fibonacci_subsequence(2) == [0, 1, 1, 2]
    assert generate_fibonacci_subsequence(8) == [0, 1, 1, 2, 3, 5, 8]

def test_generate_fibonacci_subsequence_zero():
    """Test zero input."""
    assert generate_fibonacci_subsequence(0) == [0]

def test_generate_fibonacci_subsequence_errors():
    """Test error handling."""
    # Negative input
    with pytest.raises(ValueError, match="Input must be a non-negative integer."):
        generate_fibonacci_subsequence(-1)
    
    # Non-integer input
    with pytest.raises(ValueError, match="Input must be a non-negative integer."):
        generate_fibonacci_subsequence(3.14)
    
    # Impossible sum (very large)
    with pytest.raises(ValueError, match="No Fibonacci subsequence found"):
        generate_fibonacci_subsequence(1000000)

def test_generate_fibonacci_subsequence_even_indexed_sum():
    """Verify that the sequence follows Fibonacci rules."""
    # Verify known cases
    assert generate_fibonacci_subsequence(0) == [0]
    assert generate_fibonacci_subsequence(2) == [0, 1, 1, 2]
    assert generate_fibonacci_subsequence(8) == [0, 1, 1, 2, 3, 5, 8]
    
    # Check if sequence follows Fibonacci-like progression
    def check_fibonacci_sequence(sequence):
        # Check that each number (after first two) is sum of previous two
        for i in range(2, len(sequence)):
            assert sequence[i] == sequence[i-1] + sequence[i-2], \
                f"Not a Fibonacci-like sequence: {sequence}"
    
    # Test various sequences
    sequences = [
        generate_fibonacci_subsequence(0),
        generate_fibonacci_subsequence(2),
        generate_fibonacci_subsequence(8)
    ]
    
    for sequence in sequences:
        check_fibonacci_sequence(sequence)