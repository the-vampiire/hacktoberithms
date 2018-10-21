# -*- coding: utf-8 -*-


def sum_all(n):
    n = sorted(n)
    out = 0
    for i in range(n[0], n[1]+1):
        out += i
    return out


print(sum_all([1, 4]))
print(sum_all([4, 1]))