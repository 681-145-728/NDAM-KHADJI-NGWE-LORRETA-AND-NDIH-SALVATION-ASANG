# -*- coding: utf-8 -*-
"""

@author: laureta
"""

# Function to count vowels in a string
def count_vowels(S):
    # Define a string containing all vowels
    vowels = "aeiouAEIOU"
    count = 0  # Initialize count to 0
    # Iterate through each character in the string
    for char in S:
        # Check if the character is a vowel
        if char in vowels:
            count += 1  # Increment count if it's a vowel
    return count  # Return the total count of vowels

# Get input string from user
S = input("Enter a string: ")

# Call the function to count vowels
print("Number of vowels:", count_vowels(S))
