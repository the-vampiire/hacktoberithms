#Sum of numbers

a = [1, 4]
b = [5, 1]

def sum_all(lst):
    return sum(range(min(lst), max(lst) + 1))
    
print(sum_all(a))