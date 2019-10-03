from collections import Counter

def mutations(s1, s2):
    c1 = Counter(map(str.lower, s1))
    c2 = Counter(map(str.lower, s2))
    c1.subtract(c2)
    return all(n >= 0 for n in c1.values())

tests = [
    (["hello", "Hello"], True),
    (["hello", "hey"], False),
    (["Alien", "line"], True),
    (["hel", "heel"], False)
]

for test, excepted in tests:
    ret = mutations(*test)
    assert ret == excepted
