def sum_all(num_list):
    num_list = sorted(num_list)
    diff = num_list[1] - num_list[0]
    count = 0
    while diff > num_list[0] and diff > 0:
        count += diff
        diff -= 1
    return num_list[0] + num_list[1] + count


print(sum_all([1, 4]))
