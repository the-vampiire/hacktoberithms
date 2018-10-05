from functools import reduce
from operator import mul


def answer(xs):
    positives = [x for x in xs if x > 0]
    negatives = sorted([x for x in xs if x < 0])
    # if result can be positive
    if positives or len(negatives) >= 2:
        # use even number of negativess
        if len(negatives) % 2 != 0:
            negatives = negatives[:-1]
        ret = reduce(mul, positives + negatives)
    elif 0 in xs:
        ret = 0
    else:
        # assume xs is one negative value, result must be negative
        ret = negatives[0]
    return str(ret)


tests = [
    ([2, 0, 2, 2, 0], "8"),
    ([-2, -3, 4, -5], "60"),
    # more tests
    ([0, -1, 0, 0], "0"),
    ([-1], "-1"),
]


for test, excepted in tests:
    ret = answer(test)
    assert ret == excepted, "%s: %s != %s" % (test, ret, excepted)
