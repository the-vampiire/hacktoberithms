def sum_earning(string):
    values = string.split(',')
    # Handle non-number value errors
    for iteration, value in enumerate(values[:]):
        try:
            values[iteration] = int(value)
        except ValueError:
            return 0
    # Handle all negative number values
    if all(value <= 0 for value in values):
        return 0
    
    sum_ = 0
    for value in values:
        if sum_ + value < 0:
            sum_ = 0
            continue

        sum_ += value

    return sum_

# Expected outcomes: 5
print(sum_earning('1,3,-2,1,2'))
print(sum_earning('0,7,0,2,-12,3,0,2'))
# Expected outcomes: 0
print(sum_earning('0,0,0,0,0'))
print(sum_earning('-4,-3,-7,-1'))
print(sum_earning('qwerty'))
print(sum_earning(',,3,,4'))
print(sum_earning('1,2,v,b,3'))
