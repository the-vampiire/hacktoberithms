def sum_earnings(input):
    try:
        # parse and convert input
        lst = list(map(int, input.split(',')))
    except:
        # in case of invalid input, returns 0
        return 0
    total = 0
    for nb in lst:
        total += nb
        if total < 0:
            total = 0
    return total


tests = [
    ('1,3,-2,1,2', 5),
    ('0,7,0,2,-12,3,0,2', 5),
    # negative
    ('0,0,0,0,0', 0),
    ('-4,-3,-7,-1', 0),
    # invalid
    ('qwerty', 0),
    (',,3,,4', 0),
    ('1,2,v,b,3', 0),
]


for test, excepted in tests:
    ret = sum_earnings(test)
    assert ret == excepted, '%s: %s != %s' % (test, ret, excepted)
