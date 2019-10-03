def sum_earnings(input):
    streak_sum = 0
    try:
        streak = list(map(int, input.split(',')))
        for num in streak:
            if num < 0 and num + streak_sum < 0:
                streak_sum = 0
            else:
                streak_sum += num
    except ValueError:
        return 0
    return streak_sum

assert(sum_earnings('1,3,-2,1,2') == 5)
assert(sum_earnings('0,7,0,2,-12,3,0,2') == 5)
assert(sum_earnings('0,0,0,0,0') == 0)
assert(sum_earnings('qwerty') == 0)
assert(sum_earnings(',,3,,4') == 0)
assert(sum_earnings('1,2,v,b,3') == 0)