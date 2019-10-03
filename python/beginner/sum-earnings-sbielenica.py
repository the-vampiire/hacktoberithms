
def sum_earning(input):

    streak = 0
    total_sum = 0

    for num in input:
        if num >= 0:
            streak += 1
            total_sum += num
        elif num < 0:
            streak = 0
            total_sum = 0

    return total_sum


print(sum_earning([0,7,0,2,-12,3,0,2]))
