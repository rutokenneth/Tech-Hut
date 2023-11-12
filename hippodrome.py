def smallest_diff(strengths):
    """Finds the smallest difference between two numbers in a sorted array

    Args:
        strenght (int):A list of integers representing the strenghts of horses
    Returns:
        int: The smallest difference between two consecutive elements in the array.
    """
    
    strengths.sort()
    
    smallest_difference = int(1e9)
    
    #iterate ove the sorted array and compare the strenghts of adjacent pairs
    for i in range(len(strengths)-1):
        current_difference = abs(strengths[i] - strengths[i+1])
        if current_difference < smallest_difference :
            smallest_difference = current_difference
    return smallest_difference

strengths = [10, 20, 30, 40, 50] 
smallest_difference = smallest_diff(strengths)
print(smallest_difference)      