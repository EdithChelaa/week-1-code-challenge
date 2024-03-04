def solution(N):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    # Calculate the number of occurrences for each letter
    occurrences_per_letter = N // 26
    remaining_letters = N % 26
    
    # Generate the string with equal occurrences of each letter
    result = alphabet * occurrences_per_letter + alphabet[:remaining_letters]
    
    return result
