# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 10:22:37 2024

@author: laureta
"""

def convert_to_mandarin(num_str):
    # Dictionary to map digits to Mandarin words
    trans = {'0': 'ling', '1': 'yi', '2': 'er', '3': 'san', '4': 'si', '5': 'wu', '6': 'liu', '7': 'qi', '8': 'ba', '9': 'jiu', '10': 'shi'}
    
    # Convert the input number string to an integer
    num = int(num_str)

    # Handle numbers between 0 and 10
    if num <= 10:
        return trans[num_str]

    # Handle numbers between 11 and 19
    elif num < 20:
        return 'shi ' + trans[num_str[1]]

    # Handle numbers between 20 and 99
    else:
        # Extract the tens and ones digits
        tens_digit = trans[num_str[0]]
        ones_digit = trans[num_str[1]]

        # If the ones digit is 0, return only the tens digit
        if ones_digit == 'ling':
            return tens_digit + ' shi'
        else:
            return tens_digit + ' shi ' + ones_digit

# Test cases
print(convert_to_mandarin('36'))  # Output: san shi liu
print(convert_to_mandarin('20'))  # Output: er shi
print(convert_to_mandarin('16'))  # Output: shi liu
