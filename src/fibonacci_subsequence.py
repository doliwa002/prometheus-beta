def generate_fibonacci_subsequence(n):
    """
    Generate a Fibonacci subsequence where the sum of even-indexed numbers equals n.
    
    Args:
        n (int): The target sum of even-indexed Fibonacci numbers.
    
    Returns:
        list: A Fibonacci subsequence meeting the specified condition.
    
    Raises:
        ValueError: If no valid subsequence can be found.
    """
    # Validate input
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    # Special case for 0
    if n == 0:
        return [0]
    
    # Try different subsequence lengths
    for length in range(2, 20):  # Reasonable limit to prevent infinite loops
        # Initialize Fibonacci-like sequence
        sequence = [0, 1]
        
        # Extend the sequence
        while len(sequence) < length:
            sequence.append(sequence[-1] + sequence[-2])
        
        # Check if sum of even-indexed numbers matches target
        even_sum = sum(sequence[i] for i in range(0, len(sequence), 2))
        
        if even_sum == n:
            return sequence
    
    # If no subsequence found
    raise ValueError(f"No Fibonacci subsequence found with even-indexed sum of {n}")