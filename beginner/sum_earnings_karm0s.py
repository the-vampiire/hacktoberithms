def sum_earnings(input):
    streak = 0
    for i in input.split(","):
        try:
            n = int(i)
            if n >=0:
                streak += n
            elif n < 0:
                if streak + n < 0:
                    streak = 0
                else:
                    streak += n
        except ValueError:
            return 0
    return streak


print(sum_earnings("1,3,-2,1,2")) # >>> 5
print(sum_earnings("0,7,0,2,-12,3,0,2")) # >>> 5
print(sum_earnings("3, 2, -4, 5, 1")) # >>> 6
print(sum_earnings("querty")) # >>> 0