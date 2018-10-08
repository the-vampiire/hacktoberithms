def sum_all(li):
    sum = 0
    start = min(li)
    stop = max(li)
    for i in range(start,stop+1):
        sum += i
    return sum

print(sum_all([1,4]))
print(sum_all([4,1]))