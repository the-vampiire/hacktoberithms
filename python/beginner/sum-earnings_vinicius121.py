a = "0,0,0,0,0,0"
b = "0,-1,-2,0"
c = "-1,-3,-4,-1,-2"
d = "qwerty"
e = ",,3,,4"
f = "1,2,v,b,3"
g = "0,7,0,2,-12,3,0,2"
h = "1,3,-2,1,2"


def sum_earnings(str_earn):

    next_value = 0
    total = 0
    neg_sum = 0
    if any(char.isalpha() for char in str_earn):
        return 0
    
    for s in str_earn.split(','):
        if not s:
            return 0
    
    lst = [int(s) for s in str_earn.split(',')]
    print(lst)
    
    if all(x <= 0 for x in lst):
        return 0
    
    for idx, val in enumerate(lst):
        total +=val
        if idx < len(lst)-1:
            next_value = lst[idx + 1]
        neg_sum = total + next_value
        if neg_sum <= 0:
            total = 0
            neg_sum = 0
    return total

print(sum_earnings(h))