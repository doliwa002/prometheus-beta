def generate_odd_fibonacci_sequence(n):
    """
    Generate a Fibonacci sequence containing only odd numbers.

    Args:
        n (int): The number of odd Fibonacci numbers to generate.
                 Must be a non-negative integer.

    Returns:
        list: A list of n odd Fibonacci numbers.

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be a non-negative integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Handle edge cases
    if n == 0:
        return []
    
    if n == 1:
        return [1]
    
    # Initialize the sequence with the first odd Fibonacci numbers
    sequence = [1, 1]
    
    # Generate subsequent odd Fibonacci numbers
    while len(sequence) < n:
        next_num = sequence[-1] + sequence[-2]
        
        # Only add odd numbers to the sequence
        if next_num % 2 != 0:
            sequence.append(next_num)
    
    # Truncate or return the sequence to match the requested length
    return sequence[:n]