from typing import List
from collections import deque

def find_shortest_path(grid: List[List[int]]) -> int:
    """
    Find the shortest path length in a 2D grid maze from top-left to bottom-right.
    
    Args:
        grid (List[List[int]]): A 2D grid where 0 represents open paths and 1 represents walls.
        
    Returns:
        int: Length of the shortest path from top-left to bottom-right, 
             or -1 if no path exists.
    
    Raises:
        ValueError: If the grid is empty or None.
    """
    # Validate input
    if not grid or not grid[0]:
        raise ValueError("Grid cannot be empty")
    
    # Grid dimensions
    n = len(grid)
    
    # Possible movement directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Initialize visited set and queue for BFS
    visited = set()
    queue = deque([(0, 0, 0)])  # (row, col, path_length)
    
    while queue:
        row, col, path_length = queue.popleft()
        
        # Check if reached bottom-right
        if row == n - 1 and col == n - 1:
            return path_length
        
        # Skip if already visited or out of bounds or wall
        if ((row, col) in visited or 
            row < 0 or row >= n or 
            col < 0 or col >= n or 
            grid[row][col] == 1):
            continue
        
        # Mark as visited
        visited.add((row, col))
        
        # Explore adjacent cells
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            queue.append((new_row, new_col, path_length + 1))
    
    # No path found
    return -1