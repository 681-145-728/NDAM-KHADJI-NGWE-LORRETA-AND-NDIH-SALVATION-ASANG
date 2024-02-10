# -*- coding: utf-8 -*-
"""


@author: laureta
"""

def calculate_balance(balance, annual_interest_rate, monthly_payment_rate):
    """
    Calculate the credit card balance after one year if only minimum monthly payments are made.
    """
    # Convert annual interest rate to monthly interest rate
    monthly_interest_rate = annual_interest_rate / 12.0
    
    # Initialize total paid
    total_paid = 0

    # Iterate over 12 months
    for month in range(1, 13):
        # Calculate minimum monthly payment
        minimum_payment = round(balance * monthly_payment_rate, 2)
        total_paid += minimum_payment  # Update total paid
        
        # Calculate unpaid balance
        unpaid_balance = balance - minimum_payment
        
        # Calculate interest for the month
        interest = round(monthly_interest_rate * unpaid_balance, 2)
        
        # Update balance for the next month
        balance = round(unpaid_balance + interest, 2)
        
        # Output monthly statement
        print("Month:", month)
        print("Minimum monthly payment:", minimum_payment)
        print("Remaining balance:", balance)

    # Output total paid and remaining balance at the end of the year
    print("Total paid:", total_paid)
    print("Remaining balance:", balance)


calculate_balance(4213, 0.2, 0.04)
print()
calculate_balance(4842, 0.2, 0.04)
