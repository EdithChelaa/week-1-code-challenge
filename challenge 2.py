def solution(A):
    digit_sums = {}

    # Iterate through the numbers and calculate the digit sums
    for num in A:
        digit_sum = sum(map(int, str(num)))
        if digit_sum in digit_sums:
            digit_sums[digit_sum].append(num)
        else:
            digit_sums[digit_sum] = [num]

    # Find the maximum sum of two numbers with equal digit sums
    max_sum = -1
    for sums_list in digit_sums.values():
        if len(sums_list) >= 2:
            max_sum = max(max_sum, sum(sorted(sums_list)[-2:]))

    return max_sum
