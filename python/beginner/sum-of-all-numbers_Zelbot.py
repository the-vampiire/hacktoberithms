def sum_all(nums_list):
    nums_list = sorted(nums_list)
    sum_ = 0
    for i in range(nums_list[0], nums_list[1] + 1):
        sum_ += i

    return sum_

print(sum_all([1, 4]))
print(sum_all([4, 1]))
