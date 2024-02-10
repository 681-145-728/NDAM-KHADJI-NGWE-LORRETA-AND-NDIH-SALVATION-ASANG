# -*- coding: utf-8 -*-
"""

@author: laureta
"""

def longest_run(L):
   
    longest_length = 0       # Variable to store the length of the longest run
    longest_run_sum = 0      # Variable to store the sum of the longest run
    current_length = 1       # Variable to store the length of the current run
    current_run_sum = L[0]   # Variable to store the sum of the current run
    increasing = None        # Flag to indicate if the current run is increasing or decreasing

    # Iterate through the list starting from the second element
    for i in range(1, len(L)):
        # Check if the current number is greater than or equal to the previous number
        if L[i] >= L[i - 1]:
            # If the current run is decreasing or it's the first element of the list, start a new increasing run
            if increasing is False or increasing is None:
                current_length = 1
                current_run_sum = L[i]
            current_length += 1
            current_run_sum += L[i]
            increasing = True
        else:
            # If the current run is increasing or it's the first element of the list, start a new decreasing run
            if increasing is True or increasing is None:
                current_length = 1
                current_run_sum = L[i]
            current_length += 1
            current_run_sum += L[i]
            increasing = False

        # Update the longest run if the current run is longer
        if current_length > longest_length:
            longest_length = current_length
            longest_run_sum = current_run_sum
    
    return longest_run_sum

# Test cases
print(longest_run([10, 4, 3, 8, 3, 4, 5, 7, 7, 2]))  
print(longest_run([5, 4, 10]))                      
