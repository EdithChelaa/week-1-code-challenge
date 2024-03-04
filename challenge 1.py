def solution(A):
    N = len(A)
    target_bricks = 10
    
    # Calculate the total number of bricks in the array
    total_bricks = sum(A)
    
    # Check if it's possible to distribute bricks equally
    if total_bricks % N != 0:
        return -1
    
    # Calculate the target number of bricks per box
    target_per_box = total_bricks // N
    
    # Initialize the moves count
    moves = 0
    
    # Iterate through the boxes and calculate the moves needed
    for i in range(N):
        diff = A[i] - target_per_box
        
        # Update the current box
        A[i] = target_per_box
        
        # Update the next box if it's not the last one
        if i < N - 1:
            A[i + 1] += diff
            moves += abs(diff)
    
    return moves

# Examples
print(solution([7, 15, 10, 8]))  # Output: 7
print(solution([11, 10, 8, 12, 8, 10, 11]))  # Output: 6
print(solution([7, 14, 10]))  # Output: -1
