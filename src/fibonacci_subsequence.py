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
    
    # Generate full Fibonacci sequence first
    sequence = [0, 1]
    while max(sequence) <= n * 10:  # Ensure we can find subsequences
        sequence.append(sequence[-1] + sequence[-2])
    
    # Maximum search depth to prevent infinite loop
    MAX_DEPTH = len(sequence)
    
    # Try different subsequence lengths and start points
    for length in range(1, MAX_DEPTH):
        for start in range(MAX_DEPTH - length + 1):
            # Extract subsequence
            subsequence = [num for num in sequence[start:start+length] if num % 2 == 0]
            
            # Check if sum of even numbers matches target
            if subsequence and sum(subsequence) == n:
                # Rebuild the full subsequence that contains these even numbers
                full_subsequence = sequence[start:start+length]
                return full_subsequence
    
    # If no subsequence found
    raise ValueError(f"No Fibonacci subsequence found with even-indexed sum of {n}")