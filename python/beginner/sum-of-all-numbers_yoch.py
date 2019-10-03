def sum_all(numbers):
    a, b = numbers
    if a > b:
        a, b = b, a
    n = b - a + 1
    return (a + b) * n // 2

tests = [
    ([1, 4], 10),
    ([4, 1], 10),
]

for test, excepted in tests:
    ret = sum_all(test)
    assert ret == excepted, '%s: %s != %s' % (test, ret, excepted)
