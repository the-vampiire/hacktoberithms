def sum_earnings(a):
    try:
        c=0
        l=list(map(int, a.split(",")))
        for i in l:
            if i<0 and i*-1>c:
                c=0
            else:
                c+=i
        return c
    except ValueError:
        return 0

tests = ["1,3,-2,1,2", "0,7,0,2,-12,3,0,2", "-4,-3,-7,-1", "qwerty", ",,3,,4", "1,2,v,b,3"]

for test in tests:
    print(sum_earnings(test))