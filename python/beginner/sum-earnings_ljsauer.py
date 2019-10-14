"""
Challenge: Write a function that accepts a comma-separated
string input of earning/spending activity and returns the sum 
of earning as a single int value.

Requirements: If input is empty or invalid, return 0; if spending
(negative values) is greater than earning during the cumulative
addition of values, the count should start over from the remaining
values in input.
"""

def sum_earnings():
    values = input("Enter a string of whole numbers separated by commas (e.g. 1,-3,0,-4): ").split(',')
    earnings = 0
    for i in values:
        try:
            earnings = max(0, earnings + int(i))
        except ValueError:
            earnings = 0
            break
    print(earnings)
        
    return
    
