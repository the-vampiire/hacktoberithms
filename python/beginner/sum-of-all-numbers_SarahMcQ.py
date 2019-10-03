def  sum_all(numbers):
    ''' input list of 2 numbers returns sum of those two numbers 
    plus the sum of all numbers between them '''

total = 0
numbers = list(map(int, numbers))

for x in numbers:
    total += x

print(sum(range(total)))