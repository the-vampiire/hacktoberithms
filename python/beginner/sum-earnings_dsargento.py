def sum_earnings(input):
    earnings_list = input.split(',')
    earnings = 0
    spendings = 0
    for val in earnings_list:
        try:
            val = int(val)
        except ValueError:
            return 0
        if val >= 0:
            earnings += val
        else:
            spendings += val
        if earnings < (spendings * -1):
            spendings = 0
            earnings = 0
    val_sum = spendings + earnings
    if val_sum < 0:
        return 0
    return val_sum
