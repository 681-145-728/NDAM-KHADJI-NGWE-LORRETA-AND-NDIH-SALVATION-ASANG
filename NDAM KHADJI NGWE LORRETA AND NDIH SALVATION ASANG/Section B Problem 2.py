# -*- coding: utf-8 -*-
"""


@author: laureta
"""

def calculate_fixed_payment(balance, annual_interest_rate):
   
    
    # Initialize monthly payment and balance
    monthly_payment = 10
    original_balance = balance
    
    # Iterate until balance becomes negative
    while balance > 0:
        # Reset balance for each iteration
        balance = original_balance
        
        # Calculate balance for each month with fixed monthly payment
        for month in range(12):
            # Calculate monthly interest
            monthly_interest_rate = annual_interest_rate / 12.0
            interest = monthly_interest_rate * balance
            
            # Update balance after payment and interest
            balance = (balance - monthly_payment) * (1 + monthly_interest_rate)
        
        # Increase monthly payment by 10 if balance is still positive
        if balance > 0:
            monthly_payment += 10
    
    # Print the lowest monthly payment
    print("Lowest Payment:", monthly_payment)


calculate_fixed_payment(4842, 0.2)
calculate_fixed_payment(5000, 0.18)
