#!/usr/bin/python3
def weight_average(my_list=[]):
    # Return 0 if the list is empty
    if not my_list:
        return 0
    
    # Initialize variables to store the sum of weighted scores and the sum of weights
    total_weighted_score = 0
    total_weight = 0
    
    # Iterate through the list of tuples
    for score, weight in my_list:
        total_weighted_score += score * weight
        total_weight += weight
    
    # Calculate and return the weighted average
    return total_weighted_score / total_weight if total_weight != 0 else 0

# Example usage:
if __name__ == "__main__":
    my_list = [(10, 2), (20, 1), (30, 3)]
    print(weight_average(my_list))  # Output: 23.333333333333332
