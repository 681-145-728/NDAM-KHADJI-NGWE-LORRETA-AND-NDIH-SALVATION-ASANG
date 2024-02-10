# -*- coding: utf-8 -*-
"""
0
@author: laureta
"""

#  convert Fahrenheit to Celsius
def fahrenheit_to_celsius(F):
    # Formula to convert Fahrenheit to Celsius
    C = (F - 32) / 1.8
    return C

# Input temperature in Fahrenheit 
F = float(input("Enter temperature in Fahrenheit: "))

# Call function to convert Fahrenheit to Celsius
C = fahrenheit_to_celsius(F)

# Display result
print("Temperature in Celsius:", C)


