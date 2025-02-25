import pytest
from src.fibonacci_subsequence import generate_fibonacci_subsequence

def test_generate_fibonacci_subsequence_basic():
    """Test basic functionality with a few inputs."""
    # Test a known case for 2
    sequence_2 = generate_fibonacci_subsequence(2)
    assert sequence_2[0::2] == [0, 2]
    assert sum(sequence_2[0::2]) == 2
    
    # Test a case for 8
    sequence_8 = generate_fibonacci_subsequence(8)
    assert sequence_8[0::2] == [8]
    assert sum(sequence_8[0::2]) == 8

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
    """Verify that the sum of even-indexed numbers is correct."""
    def check_even_sum(n):
        sequence = generate_fibonacci_subsequence(n)
        even_sum = sum(sequence[i] for i in range(0, len(sequence), 2))
        assert even_sum == n, f"Failed for n={n}, sequence={sequence}"
    
    # Test various inputs
    test_inputs = [0, 2, 8, 10, 20, 50]
    for test_input in test_inputs:
        check_even_sum(test_input)