"""
Challenge: Write a function that takes a list of two numbers
and return the sum of those two numbers plus the sum of all
the numbers between them.
"""

import random

lst = [random.randint(0,9) for i in range(2)]

def sum_all(lst):
    sum_nums = 0
    lst.sort()
    
    for num in range(lst[0], lst[1]+1):
            sum_nums += num

    print(lst)
    return sum_nums
