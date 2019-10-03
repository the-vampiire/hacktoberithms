def sum_all(n):
    n = sorted(n)
    out = 0
    for i in range(n[0], n[1]+1):
        out += i
    return out


print(sum_all([1, 4])) # >>> 10
print(sum_all([4, 1])) # >>> 10
print(sum_all([10, 25])) # >>> 280
print(sum_all([22, 12])) # >>> 187