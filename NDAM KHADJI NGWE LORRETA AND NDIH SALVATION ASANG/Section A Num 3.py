# -*- coding: utf-8 -*-
"""

@author: laureta
"""
import math  # Import the math module for square root function

# Function to compute roots of a quadratic equation
def quadratic_roots(a, b, c):
    # Compute the discriminant
    discriminant = b**2 - 4*a*c
    # Check if roots are real and distinct
    if discriminant > 0:
        # Calculate two real roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    # Check if roots are real and equal
    elif discriminant == 0:
        # Calculate a single real root
        root = -b / (2*a)
        return root, root
    else:
        # Calculate two complex roots
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

# Coefficients of the quadratic equation
a = 1.2
b = 2.3
c = -3.4

# Call the function to compute roots
root1, root2 = quadratic_roots(a, b, c)

# Print the roots
print("Root 1:", root1)
print("Root 2:", root2)
