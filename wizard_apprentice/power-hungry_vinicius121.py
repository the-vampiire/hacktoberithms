a = [2, -3, 1, 0, -5, 0, 5]
b = [-2, -3, 4, -5, 5, 6]
c = [0,0,0,0,0,0] 
d = [-2, -3, 4, -5] #60
e = [0, -1, 0, 0] # 0
f = [-1] #-1
g = [2, -3, 1, 0, -5]

#lst[1:] == lst[:-1]
#all(x == val for x in list1)


def answer(lst):
    
    mult = 1

    if all(x == 0 for x in lst):
        print("all zeros")
        return 0
    elif len(lst) == 1:
        return lst[0]
    else:
        pos = [x for x in lst if x > 0]
        neg = [x for x in lst if x < 0]
        neg.sort()
    if len(neg) % 2 != 0:
        neg = neg[:-1]
    lst = pos + neg
    print(lst)
    if len(lst) == 0:
        return 0
    for a in lst:
        mult *= a
    return str(abs(mult))
    
print(answer(d))