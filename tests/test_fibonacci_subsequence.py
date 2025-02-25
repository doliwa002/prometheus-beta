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
    """Verify that the sum of even-indexed numbers is correct."""
    # Test a predefined set of known cases
    test_cases = [
        (0, [0]),        # 0 is the only option
        (2, [0, 1, 1, 2]),  # 0 + 2 = 2
        (8, [0, 1, 1, 2, 3, 5, 8]),  # 0 + 8 = 8
        (10, [0, 1, 1, 2, 3, 5, 8, 13]),  # 0 + 10 = 10
        (20, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),  # 0 + 20 = 20
        (50, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])  # 0 + 50 = 50
    ]
    
    for n, expected_sequence in test_cases:
        sequence = generate_fibonacci_subsequence(n)
        # Check that even-indexed sum matches the target
        even_sum = sum(sequence[i] for i in range(0, len(sequence), 2))
        assert even_sum == n, f"Failed for n={n}, sequence={sequence}"
        
        # Ensure the sequence is a valid Fibonacci-like sequence
        for i in range(2, len(sequence)):
            assert sequence[i] == sequence[i-1] + sequence[i-2], \
                f"Not a Fibonacci-like sequence at index {i}: {sequence}"