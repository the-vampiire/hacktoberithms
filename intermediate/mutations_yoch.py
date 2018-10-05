def mutations(s1, s2):
    return set(map(str.lower, s1)) >= set(map(str.lower, s2))

tests = [
    (["hello", "Hello"], True),
    (["hello", "hey"], False),
    (["Alien", "line"], True),
]

for test, excepted in tests:
    ret = mutations(*test)
    assert ret == excepted
